# -*- coding = utf-8 -*-
from sys import maxsize

from flask_restful import Resource
from sqlalchemy import and_
from sqlalchemy.orm import scoped_session

from app.blueprint.tyfo import parser
from app.blueprint.tyfo.database import Session
from app.blueprint.tyfo.model import SingleUserProfile, MbLabel, MbCategorynumEx
from app.common.constant import CostGrade, ActiveGrade


class FilterUserView(Resource):

    def post(self):
        """画像列表筛选"""

        session = scoped_session(Session)

        req = parser.filter_user.parse_args()
        isVIP = req.get("isVIP")
        active_grade = req.get("activeGrade")
        cost_grade = req.get("costGrade")
        discount_sum = req.get("discountSum")
        tag_id = req.get("featureTag")
        sex = req.get("sex")
        address = req.get("address")
        age = req.get("age")
        last_login = req.get("lastLogin")
        register_time = req.get("registerTime")
        order_sum = req.get("orderSum")
        total_cost = req.get("totalCost")
        page = req.get("page", 1)
        count = req.get("count", 10)
        category_id = req.get("categoryId")

        # deal with the params about time
        login_start = last_login["start"]
        login_end = maxsize if last_login["end"] == 0 else last_login["end"]
        register_start = register_time["start"]
        register_end = maxsize if register_time["end"] == 0 else register_time["end"]

        # deal with the params about dict
        age_higher = maxsize if age["above"] else age["higher"]
        age_lower = -maxsize if age["lower"] == -1 else age["lower"]

        order_sum_higher = maxsize if order_sum["above"] else order_sum["higher"]
        order_sum_lower = -maxsize if order_sum["lower"] == -1 else order_sum["lower"]

        total_cost_higher = maxsize if total_cost["above"] else total_cost["higher"]
        total_cost_lower = -maxsize if total_cost["lower"] == -1 else total_cost["lower"]

        discount_sum_higher = maxsize if discount_sum["above"] else discount_sum["higher"]
        discount_sum_lower = -maxsize if discount_sum["lower"] == -1 else discount_sum["lower"]

        # sex 0, 1, 2, type of str or int
        sex = None if sex == -1 else sex
        is_vip = None if isVIP == -1 else isVIP

        expression = []

        if age_higher < maxsize:
            expression.append(SingleUserProfile.mb_age < age_higher)
        if age_lower > -maxsize:
            expression.append(SingleUserProfile.mb_age > age_lower)

        if order_sum_higher < maxsize:
            expression.append(SingleUserProfile.mb_ordernum < order_sum_higher)
        if order_sum_lower > -maxsize:
            expression.append(SingleUserProfile.mb_ordernum > order_sum_lower)

        if register_end < maxsize:
            expression.append(SingleUserProfile.mb_regdate < register_end)
        if register_start > -maxsize:
            expression.append(SingleUserProfile.mb_regdate > register_start)

        if discount_sum_higher < maxsize:
            expression.append(SingleUserProfile.mb_discountnum < discount_sum_higher)
        if discount_sum_lower > -maxsize:
            expression.append(SingleUserProfile.mb_discountnum > discount_sum_lower)

        if sex:
            expression.append(SingleUserProfile.mb_sex == sex)

        if is_vip:
            expression.append(SingleUserProfile.is_member == is_vip)

        if address:
            zone = address.get("zone")
            city = address.get("city")
            province = address.get("province")
            if zone:
                expression.append(SingleUserProfile.mb_county == zone)
            elif city:
                expression.append(SingleUserProfile.mb_city == city)
            elif province:
                expression.append(SingleUserProfile.mb_province == province)

        # 要跟costgrade联合组成筛选条件
        if cost_grade:
            cost_list = [CostGrade.grade.get(i) for i in cost_grade]
            cost_higer_list = [i["higher"] for i in cost_list]
            cost_lower_list = [i["lower"] for i in cost_list]
            cost_higer_list.append(total_cost_higher)
            cost_lower_list.append(total_cost_lower)
            total_cost_higher = min(cost_higer_list)
            total_cost_lower = max(cost_lower_list)

        if total_cost_lower < total_cost_higher:
            if total_cost_higher < maxsize:
                expression.append(SingleUserProfile.mb_moneysum < total_cost_higher)
            if total_cost_lower > -maxsize:
                expression.append(SingleUserProfile.mb_moneysum > total_cost_lower)

        # 要跟activegrade联合
        if active_grade:
            active_list = [ActiveGrade.grade.get(i) for i in active_grade]
            active_higer_list = [i["higher"] for i in active_list]
            active_lower_list = [i["lower"] for i in active_list]
            active_higer_list.append(login_end)
            active_lower_list.append(login_start)
            login_end = min(active_higer_list)
            login_start = max(active_lower_list)

        if login_start < login_end:
            if login_end < maxsize:
                expression.append(SingleUserProfile.mb_lastlogin < login_end)
            if login_start > -maxsize:
                expression.append(SingleUserProfile.mb_lastlogin > login_start)

        source = session.query(SingleUserProfile)

        if tag_id:
            source = source.join(MbLabel, SingleUserProfile.mb_id == MbLabel.mb_id)
            expression.append(MbLabel.labelid.in_(tag_id))

        if category_id:
            source = source.join(MbCategorynumEx, SingleUserProfile.mb_id == MbCategorynumEx.mb_id)
            expression.append(MbCategorynumEx.category_id == category_id)

        users = source.filter(and_(*expression)).group_by(SingleUserProfile.mb_id)
        total = users.count()

        start = (page - 1) * count
        users = users.slice(start, start + count).all()

        def detail(user):
            """

            :type user: SingleUserProfile
            """

            return {
                "mbId": user.mb_id,
                "mbName": user.mb_name,
                "mbOrdernum": user.mb_ordernum,
            }

        return {
            "total": total,
            "userList": [detail(i) for i in users]
        }
