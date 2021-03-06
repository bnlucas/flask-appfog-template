"""
urls.py

URL dispatch route mappings and error handlers

"""
import os

from flask import render_template, abort

from application import app
from application import views


## URL dispatch rules
# Home page
app.add_url_rule('/', 'home', view_func=views.home)

# Say hello
app.add_url_rule('/hello/<username>', 'say_hello', view_func=views.say_hello)

# Env variables
app.add_url_rule('/_af/env', view_func=views.af_env)


## Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500
