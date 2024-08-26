class EasyRpaException(Exception):
    
    """基础自定义异常类，用于应用程序中的错误处理。"""
    def __init__(self, message, code=None, cause=None, data=None):
        """
        初始化自定义异常。

        :param message: 描述异常的字符串消息。
        :param code: 可选的整数错误代码。
        :param cause: 导致当前异常的另一个异常实例。
        :param data: 与异常相关的附加数据。
        """
        super().__init__(message)  # 调用基类的构造函数
        self.message = message
        self.code = code
        self.cause = cause
        self.data = data

    def __str__(self):
        """提供异常的字符串表示，方便调试和日志记录。"""
        cause_str = f", caused by {self.cause}" if self.cause else ""
        return f"{self.__class__.__name__}(code={self.code}, message={self.message}{cause_str})"

    def __repr__(self):
        """提供异常的官方字符串表示，包括所有属性。"""
        return (f"{self.__class__.__name__}(message={self.message!r}, code={self.code!r}, "
                f"cause={self.cause!r}, data={self.data!r})")

