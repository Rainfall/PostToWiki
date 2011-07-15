#! /usr/bin/python

import web
from application import rtool
from login import Login


class Event(rtool.page):

    path = "/event"

    def GET(self):
        return web.ctx.render.event(msg = "Denis")