#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _base import JsonBase
from misc._route import route

from model.task import Task


@route('/j/task/list')
class TaskList(JsonBase):
    def get(self):
        li = Task.select().where(Task.type == Task.TYPE.TODO).order_by(Task.index)
        li = [o.to_dict() for o in li]

        self.finish(dict(data=li))
