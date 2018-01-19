# -*- coding = utf-8 -*-
from flask import Blueprint
from flask_restful import Api

from app.blueprint.tyfo import view


tyfo = Blueprint("tyfo", __name__, url_prefix="/tyfo")
tyfo_api = Api(tyfo)

tyfo_api.add_resource(view.FilterUserView, "/demo")
