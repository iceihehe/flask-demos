# -*- coding = utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def config_mysql(uri="", **kwargs):

    engine = create_engine(uri, **kwargs)
    session = sessionmaker(bind=engine)
    base = declarative_base(bind=engine)

    return session, base
