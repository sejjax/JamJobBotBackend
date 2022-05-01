from app.app import get_app
from peewee import *

app = get_app()

db = PostgresqlDatabase(
    database=app.config.db.database,
    user=app.config.db.user,
    password=app.config.db.password,
    host=app.config.db.host,
    port=app.config.db.port
)


class BaseModel(Model):
    class Meta:
        database = db
