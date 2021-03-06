from django.db.models import TextField, ManyToManyField, CharField

from foodsaving.base.base_models import BaseModel, LocationModel
from config import settings
from timezone_field import TimeZoneField


class Group(BaseModel, LocationModel):
    name = CharField(max_length=settings.NAME_MAX_LENGTH, unique=True)
    description = TextField(blank=True)
    members = ManyToManyField(settings.AUTH_USER_MODEL, related_name='groups')
    password = CharField(max_length=255, blank=True)
    public_description = TextField(blank=True)
    timezone = TimeZoneField(default='Europe/Berlin', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)
