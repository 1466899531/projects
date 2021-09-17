
class AppiumException(Exception):
    def __init__(self, message):
        # 抛出异常信息
        super().__init__(message)
