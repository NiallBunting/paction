
class BaseException(Exception):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return self.message

class ConfigError(BaseException):
    """Config Error"""