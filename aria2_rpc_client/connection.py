from typing import Protocol
from xmlrpc.client import ServerProxy


class Connection(Protocol):
    def make_connection(self) -> ServerProxy:
        ...


class DefaultConnection:
    def __init__(self, host: str, port: str) -> None:
        self.host = host
        self.port = port

    def make_connection(self) -> ServerProxy:
        addr = f"http://{self.host}:{self.port}/rpc"
        return ServerProxy(addr)
