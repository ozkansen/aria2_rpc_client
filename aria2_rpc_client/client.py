from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Dict
from typing import List

from .connection import Connection
from .connection import DefaultConnection
from .options import FileDownloadOptions
from .types import GlobalStat
from .types import SessionInfo
from .types import Version


class Client(ABC):
    def __init__(self, connection: Connection = DefaultConnection()) -> None:
        self._connection = connection
        self._server = connection.make_connection()

    def _call(self, method: str, *params: Any) -> Any:
        response = self._server.__getattr__(method)(self._connection.secret, *params)
        return response

    @abstractmethod
    def add_uri(self, urls: List[str], options: FileDownloadOptions) -> str:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.addUri"""

        response = self._call("aria2.addUri", urls, options.export())
        return str(response)

    @abstractmethod
    def pause(self, gid: str) -> str:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.pause"""

        response = self._call("aria2.pause", gid)
        return str(response)

    @abstractmethod
    def force_pause(self, gid: str) -> str:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.forcePause"""

        response = self._call("aria2.forcePause", gid)
        return str(response)

    @abstractmethod
    def unpause(self, gid: str) -> str:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.unpause"""

        response = self._call("aria2.unpause", gid)
        return str(response)

    @abstractmethod
    def unpause_all(self) -> str:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.unpauseAll"""

        response = self._call("aria2.unpauseAll")
        return str(response)

    @abstractmethod
    def remove(self, gid: str) -> str:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.remove"""

        response = self._call("aria2.remove", gid)
        return str(response)

    @abstractmethod
    def force_remove(self, gid: str) -> str:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.forceRemove"""

        response = self._call("aria2.forceRemove", gid)
        return str(response)

    @abstractmethod
    def pause_all(self) -> str:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.pauseAll"""

        response = self._call("aria2.pauseAll")
        return str(response)

    @abstractmethod
    def force_pause_all(self) -> str:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.forcePauseAll"""

        response = self._call("aria2.forcePauseAll")
        return str(response)

    @abstractmethod
    def list_methods(self) -> List[str]:
        """https://aria2.github.io/manual/en/html/aria2c.html#system.listMethods"""

        response = self._call("system.listMethods")
        return list(response)

    @abstractmethod
    def get_global_stat(self) -> GlobalStat:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.getGlobalStat"""

        response = self._call("aria2.getGlobalStat")
        global_stat = GlobalStat(**response)
        return global_stat

    @abstractmethod
    def get_version(self) -> Version:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.getVersion"""

        response = self._call("aria2.getVersion")
        version = Version(**response)
        return version

    @abstractmethod
    def shutdown(self) -> str:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.shutdown"""

        response = self._call("aria2.shutdown")
        return str(response)

    @abstractmethod
    def force_shutdown(self) -> str:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.forceShutdown"""

        response = self._call("aria2.forceShutdown")
        return str(response)

    @abstractmethod
    def get_session_info(self) -> SessionInfo:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.getSessionInfo"""

        response = self._call("aria2.getSessionInfo")
        return SessionInfo(**response)

    @abstractmethod
    def save_session(self) -> str:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.saveSession"""

        response = self._call("aria2.saveSession")
        return str(response)

    @abstractmethod
    def get_option(self, gid: str) -> Dict[str, str]:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.getOption"""

        response = self._call("aria2.getOption", gid)
        return dict(response)

    @abstractmethod
    def get_global_option(self) -> Dict[str, str]:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.getGlobalOption"""

        response = self._call("aria2.getGlobalOption")
        return dict(response)

    @abstractmethod
    def purge_download_result(self) -> str:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.purgeDownloadResult"""

        response = self._call("aria2.purgeDownloadResult")
        return str(response)

    @abstractmethod
    def remove_download_result(self, gid: str) -> str:
        """https://aria2.github.io/manual/en/html/aria2c.html#aria2.removeDownloadResult"""

        response = self._call("aria2.removeDownloadResult", gid)
        return str(response)


class DefaultClient(Client):
    def add_uri(self, urls: List[str], options: FileDownloadOptions = None) -> str:

        if not options:
            options = FileDownloadOptions()

        result = super().add_uri(urls, options)
        return result

    def pause(self, gid: str) -> str:
        response = super().pause(gid)
        return response

    def force_pause(self, gid: str) -> str:
        response = super().force_pause(gid)
        return response

    def unpause(self, gid: str) -> str:
        response = super().unpause(gid)
        return response

    def unpause_all(self) -> str:
        response = super().unpause_all()
        return response

    def remove(self, gid: str) -> str:
        response = super().remove(gid)
        return response

    def force_remove(self, gid: str) -> str:
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

    def shutdown(self) -> str:
        response = super().shutdown()
        return response

    def force_shutdown(self) -> str:
        response = super().force_shutdown()
        return response

    def get_session_info(self) -> SessionInfo:
        response = super().get_session_info()
        return response

    def save_session(self) -> str:
        response = super().save_session()
        return response

    def get_option(self, gid: str) -> Dict[str, str]:
        response = super().get_option(gid)
        return response

    def get_global_option(
        self,
    ) -> Dict[str, str]:
        response = super().get_global_option()
        return response

    def purge_download_result(self) -> str:
        response = super().purge_download_result()
        return response

    def remove_download_result(self, gid: str) -> str:
        response = super().remove_download_result(gid)
        return response
