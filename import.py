
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tqdm import tqdm

import csv

engine = create_engine("postgresql://postgres:srujan@localhost:5432/test")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Book(Base):
	__tablename__ = "Books"
	isbn = Column(String, primary_key = True)
	title = Column(String)
	year = Column(Integer)
	author = Column(String)


data = open('books.csv','rt')
Base.metadata.create_all(engine)
data = list(csv.reader(data))
for a in data[1:]:
	session.add( Book(isbn = a[0] , title = a[1] ,author = a[2] ,  year = int(a[3]) ))
session.commit()

