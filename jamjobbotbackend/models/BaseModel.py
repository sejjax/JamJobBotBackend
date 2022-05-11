from peewee import *
from jamjobbotbackend.misc.connect_db import connect_db

db = connect_db()


class BaseModel(Model):
    class Meta:
        database = db
