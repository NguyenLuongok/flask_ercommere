from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from application.common.error_config import ErrorConfig
from application.common.validate import ItemSchema, PaginationSchema
from application.common.helper import pagination
from application.server import app, request, jsonify, render_template, redirect
from application.database import db
from application.model.model import Item
from application.common.sqlalchemy_helper import to_dict


@app.route("/")
def home():
    return render_template("index.html")