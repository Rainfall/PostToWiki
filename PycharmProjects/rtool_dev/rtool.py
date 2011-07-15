#! /usr/bin/python

import sys
import os.path
import os
import web
from web.contrib.template import render_jinja
from application import rtool
from controllers import *


# config path
working_dir = os.path.dirname(__file__)
sys.path.append(working_dir)
os.chdir(working_dir)

#config session and render
session = web.session.Session(rtool, web.session.DiskStore("session"))
render = render_jinja(
    "templates",
    encoding = "utf-8",
    )

def init_hook():
    web.ctx.session = session
    web.ctx.render = render
    web.template.Template.globals["session"] = session


rtool.add_processor(web.loadhook(init_hook))

if __name__ == "__main__":
    rtool.run()
