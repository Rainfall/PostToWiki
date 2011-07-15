#! /usr/bin/python

import web
from application import rtool
from login import Login


class Index(rtool.page):

    path = "/"

    def GET(self):
        return web.ctx.render.index(msg = "Denis")#msg = web.ctx.session.user)

  