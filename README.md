# How to using this package

## Installing

```
pip install aria2_rpc_client
```

## Using

```python
from aria2_rpc_client import DefaultClient
from aria2_rpc_client import DefaultConnection
from aria2_rpc_client import FileDownloadOptions

# Make connection, enter aria2 rpc server information
connection = DefaultConnection("localhost", "6800", "top_secret_key")

# Make client
client = DefaultClient(connection)

# Download options
options = FileDownloadOptions()
options.set_filename("changed.mkv")
options.set_dir("/home/user/downloads")
options.add_header("token", "da78d676ds6a86dsa6d8sa6d8")

# Download start & set options
result = client.add_uri(["https://jell.yfish.us/media/jellyfish-15-mbps-hd-h264.mkv"], options)

# Get defined GID number from aria2
print(result)
# 6be2fb970af88d07

# Set download pause
pause_download = client.pause(result)
print(pause_download)
# 6be2fb970af88d07
```
