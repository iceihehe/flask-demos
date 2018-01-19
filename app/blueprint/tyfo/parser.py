# -*- coding = utf-8 -*-

from flask_restful.reqparse import RequestParser
from app.common.validator import address_check, range_above, range_time, int_check, float_int_check


filter_user = RequestParser()
area_selector_parser = RequestParser()
downloader_parser = RequestParser()
search_user = RequestParser()
user_id = RequestParser()
age_spacing = RequestParser()
category_name = RequestParser()
type_id = RequestParser()
address_param = RequestParser()

# filter user params
filter_user.add_argument("isVIP", location="json", type=int_check, default=-1)
filter_user.add_argument("activeGrade", location="json", action="append")
filter_user.add_argument("costGrade", location="json", action="append")
filter_user.add_argument("sex", location="json", type=int_check, default=-1)
filter_user.add_argument("featureTag", location="json", action="append")
filter_user.add_argument("count", location="json", type=int, default=10)
filter_user.add_argument("page", location="json", type=int, default=1)
filter_user.add_argument("address", location="json", type=address_check, required=True)
filter_user.add_argument("age", location="json", type=range_above, required=True)
filter_user.add_argument("lastLogin", location="json", type=range_time, required=True)
filter_user.add_argument("registerTime", location="json", type=range_time, required=True)
filter_user.add_argument("orderSum", location="json", type=range_above, required=True)
filter_user.add_argument("totalCost", location="json", type=float_int_check, required=True)
filter_user.add_argument("discountSum", location="json", type=range_above, required=True)
filter_user.add_argument("categoryId", location="json", type=int, required=True)


