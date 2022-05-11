from peewee import Model

from jamjobbotbackend.misc import connect_db

db = connect_db()


class BaseModel(Model):
    class Meta:
        database = db
