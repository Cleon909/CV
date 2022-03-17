from application import db
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
import pymysql

engine = create_engine('mysql+pymysql://root:todo@db/analytics', convert_unicode=True, echo=False)
# Base = declarative_base()
# Base.metadata.reflect(engine)

db.Model.metadata.reflect(db.engine)

class PageView(db.Model):
    __table__ = db.Model.metadata.tables['pageview']

    # __table__ = Table('pageview', Base.metadata, autoload_with=engine)
    #   id = AutoField()
    # domain = CharField()
    # url = TextField()
    # timestamp = DateTimeField(default=datetime.datetime.now, index=True)
    # title = TextField(default='')
    # ip = CharField(default='')
    # referrer = TextField(default='')
    # headers = JSONField()
    # params = JSONField()