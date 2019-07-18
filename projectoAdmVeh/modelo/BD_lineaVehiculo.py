import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class _LineaVehiculo(Base):

    __tablename__ = "LineaVehiculo"

    id = Column(Integer, primary_key = True)
    idTipoVehiculo= Column(Integer)#foreing key
    idMarcaVehiculo= Column(Integer)#foreing key
    linea = Column(String(150))


def makeTable(eng):

    Base.metadata.create_all(bind =eng)