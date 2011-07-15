#! /usr/bin/python

import web
from application import rtool


class Profile(rtool.page):

    path = "/profile"

    def GET(self):
        return web.ctx.render.profile(msg = "Denis")