#!/usr/bin/env python
import yaml
import pymssql

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

def get_connstr(path, db_name):
    with open(path, 'r') as f:
        yml = yaml.load(f)

        conn_str = 'postgresql://{}:{}@{}:{}/{}'

        conn_str = conn_str.format(yml['to_user'],
                             yml['to_pass'],
                             yml['to_server'],
                             str(yml['to_port']),
                             db_name)
    return conn_str

def get_connection(path, db_name):
    with open(path, 'r') as f:
        yml = yaml.load(f)
        conn_pg  = pg.connect(host = yml['to_server'],
                              port = yml['to_port'],
                              database = db_name,
                              user = yml['to_user'],
                              password = yml['to_pass'])

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

def pg_commit(conn, q):
    cursor = conn.cursor()
    cursor.execute(q)
    conn.commit()
    return cursor

def get_MSSQL(path, db_name):
    with open(path, 'r') as f:
        yml = yaml.load(f)

        return pymssql.connect(str(yml['from_server']),
                           str(yml['from_user']),
                           str(yml['from_password']),
                           db_name, charset='utf8')

