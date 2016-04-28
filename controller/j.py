#!/usr/bin/env python
# -*- coding: utf-8 -*-

from _base import JsonBase
from misc._route import route

from model.task import Task


@route('/j/task/list')
class TaskList(JsonBase):
    def get(self):
        type_ = self.get_argument('type')
        li = Task.select().where(Task.type == type_).order_by(Task.index)
        li = [o.to_dict() for o in li]

        self.finish(dict(data=li))
