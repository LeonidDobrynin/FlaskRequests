import atexit
from sqlalchemy import Column, String, Integer, Text, DateTime, create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

PG_DSN = 'postgresql://app:1234@127.0.0.1:5431/ultimate'

engine = create_engine(PG_DSN)

Base = declarative_base()
Session = sessionmaker(bind=engine)

atexit.register(engine.dispose)

class Announcement(Base):

    __tablename__ = 'app_announcement'

    id = Column(Integer, primary_key=True, autoincrement=True)
    header = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())
    username = Column(String, nullable=False, unique=True, index=True)

Base.metadata.create_all(bind=engine)
