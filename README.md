# cavaconn
Connect to cava_servers to create SQLAlchemyEnginers, connect to APIs

## Installation

`$ git clone https://github.com/cavagrill/cava_connect.git && cd cava_connect`

`$ python setup.py install`

## Usage
a server_info.yml and a twitter_info.yml file should be placed in a directory

```python
import cavaconn as cc

eng = cc.get_connections('server_info.yml')

api_keys = cc.connect_twitter('twitter_info.yml')
```

## Example Yaml

```yaml
---
  access_token: 'a'
  access_token_secret: 'a'
  consumer_key: 'b'
  consumer_secret: 'b'
```
