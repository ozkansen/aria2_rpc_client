# How to using this package

## Installing

```
pip install aria2_rpc_client
```

## Using

```python
from aria2_rpc_client import DefaultClient
from aria2_rpc_client import DefaultConnection

connection = DefaultConnection("localhost", "6800", "top_secret_key")
client = DefaultClient(connection)

result = client.add_uri(["https://jell.yfish.us/media/jellyfish-15-mbps-hd-h264.mkv"])
print(result)
# 6be2fb970af88d07

remove_download = client.remove(result)
print(remove_download)
# 6be2fb970af88d07
```
