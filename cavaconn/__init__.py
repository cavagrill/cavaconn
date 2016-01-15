#!/usr/bin/env python
import yaml

import psycopg2 as pg

from collections import namedtuple
from sqlalchemy import create_engine

def get_connections(path):
    # Shouts out to Josh Patchus for this connection code.
    with open(path, 'r') as f:
        yml = yaml.load(f)

        conn_str = 'postgresql://{}:{}@{}:{}/cavagrill'

        db = conn_str.format(yml['to_user'],
                             yml['to_pass'],
                             yml['to_server'],
                             str(yml['yml']))

    return create_engine(db)

def connect_twitter(path):
    ApiInfo = namedtuple('ApiInfo', 'access_token, access_token_secret, consumer_key, consumer_secret')

    with open(path, 'r') as f:
        yml = yaml.load(f)
        keys = ApiInfo(access_token=yml['access_token'],
                       access_token_secret=yml['access_token_secret'],
                       consumer_key=yml['consumer_key'],
                       consumer_secret=yml['consumer_secret'])

        return keys
