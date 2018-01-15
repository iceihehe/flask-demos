# -*- coding = utf-8 -*-


class Config:

    BLUEPRINTS = (
        "app.blueprint.tyfo:tyfo",
    )

    # tyfo的数据库
    TYFO_SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:root@127.0.0.1:3306/tyfo_data?charset=utf8"
    TYFO_SQLALCHEMY_POOL_SIZE = 30
    TYFO_SQLALCHEMY_MAX_OVERFLOW = 5
    TYFO_SQLALCHEMY_POOL_RECYCLE = 60