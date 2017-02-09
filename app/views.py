# -*- coding: utf-8 -*-
# @Author: dima
# @Date:   2017-02-07 11:44:41
# @Last Modified by:   Dima Sumaroka
# @Last Modified time: 2017-02-09 14:29:51
from app import app
from flask import render_template

@app.route('/', methods=['GET'])
def login():
    return render_template('home.html', apiKey = app.google_api_key, transitUrl = app.trasit_url)