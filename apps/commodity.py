#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, request, g, session, redirect, url_for
from apps import app


@app.route('/commodity')
def commodity():
    return render_template("commodity.html", title='Commodity')