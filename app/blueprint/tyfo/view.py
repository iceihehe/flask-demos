# -*- coding = utf-8 -*-

from flask.views import MethodView

from app.blueprint.tyfo.database import Session


class ListView(MethodView):

    def get(self):
        """画像列表筛选"""

        return "xiba"