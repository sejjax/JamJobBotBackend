from peewee import *
from . import BaseModel


class HR(BaseModel):
    username = TextField()
    phone_number = TextField()
    email = TextField()
    name = TextField()
    # Vacancy of the company for which the candidate is looking for
    company = TextField()
