import logging
from logging.handlers import RotatingFileHandler
from easyrpa.tools.json_tools import JsonTool
import json
import os
import sys
import threading
from easyrpa.enums.easy_rpa_exception_code_enum import EasyRpaExceptionCodeEnum
from easyrpa.models.easy_rpa_exception import EasyRpaException

# 创建日志目录
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 定义日志文件的路径
db_log_file = os.path.join(log_dir, "db.log")
business_log_file = os.path.join(log_dir, "business.log")
script_log_file = os.path.join(log_dir, "script.log")
api_log_file = os.path.join(log_dir, "api.log")

# 定义日志的格式为 JSON
class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'asctime': self.formatTime(record, self.datefmt),
            'name': record.name,
            'level': record.levelname,
            'message': record.getMessage()
        }
        # 额外的字段
        if hasattr(record, 'data'):
            log_record['data'] = record.data
        if hasattr(record, 'log_type'):
            log_record['log_type'] = record.log_type
        if hasattr(record, 'title'):
            log_record['title'] = record.title
        # 处理异常信息
        if record.exc_info:
            exception_info = self.formatException(record.exc_info)
            log_record['exception'] = exception_info
        return json.dumps(log_record, ensure_ascii=False)

# 配置日志记录器
def setup_logger(name, log_file, level=logging.INFO):
    # 创建一个日志记录器
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 创建一个文件处理器，并设置文件大小和备份数量
    file_handler = RotatingFileHandler(log_file, maxBytes=10485760, backupCount=5)
    file_handler.setLevel(level)

    # 创建 JSON 格式的格式化器
    formatter = JsonFormatter()
    file_handler.setFormatter(formatter)

    # 添加处理器到日志记录器
    logger.addHandler(file_handler)
    return logger

# 创建不同类型的日志记录器实例
db_logger = setup_logger('db_logger', db_log_file)
business_logger = setup_logger('business_logger', business_log_file)
script_logger = setup_logger('script_logger', script_log_file)
api_logger = setup_logger('api_logger', api_log_file)

# 基础日志记录函数
def log_message(logger, level, log_type, title, message, data=None, exc_info=None):
    logger.log(level, message, extra={'log_type': log_type, 'title': title, 'data': JsonTool.any_to_json(data)}, exc_info=exc_info)

# 数据库日志
def log_db_info(title, message, data=None):
    db_logger.log(logging.INFO, message, extra={'log_type': 'Database', 'title': title, 'data': JsonTool.any_to_json(data)}, exc_info=None)

def log_db_warn(title, message, data=None, exc_info=None):
    db_logger.log(logging.WARNING, message, extra={'log_type': 'Database', 'title': title, 'data': JsonTool.any_to_json(data)}, exc_info=exc_info)

def log_db_error(title, message, data=None, exc_info=None):
    db_logger.log(logging.ERROR, message, extra={'log_type': 'Database', 'title': title, 'data': JsonTool.any_to_json(data)}, exc_info=exc_info)


# 业务日志
def log_business_info(title, message, data=None):
    business_logger.log(logging.INFO, message, extra={'log_type': 'Business', 'title': title, 'data': JsonTool.any_to_json(data)}, exc_info=None)

def log_business_warn(title, message, data=None, exc_info=None):
    business_logger.log(logging.WARNING, message, extra={'log_type': 'Business', 'title': title, 'data': JsonTool.any_to_json(data)}, exc_info=exc_info)

def log_business_error(title, message, data=None, exc_info=None):
    business_logger.log(logging.ERROR, message, extra={'log_type': 'Business', 'title': title, 'data': JsonTool.any_to_json(data)}, exc_info=exc_info)

# 脚本日志
def log_script_info(title, message, data=None):
    script_logger.log(logging.INFO, message, extra={'log_type': 'Script', 'title': title, 'data': JsonTool.any_to_json(data)}, exc_info=None)

def log_script_warn(title, message, data=None, exc_info=None):
    script_logger.log(logging.WARNING, message, extra={'log_type': 'Script', 'title': title, 'data': JsonTool.any_to_json(data)}, exc_info=exc_info)

def log_script_error(title, message, data=None, exc_info=None):
    script_logger.log(logging.ERROR, message, extra={'log_type': 'Script', 'title': title, 'data': JsonTool.any_to_json(data)}, exc_info=exc_info)

# 接口日志
def log_api_info(title, message, data=None):
    api_logger.log(logging.INFO, message, extra={'log_type': 'Api', 'title': title, 'data': JsonTool.any_to_json(data)}, exc_info=None)

def log_api_error(title, message, data=None, exc_info=None):
    api_logger.log(logging.ERROR, message, extra={'log_type': 'Api', 'title': title, 'data': JsonTool.any_to_json(data)}, exc_info=exc_info)


# 全局异常捕获
def global_except_hook(exc_type, exc_value, exc_traceback):
    # 处理异常逻辑
    log_business_error(title="global_except_hook",message=str(exc_type),data=str(exc_value),exc_info=exc_traceback)

def thread_except_hook(args):
    # 处理异常逻辑
    log_business_error(title="thread_except_hook",message="thread",data=None,exc_info=args)

sys.excepthook = global_except_hook
threading.excepthook = thread_except_hook

# def throw_exception():
#     # 在线程中引发异常
#     raise Exception('not support jobstore:',{"key111":"value111","key222":222})

# def test_thread_except_hook():
#     # 创建一个新的线程
#     thread = threading.Thread(target=throw_exception)

#     # 设置线程异常捕获机制
#     threading.excepthook = thread_except_hook

#     # 启动线程
#     thread.start()

#     # 等待线程结束
#     thread.join()

# 使用日志记录器
if __name__ == "__main__":
    # 业务日志
    #log_message(business_logger, logging.INFO, 'Business', 'Business Info', 'This is a business info message')
    #log_message(business_logger, logging.ERROR, 'Business', 'Business Error', 'This is a business error message',{"key1":"value1","key2":2})

    # 数据库日志
    #log_message(db_logger, logging.INFO, 'Database', 'DB Info', 'Database operation successful')
    #log_message(db_logger, logging.ERROR, 'Database', 'DB Error', 'Database operation failed',{"key11":"value11","key22":22})

    # 脚本日志
    #log_message(script_logger, logging.WARNING, 'Script', 'Script Warning', 'This is a script warning message',{"key111":"value111","key222":222})

    # 全局异常
    #raise EasyRpaException('not support jobstore:',EasyRpaExceptionCodeEnum.DATA_TYPE_ERROR.value[1],{"key111":"value111","key222":222})
    #raise Exception('not support jobstore:',{"key111":"value111","key222":222})
    #test_thread_except_hook()


    # 异常日志
    try:
        1 / 0
    except Exception as e:
        log_message(business_logger, logging.ERROR, 'Business', 'Exception', 'An error occurred',{"key11111":"value11111","key22222":22222}, exc_info=e)