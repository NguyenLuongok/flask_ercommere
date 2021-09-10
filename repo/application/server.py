from flask import Flask, request, jsonify, url_for, render_template,\
    redirect, session
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from application.database import init_database
from .controller import init_view
from .config.config_dev import ConfigDevelop

app = Flask(__name__)
app.config.from_object(ConfigDevelop)
init_database(app)
init_view(app)
