# -*- coding = utf-8 -*-

from sys import maxsize


def phone_check(data):
    """"""

    if len(data) != 11 or not data.startswith("1"):
        raise TypeError("invalid phone number")
    return data


def int_or_none(data):
    if not data:
        return data

    if isinstance(data, str) and data.isdigit():
        return int(data)

    if isinstance(data, int):
        return data

    raise TypeError("invalid type")


def user_name(data):
    if data is None or not isinstance(data, str) or len(data) > 20:
        raise TypeError("Wrong user name")

    for i in data:
        if not "\u4e00" <= i <= "\u9fff":
            raise TypeError("Wrong user name")

    return data


def role_name(data):
    if data is None or not isinstance(data, str) or len(data) > 10:
        raise TypeError("Wrong user name")

    for i in data:
        if not "\u4e00" <= i <= "\u9fff":
            raise TypeError("Wrong user name")

    return data


def address_check(data):
    """"""

    if not isinstance(data, dict):
        raise TypeError("Wrong params")

    address = list(data.keys())

    if "province" not in address or "city" not in address or "zone" not in address:
        raise TypeError("Wrong params")
    return data


def range_above(data):
    """"""

    if not isinstance(data, dict):
        raise TypeError("Wrong params")

    above = data.get("above", "")
    lower = data.get("lower", "")
    higher = data.get("higher", "")

    if not isinstance(above, int) or not isinstance(lower, int) \
            or not isinstance(higher, int):
        raise TypeError("Wrong params")
    if lower == higher == -1:
        return {"above": 1, "lower": -1, "higher": -1}
    return data


def float_int_check(data):

    if not isinstance(data, dict):
        raise TypeError("Wrong params")
    above = data.get("above", 1)
    lower = data.get("lower", 0)
    higher = data.get("higher", 0)
    if not isinstance(above, int):
        raise TypeError("Wrong params")
    if lower == higher == -1:
        return {"above": 1, "lower": -1, "higher": -1}
    return data


def range_time(data):

    if not isinstance(data, dict) or "end" not in list(data.keys()) or "start" not in list(data.keys()):
        raise TypeError("Wrong params")
    elif data["end"] == data["start"] == 0:
        return {"end": maxsize, "start": -maxsize}
    elif data["end"] * data["start"] == 0:
        return TypeError("Wrong params")
    return {"end": data["end"] / 1000, "start": data["start"] / 1000}


def int_check(data):
    """data is only int of -1, 0, 1, -1 is a default value and 0 stands for normal person, 1 stands for vip"""

    if not isinstance(data, int) or data not in [-1, 0, 1]:
        raise TypeError("Wrong params")
    return data


def date_parser(data):
    try:
        data = int(data)
    except Exception as e:
        raise TypeError("Date must be Int")
    return data / 1000
