# -*- coding = utf-8 -*-
from sqlalchemy import Column, Integer, String, Float, DateTime

from app.blueprint.tyfo.database import Base


class SingleUserProfile(Base):

    __tablename__ = "single_usr_profile"

    mb_id = Column(Integer, primary_key=True)
    sa_id = Column(Integer)
    mb_name = Column(String)
    mb_petname = Column(String)
    mb_loginname = Column(String)
    mb_sex = Column(Integer)
    mb_age = Column(Integer)
    mb_mobile = Column(String)
    mb_email = Column(String)
    mb_regdate = Column(Integer)
    mb_online = Column(Integer)
    mb_nowscores = Column(Integer)
    is_member = Column(Integer)
    mb_province = Column(Integer)
    mb_city = Column(Integer)
    mb_country = Column(Integer)
    mb_followgoodsnum = Column(Integer)
    mb_followshopsnum = Column(Integer)
    mb_trolleygoodsnum = Column(Integer)
    mb_firstorder = Column(Integer)
    mb_lastorder = Column(Integer)
    mb_firstlogin = Column(Integer)
    mb_lastlogin = Column(Integer)
    mb_loginnum = Column(Integer)
    mb_urgenum = Column(Integer)
    mb_delaynum = Column(Integer)
    mb_returnnum = Column(Integer)
    mb_moneysum = Column(Float)
    mb_avg = Column(Float)
    mb_lastyear_avg = Column(Float)
    mb_discountnum = Column(Integer)
    mb_freelogisticnum = Column(Integer)
    mb_ordernum = Column(Integer)
    mb_goodsnum = Column(Integer)
    mb_couponnum = Column(Integer)
    mb_couponednum = Column(Integer)
    mb_cp_moneynum = Column(Float)
    label_ids = Column(String)
    statistic_time = Column(DateTime)
    mb_ordermoneysum = Column(Float)
