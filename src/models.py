import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    userName= Column(String(200), nullable=False)
    password= Column(Integer,nullable=False)
    post_id=Column(ForeignKey('post.id'))
    post=relationship('Post')

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    video=relationship('Video')
    music=relationship('Music')
    
class Video(Base):
    __tablename__ ='video'
    id=Column(Integer,primary_key=True)
    name=Column(String(200),nullable=False)
    length=Column(Integer,nullable=False)
    type=Column(String(300),nullable=False)
    post_id=Column(Integer,ForeignKey('post.id'))

class Music(Base):
    __tablename__='music'
    id=Column(Integer,primary_key=True)
    type=Column(String(300),nullable=False)
    length=Column(Integer,nullable=False)   
    post_id=Column(Integer,ForeignKey('post.id')) 
  

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e