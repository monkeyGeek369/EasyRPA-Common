from enum import Enum

class RpaExeResultCodeEnum(Enum):

    '''正常枚举99999'''
    SUCCESS = ('success', 99999, '成功')

    '''网络问题(10000-19999)
    10000-10099: 官网网络相关
    10100-10199: 本地网络相关
    10200-10299: 网络代理相关
    '''
    NET_WEBSITE_ERROR = ('net_website_error', 10001, '官网异常')
    NET_WEBSITE_SECURE_CHECK_ERROR = ('net_website_secure_check_error', 10002, '官网安全验证异常')

    NET_LOCAL_ERROR = ('net_local_error', 10100, '本地网络不通')

    NET_AGENCY_ERROR = ('net_agency_error', 10200, '网络代理异常')

    '''数据问题(11000-11999)
    11000-11099: 数据值相关
    11100-11199: 数据格式相关
    '''
    DATA_VALUE_NULL = ('data_value_null', 11000, '数据值为空')

    DATA_VALUE_INT_ERROR = ('data_value_int_error', 11100, '数据值不是整数')
    DATA_VALUE_FLOAT_ERROR = ('data_value_float_error', 11101, '数据值不是浮点数')
    DATA_VALUE_BOOL_ERROR = ('data_value_bool_error', 11102, '数据值不是布尔值')
    DATA_VALUE_STRING_ERROR = ('data_value_string_error', 11103, '数据值不是字符串')

    '''系统问题(12000-12999)
    12000-12099: 服务器问题
    12100-12199: 浏览器问题
    '''
    SYSTEM_OPT_ERROR = ('system_opt_error', 12000, '服务器异常')
    SYSTEM_OPT_UPDATE_ERROR = ('system_opt_update_error', 12001, '服务器系统更新异常')

    BROWSER_ERROR = ('browser_error', 12100, '浏览器异常')
    BROWSER_UPDATE_ERROR = ('browser_update_error', 12101, '浏览器更新异常')
    
    
    '''流程问题(13000-13999)
    13000-13099: 流程执行相关
    13100-13199: 浏览器识别相关
    13200-13299: 元素识别相关
    '''
    FLOW_EXE_ERROR = ('flow_exe_error', 13000, '流程执行未知异常')
    FLOW_EXE_DATA_ERROR = ('flow_exe_data_error', 13001, '流程执行结果数据异常')
    FLOW_EXE_PARAM_ERROR = ('flow_exe_param_error', 13002, '流程执行参数异常')

    FLOW_BROWSER_ERROR = ('flow_browser_error', 13100, '浏览器识别未知异常')

    FLOW_ELEMENT_ERROR = ('flow_element_error', 13200, '元素识别未知异常')
    FLOW_ELEMENT_MULTIPLE_ERROR = ('flow_element_multiple_error', 13201, '元素识别多个异常')
    FLOW_ELEMENT_NULL_ERROR = ('flow_element_null_error', 13202, '元素不存在')