# cavaconn
Connect to cava_servers to create SQLAlchemyEnginers, connect to APIs

## Installation

`$ git clone https://github.com/cavagrill/cava_connect.git && cd cava_connect`

`$ python setup.py install`

## Usage
a server_info.yml and a twitter_info.yml file should be placed in a directory

```python
import cavaconn as cc

# creates a SQLAlchemy engine object tied to our postgresql db
eng = cc.get_engine('server_info.yml', db_name)

# creates a PostgreSQL connection
conn = cc.get_connection('server_info.yml', db_name)

# creates a named_tuple object of twitter auth keys that can be accessed like api_keys.access_token
api_keys = cc.connect_twitter('twitter_info.yml')

# Executes a SQL Query on an existing PostgreSQL connection
q = """DROP TABLE IF EXISTS throwaway;"""
cc.pg_commit(conn, q)
```

## Example Yaml

```yaml
---
  access_token: 'a'
  access_token_secret: 'a'
  consumer_key: 'b'
  consumer_secret: 'b'
```
