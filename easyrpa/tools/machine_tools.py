import uuid,platform,subprocess,socket
from easyrpa.tools.blake3_tool import Blake3Tool

def get_machine_mac_id() -> str:
    mac_id = uuid.getnode()
    if mac_id is None or mac_id == 0:
        return None
    return str(mac_id)

def get_machine_cpu_id() -> str:
    cpu_id = platform.processor()
    if cpu_id is None:
        return None
    return cpu_id

def get_machine_disk_id() -> str:
    os_type = platform.system()
    result = None
    if os_type == "Windows":
        result = subprocess.check_output('wmic diskdrive get SerialNumber', shell=True)
        result = result.decode().split('\n')[1].strip()
    elif os_type == "Linux":
        result = subprocess.check_output('lsblk -o SERIAL', shell=True)
        result = result.decode().split('\n')[1].strip()
    elif os_type == "Darwin":  # macOS
        result = subprocess.check_output('diskutil info /dev/disk0 | grep "Device / Media Name:"', shell=True)
        result = result.decode().split(':')[1].strip()

    if result is None:
        return None
    
    return result

def get_main_board_id() -> str:
    os_type = platform.system()
    result = None
    if os_type == "Windows":
        result = subprocess.check_output('wmic baseboard get serialnumber', shell=True)
        result = result.decode().strip().split('\n')[1]
    elif os_type == "Linux":
        try:
            with open("/sys/devices/virtual/dmi/id/board_serial", 'r') as file:
                result = file.read().strip()
        except Exception as e:
            result = None
    elif os_type == "Darwin":
        result = subprocess.check_output('system_profiler SPHardwareDataType | grep Serial', shell=True)
        result = result.decode().strip().split(': ')[1]

    if result is None:
        return None
    
    return result

def get_machine_ips() -> list[str]:
    hostname = socket.gethostname()
    ips = socket.getaddrinfo(hostname, None)
    if ips is None:
        return None
    return [ip[4][0] for ip in ips]

def get_machine_id(salt:str,key:str,args:list[str]) -> str:
    if args is None or len(args) == 0:
        return None
    
    keys = None
    for arg in args:
        if arg is None:
            continue
        if keys is None:
            keys = arg
        else:
            keys = keys + arg

    tool = Blake3Tool(salt=salt, key=key)
    return tool.hash(keys)

if __name__ == '__main__':
    mac = get_machine_mac_id()
    print(mac)

    cpu_id = get_machine_cpu_id()
    print(cpu_id)

    disk_id = get_machine_disk_id()
    # 8CE3_8E03_0094_8A52_0000_0000_0000_0000.
    print(disk_id)

    board_id = get_main_board_id()
    # 240334518805292
    print(board_id)

    ip_list = get_machine_ips()
    print(ip_list)

    pass

