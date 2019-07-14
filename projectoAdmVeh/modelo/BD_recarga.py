import sqlalchemy
from sqlalchemy import Column, Integer, String,Date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class _Recarga(Base):

    __tablename__ = "Recarga"

    id = Column(Integer, primary_key = True)
    precioCombustible = Column(Integer)#foreing key
    #valorRecarga = Column(Integer)
    fecha = Column(Date)
    idTacometro = Column(Integer)
    idVehiculo = Column(Integer)



def makeTable(eng):

    Base.metadata.create_all(bind =eng)
