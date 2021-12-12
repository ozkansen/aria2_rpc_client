from typing import Optional


class BaseClientException(Exception):
    def __init__(self, msg: Optional[str] = None, from_exc: Optional[Exception] = None) -> None:
        self.msg = msg
        self.from_exc = from_exc

        super(Exception, self).__init__(self.msg, self.from_exc)


class ConnectionRefusedException(BaseClientException):
    ...
