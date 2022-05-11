from peewee import *
from .BaseModel import BaseModel


class HR(BaseModel):
    telegram_chat_id = IntegerField()
    telegram_name = TextField()
    username = TextField(null=True)
    phone_number = TextField(null=True)
    email = TextField(null=True)
    # Vacancy of the company for which the candidate is looking for
    company = TextField(null=True)
