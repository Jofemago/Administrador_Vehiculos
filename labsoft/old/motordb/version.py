import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

print(sqlalchemy.__version__)
#engine = create_engine('sqlite:///./../db/foo.db',echo=True)
#engine = create_engine('sqlite:///./../foo.db')

engine = create_engine('sqlite:///foo.db')
#session = sessionmaker(bind = engine)()

#session.commit()


Base.metadata.create_all(bind =engine)#create the database and the model