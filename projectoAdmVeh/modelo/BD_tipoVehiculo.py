import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class _TipoVehiculo(Base):

    __tablename__ = "TipoVehiculo"

    id = Column(Integer, primary_key = True)
    tipo = Column(String(50))



def makeTable(eng):

    Base.metadata.create_all(bind =eng)
