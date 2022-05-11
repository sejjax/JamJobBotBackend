from typing import Union
from peewee import *
from .config import get_config, DBType


def connect_db() -> Union[PostgresqlDatabase, SqliteDatabase]:
    config = get_config()
    db_type = config.db.type

    db = None
    if db_type == DBType.POSTGRES:
        db = PostgresqlDatabase(
            database=config.db.database,
            user=config.db.user,
            password=config.db.password,
            host=config.db.host,
            port=config.db.port
        )
    elif db_type == DBType.SQLITE:
        db = SqliteDatabase(config.db.path)
    db.connect()
    return db
