#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model._base import Base
from peewee import CharField, IntegerField, PrimaryKeyField


class Task(Base):
    class TYPE(object):
        TODO = 1
        DOING = 2
        DONE = 3

    id = PrimaryKeyField()
    title = CharField(max_length=32)
    percent = IntegerField()
    create_time = IntegerField(index=True)
    index = IntegerField(index=True)
    type = IntegerField(default=TYPE.TODO)
