from typing import Union, Optional
from os import environ

from environs import Env


def get_env(
    cast: Union[
        Env.str,
        Env.int,
        Env.enum,
        Env.path,
        Env.url,
        Env.date,
        Env.datetime,
        Env.bool,
        Env.decimal,
        Env.float,
        Env.json,
        Env.list,
        Env.log_level
    ],
    name: str,
    optional: bool = False
) -> Optional:
    if optional:
        return cast(environ.get(name)) if name in environ else None
    return cast(name)
