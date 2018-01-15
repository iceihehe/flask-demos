# -*- coding = utf-8 -*-
from app.common.util import config_mysql
from config import Config

Session, Base = config_mysql(
    Config.TYFO_SQLALCHEMY_DATABASE_URI,
    pool_size=Config.TYFO_SQLALCHEMY_POOL_RECYCLE,
    max_overflow=Config.TYFO_SQLALCHEMY_MAX_OVERFLOW,
    pool_recycle=Config.TYFO_SQLALCHEMY_POOL_RECYCLE
)

