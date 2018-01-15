# -*- coding = utf-8 -*-

from flask.views import MethodView
from sqlalchemy.orm import scoped_session

from app.blueprint.tyfo.database import Session
from app.blueprint.tyfo.model import SingleUserProfile


class FilterUserView(MethodView):

    def get(self):
        """画像列表筛选"""

        session = scoped_session(Session)

        users = session.query(SingleUserProfile).all()

        return "xiba"