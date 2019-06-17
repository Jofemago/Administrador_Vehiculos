import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#from createDatabase import makeEngine


Base = declarative_base()

class TipoVehiculo(Base):

    __tablename__ = "tipoVehiculo"

    id = Column(Integer, primary_key = True)
    tipo = Column(String(50))



def makeTableTipoVehiculo(eng):

    Base.metadata.create_all(bind =eng)