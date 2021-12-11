class BaseClientException(Exception):
    def __init__(self, msg: str, from_exc: Exception) -> None:
        self.msg = msg
        self.from_exc = from_exc


class ConnectionRefusedException(BaseClientException):
    ...
