#!/usr/bin/env python
import yaml

import psycopg2 as pg

from collections import namedtuple
from sqlalchemy import create_engine

def get_engine(path, db_name):
    # Shouts out to Josh Patchus for this connection code.
    with open(path, 'r') as f:
        yml = yaml.load(f)

        conn_str = 'postgresql://{}:{}@{}:{}/{}'

        db = conn_str.format(yml['to_user'],
                             yml['to_pass'],
                             yml['to_server'],
                             str(yml['to_port']),
                             db_name)

    return create_engine(db)

def get_connection(path, db_name):
    with open(path, 'r') as f:
        yml = yaml.load(f)
        conn_pg  = pg.connect(host = codes['to_server'],
                              port = codes['to_port'],
                              database = db_name,
                              user = codes['to_user'],
                              password = codes['to_pass'])

    return conn_pg

def connect_twitter(path):
    ApiInfo = namedtuple('ApiInfo', 'access_token, access_token_secret, consumer_key, consumer_secret')

    with open(path, 'r') as f:
        yml = yaml.load(f)
        keys = ApiInfo(access_token=yml['access_token'],
                       access_token_secret=yml['access_token_secret'],
                       consumer_key=yml['consumer_key'],
                       consumer_secret=yml['consumer_secret'])

        return keys
