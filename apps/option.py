#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, request, g, session, redirect, url_for
from apps import app


@app.route('/option')
def option():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template("option.html", title='Option')