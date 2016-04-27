#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import mako.lookup
import mako.template
import tornado.web


class Base(tornado.web.RequestHandler):
    def initialize(self):
        template_path = os.path.join(os.path.dirname(__file__), '..', 'template')
        self.lookup = mako.lookup.TemplateLookup(directories=template_path,
                                                 input_encoding='utf-8',
                                                 output_encoding='utf-8')

    def render_string(self, filename, **kwargs):
        kwargs["current_user"] = self.current_user
        template = self.lookup.get_template(filename)
        namespace = self.get_template_namespace()
        namespace.update(kwargs)

        return template.render(**namespace)

    def render(self, **kwargs):
        filename = "{0}.html".format(self._camel_to_underline(self.__class__.__name__))
        filename = "{0}{1}".format(filename[0].lower(), filename[1:])
        self.finish(self.render_string(filename, **kwargs))

    def get_current_user(self):
        pass

    def _camel_to_underline(self, camel_format):
        ''' 驼峰命名格式转下划线命名格式
        '''
        underline_format = ''
        if isinstance(camel_format, str):
            for i, _s_ in enumerate(camel_format):
                if i == 0:
                    underline_format += _s_ if _s_.islower() else _s_.lower()
                else:
                    underline_format += _s_ if _s_.islower() else '_' + _s_.lower()

        return underline_format
