from dataclasses import dataclass

from environs import Env
from typing import List


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    api_id: str
    api_hash: str
    admin_ids: List[int]

@dataclass
class HttpServer:
    host: str
    port: str


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    httpserver: HttpServer
    db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            api_id=env.str("API_ID"),
            api_hash=env.str("API_HASH"),
            admin_ids=list(map(int, env.list("ADMINS"))),
        ),
        httpserver=HttpServer(
            host=env.str('HTTP_HOST'),
            port=env.int('HTTP_PORT')
        ),
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        ),
        misc=Miscellaneous()
    )
