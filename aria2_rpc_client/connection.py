from typing import Protocol
from xmlrpc.client import ServerProxy


class Connection(Protocol):
    host: str
    port: str
    secret: str

    def make_connection(self) -> ServerProxy:
        ...


class DefaultConnection:
    def __init__(
        self, host: str = "localhost", port: str = "6800", secret: str = ""
    ) -> None:
        self.host = host
        self.port = port
        self.secret = f"token:{secret}"

    def make_connection(self) -> ServerProxy:
        addr = f"http://{self.host}:{self.port}/rpc"
        return ServerProxy(addr)
