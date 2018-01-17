# -*- coding = utf-8 -*-
from sqlalchemy import Column, Integer, String, Float, DateTime, TEXT

from app.blueprint.tyfo.database import Base


class SingleUserProfile(Base):

    __tablename__ = "single_usr_profile"

    mb_id = Column(Integer, primary_key=True)
    sa_id = Column(Integer)
    mb_name = Column(String(1024))
    mb_petname = Column(String(1024))
    mb_loginname = Column(String(1024))
    mb_sex = Column(Integer)
    mb_age = Column(Integer)
    mb_mobile = Column(String(1024))
    mb_email = Column(String(1024))
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
    label_ids = Column(String(1024))
    statistic_time = Column(DateTime)
    mb_ordermoneysum = Column(Float)


class Categorynum(Base):

    __tablename__ = "categorynum"

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(1024))
    category_ordernum = Column(Integer)
    category_moneysum = Column(Float)
    category_avg = Column(Float)
    category_time = Column(Integer)


class EverydayLognum(Base):

    __tablename__ = "everyday_lognum"

    logdate = Column(Integer, primary_key=True)
    lognum = Column(Integer)


class LocationStatistic(Base):

    __tablename__ = "location_statistic"

    mb_province = Column(Integer)
    mb_city = Column(Integer)
    mb_county = Column(Integer, primary_key=True)
    ordernum = Column(Integer)
    moneysum = Column(Float)
    goodsnum = Column(Integer)
    timestamp = Column(Integer)


class MbAmiba(Base):

    __tablename__ = "mb_amiba"

    mb_id = Column(Integer, primary_key=True)
    amiba_id = Column(Integer)
    amiba_name = Column(String(1024))
    amiba_ordernum = Column(Integer)
    amiba_moneysum = Column(Float)
    amiba_goodsnum = Column(Integer)
    amb_date = Column(Integer)


class MbCategorynumEx(Base):

    __tablename__ = "mb_categorynum_ex"

    mb_id = Column(Integer, primary_key=True)
    category_id = Column(Integer)
    category_name = Column(String(1024))
    category_ordernum = Column(Integer)
    category_ordernum = Column(Integer)
    category_moneysum = Column(Float)
    category_date = Column(Integer)


class MbCfnum(Base):

    __tablename__ = "mb_cfnum"

    mb_id = Column(Integer, primary_key=True)
    cf_id = Column(Integer)
    cf_name = Column(String(1024))
    cf_ordernum = Column(Integer)
    cf_moneysum = Column(Float)
    cf_goodsnum = Column(Integer)
    cf_date = Column(Integer)


class MbLabel(Base):

    __tablename__ = "mb_label"

    mb_id = Column(Integer, primary_key=True)
    labelid = Column(Integer)
    label_date = Column(Integer)


class MbWordCloud(Base):

    __tablename__ = "mb_word_cloud"

    mb_id = Column(Integer, primary_key=True)
    word_cloud = Column(TEXT)
    updatetime = Column(Integer)
