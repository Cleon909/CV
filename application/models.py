from application import db
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:todo@db/analytics.db', convert_unicode=True, echo=False)
Base = declarative_base()
Base.metadata.reflect(engine)

class PageView(Base):
    __table__ = Base.metadata.tables['PageView']
