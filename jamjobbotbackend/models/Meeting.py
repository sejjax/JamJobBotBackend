from peewee import DateTimeField, TimeField, IntegerField, TextField

from .BaseModel import BaseModel


class Meeting(BaseModel):
    time_start: DateTimeField()
    duration: TimeField()
    # Used enum: MeetingType
    type: IntegerField()
    # Used enum: MeetingServiceType
    service_type: IntegerField()
    # Link to interview can be: Phone Number, Telegram username or http link
    link: TextField()
