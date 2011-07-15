#! /usr/bin/python

import web
from application import rtool
from web import form

from models import *
from models.mongo_database import *
from rtool import session


LoginForm = form.Form(
    form.Textbox("login", description="Login"),
    form.Password("password", description="Password"),
    form.Button("Login", type="submit", description="Login"),
    )

class Login(rtool.page):
    path = "/login"

    def GET(self):        
        return web.ctx.render.login(login_form = LoginForm(), msg="Anonymous")
    
    def POST(self):
        login_form = LoginForm()
        
        if not login_form.validates():
            return web.ctx.render.login(login_form = login_form, msg="Anonymous")

        web.ctx.session.user = login_form.value["login"]
        raise web.seeother("/")

