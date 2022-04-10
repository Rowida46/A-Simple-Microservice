# Here is the file that defines our database connection using SQLAlchemy.

import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



SQLALCHEMY_DATABASE_URL = 'sqlite:///data.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# define your database models once! Using SQLAlchemy’s declarative_base()
Base = declarative_base() 