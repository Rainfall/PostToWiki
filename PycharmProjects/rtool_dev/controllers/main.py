#!/usr/bin/python

import web
from application import rtool


class Main(rtool.page):
    path = "/main"

    def GET(self):        
        return web.ctx.render.main(msg = web.ctx.session.user)
