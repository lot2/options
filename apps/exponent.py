#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, request, g, session, redirect, url_for
from apps import app


@app.route('/exponent')
def exponent():
    return render_template("exponent.html", title='Exponent')