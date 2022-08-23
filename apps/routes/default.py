# -*- coding:utf-8 -*-
from apps import app

@app.route('/')
def home():
    return("Hello world!")
