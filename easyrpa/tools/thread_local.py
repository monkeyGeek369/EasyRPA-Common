import threading

class ThreadLocalData:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ThreadLocalData, cls).__new__(cls)
                cls._threading_local = threading.local()
        return cls._instance

    def set_data(self, key, value):
        # 为当前线程设置数据
        if not hasattr(self._threading_local, 'data'):
            setattr(self._threading_local, 'data', {})
        self._threading_local.data[key] = value

    def get_data(self, key, default=None):
        # 获取当前线程的数据，如果数据不存在，则返回默认值
        data = getattr(self._threading_local, 'data', {})
        return data.get(key, default)

    def clear_data(self):
        # 清除当前线程的所有数据
        if hasattr(self._threading_local, 'data'):
            delattr(self._threading_local, 'data')


# 使用示例
def get_thread_local_data():
    return ThreadLocalData()

# 设置数据
#get_thread_local_data().set_data('user', 'Alice')

# 清除数据
#get_thread_local_data().clear_data()