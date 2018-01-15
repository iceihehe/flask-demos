# -*- coding = utf-8 -*-
from flask import Blueprint

from app.blueprint.tyfo import view


tyfo = Blueprint("tyfo", __name__, url_prefix="/tyfo")

tyfo.add_url_rule("/demo", view_func=view.ListView.as_view("demo"))
