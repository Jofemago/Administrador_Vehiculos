import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class _Vehiculo(Base):


    __tablename__ = "Vehiculo"

    id = Column(Integer, primary_key = True)
    nombre = Column(String(10))
    idLineaVehiculo = Column(Integer)#foreing key
    idCombustible = Column(Integer)#foreing key


def makeTable(eng):

    Base.metadata.create_all(bind =eng)
