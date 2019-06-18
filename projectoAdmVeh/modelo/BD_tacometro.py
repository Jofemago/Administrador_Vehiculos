import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class _Tacometro(Base):

    __tablename__ = "Tacometro"

    id = Column(Integer, primary_key = True)
    idVehiculo = Column(Integer)#foreing key
    valorTacometro = Column(Integer)
    fecha = Column(String(50))


def makeTable(eng):

    Base.metadata.create_all(bind =eng)
