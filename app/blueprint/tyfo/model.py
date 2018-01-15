# -*- coding = utf-8 -*-
from sqlalchemy import Column, Integer, String

from app.blueprint.tyfo.database import Base


class SingleUserProfile(Base):

    __tablename__ = "single_usr_profile"
