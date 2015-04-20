__author__ = 'junger'
import datetime

from peewee import *

DATABASE = SqliteDatabase('solon.db')

class User(Model):
    username=CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)

    class Meta:
        database = DATABASE

