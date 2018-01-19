# -*- coding = utf-8 -*-
from sys import maxsize


class CostGrade:
    """消费等级"""

    grade = {
        "V1": {"lower": 0, "higher": 50},
        "V2": {"lower": 50, "higher": 200},
        "V3": {"lower": 200, "higher": 1000},
        "V4": {"lower": 1000, "higher": 10000},
        "V5": {"lower": 10000, "higher": maxsize}
    }


class ActiveGrade:
    """活跃等级"""
    grade = {
        "V1": {"lower": 0, "higher": 1},
        "V2": {"lower": 1, "higher": 5},
        "V3": {"lower": 5, "higher": 20},
        "V4": {"lower": 20, "higher": 100},
        "V5": {"lower": 100, "higher": maxsize}
    }
