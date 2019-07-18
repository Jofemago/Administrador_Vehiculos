import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class _MarcaVehiculo(Base):


    __tablename__ = "MarcaVehiculo"

    id = Column(Integer, primary_key = True)
    idTipoVehiculo= Column(Integer)#foreing key
    marca = Column(String(100))


def makeTable(eng):

    Base.metadata.create_all(bind =eng)
