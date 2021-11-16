from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import List

from .connection import Connection
from .types import GID
from .types import GlobalStat
from .types import Version


class Client(ABC):
    def __init__(self, connection: Connection) -> None:
        self._connection = connection
        self.server = connection.make_connection()

    def call(self, method: str, *params: Any) -> Any:
        response = self.server.__getattr__(method)(self._connection.secret, *params)
        return response

    @abstractmethod
    def add_uri(self, urls: List[str], *params: Any) -> GID:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.addUri"""

        response = self.call("aria2.addUri", urls, *params)
        return GID(response)

    @abstractmethod
    def pause(self, gid: GID) -> GID:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.pause"""

        response = self.call("aria2.pause", gid)
        return GID(response)

    @abstractmethod
    def force_pause(self, gid: GID) -> GID:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.forcePause"""

        response = self.call("aria2.forcePause", gid)
        return GID(response)

    @abstractmethod
    def unpause(self, gid: GID) -> GID:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.unpause"""

        response = self.call("aria2.unpause", gid)
        return GID(response)

    @abstractmethod
    def unpause_all(self) -> str:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.unpauseAll"""

        response = self.call("aria2.unpauseAll")
        return str(response)

    @abstractmethod
    def remove(self, gid: GID) -> GID:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.remove"""

        response = self.call("aria2.remove", gid)
        return GID(response)

    @abstractmethod
    def force_remove(self, gid: GID) -> GID:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.forceRemove"""

        response = self.call("aria2.forceRemove", gid)
        return GID(response)

    @abstractmethod
    def pause_all(self) -> str:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.pauseAll"""

        response = self.call("aria2.pauseAll")
        return str(response)

    @abstractmethod
    def force_pause_all(self) -> str:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.forcePauseAll"""

        response = self.call("aria2.forcePauseAll")
        return str(response)

    @abstractmethod
    def list_methods(self) -> List[str]:
        """https://aria2.github.io/manual/en/html/aria2c.html#system.listMethods"""

        response = self.call("system.listMethods")
        return list(response)

    @abstractmethod
    def get_global_stat(self) -> GlobalStat:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.getGlobalStat"""

        response = self.call("aria2.getGlobalStat")
        global_stat = GlobalStat(**response)
        return global_stat

    @abstractmethod
    def get_version(self) -> Version:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.getVersion"""

        response = self.call("aria2.getVersion")
        version = Version(**response)
        return version


class DefaultClient(Client):
    def add_uri(self, urls: List[str], *params: Any) -> GID:
        result = super().add_uri(urls, *params)
        return result

    def pause(self, gid: GID) -> GID:
        response = super().pause(gid)
        return response

    def force_pause(self, gid: GID) -> GID:
        response = super().force_pause(gid)
        return response

    def unpause(self, gid: GID) -> GID:
        response = super().unpause(gid)
        return response

    def unpause_all(self) -> str:
        response = super().unpause_all()
        return response

    def remove(self, gid: GID) -> GID:
        response = super().remove(gid)
        return response

    def force_remove(self, gid: GID) -> GID:
        response = super().force_remove(gid)
        return response

    def pause_all(self) -> str:
        response = super().pause_all()
        return response

    def force_pause_all(self) -> str:
        response = super().force_pause_all()
        return response

    def list_methods(self) -> List[str]:
        response = super().list_methods()
        return response

    def get_global_stat(self) -> GlobalStat:
        response = super().get_global_stat()
        return response

    def get_version(self) -> Version:
        response = super().get_version()
        return response
