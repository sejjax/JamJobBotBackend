from typing import List, Optional
from enum import Enum
from dataclasses import dataclass

from environs import Env

from jamjobbotbackend.utils import get_env


class AppMode(Enum):
    DEVELOPMENT = 'development'
    PRODUCTION = 'production'


class DBType(Enum):
    SQLITE = 'sqlite'
    POSTGRES = 'postgres'


@dataclass
class DBConfig:
    type: DBType
    path: Optional[str]
    host: Optional[str]
    port: Optional[int]
    password: Optional[str]
    user: Optional[str]
    database: Optional[str]


@dataclass
class TgBot:
    api_id: int
    api_hash: str
    admin_ids: List[int]


@dataclass
class HttpServer:
    host: str
    port: int


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    mode: AppMode
    tg_bot: TgBot
    httpserver: HttpServer
    db: DBConfig
    misc: Miscellaneous


def get_config(path: str = None):
    env = Env()
    env.read_env(path)

    db_type = env.enum('DB_TYPE', type=DBType, ignore_case=True)
    db_config = None

    if db_type == DBType.SQLITE:
        db_config = DBConfig(
            type=db_type,
            path=get_env(env.str, 'DB_PATH'),
            host=get_env(env.str, 'DB_HOST', optional=True),
            port=get_env(env.int, 'DB_PORT', optional=True),
            password=get_env(env.str, 'DB_PASS', optional=True),
            user=get_env(env.str, 'DB_USER', optional=True),
            database=get_env(env.str, 'DB_NAME', optional=True),
        )
    elif db_type == DBType.POSTGRES:
        db_config = DBConfig(
            type=db_type,
            path=get_env(env.str, 'DB_PATH', optional=True),
            host=get_env(env.str, 'DB_HOST'),
            port=get_env(env.int, 'DB_PORT'),
            password=get_env(env.str, 'DB_PASS'),
            user=get_env(env.str, 'DB_USER'),
            database=get_env(env.str, 'DB_NAME'),
        )

    return Config(
        mode=env.enum('APP_MODE', type=AppMode, ignore_case=True),
        tg_bot=TgBot(
            api_id=env.str("API_ID"),
            api_hash=env.str("API_HASH"),
            admin_ids=list(map(int, env.list("ADMINS"))),
        ),
        httpserver=HttpServer(
            host=env.str('HTTP_HOST'),
            port=env.int('HTTP_PORT')
        ),
        db=db_config,
        misc=Miscellaneous()
    )
