# -*- coding = utf-8 -*-

from pymongo import MongoClient
from sqlalchemy.orm import scoped_session

from app.blueprint.tyfo.database import Session
from app.blueprint.tyfo.model import SingleUserProfile

client = MongoClient("mongodb://tyfo:YNQ6OEn16SfNmLRA@192.168.20.182", authSource="hive")
db = client.hive


if __name__ == '__main__':

    session = scoped_session(Session)

    flag = 0
    total = db.single_usr_profile.count()
    for i in db.single_usr_profile.find():
        i.pop("_id")
        i["mb_lastyear_couponnum"] = i.pop("mb_ly_couponnum")
        d = {}
        for j in i.keys():
            if j in SingleUserProfile.__dict__:
                d[j] = i[j]
        a = SingleUserProfile(**d)
        session.add(a)
        if not flag % 200:
            session.commit()
        flag += 1
        print("{0}/{1}".format(flag, total))

    session.commit()
