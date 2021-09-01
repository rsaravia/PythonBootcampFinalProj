from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://roberto:password@localhost:3308/mydatabase")
Session = sessionmaker(bind=engine)
Session = Session()

Base = declarative_base()