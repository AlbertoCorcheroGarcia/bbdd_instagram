import os
import sys
from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

association_table = Table('users_followers', Base.metadata,
    Column('user', Integer, ForeignKey('user.id')),
    Column('followers', Integer, ForeignKey('user.id'))
)


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String)
    mail = Column(String)
    bio = Column(String, nullable=True)
    follower = relationship("Follower",secondary=association_table)
    #follower = nombre de la columna 

    

# class Followers (Base):
#     __tablename__ = 'followers'
#     id = Column(Integer, primary_key=True)
#     id_user = Column (Integer, ForeignKey("user.id"))



        


class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normnamal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    media = Column(String(250))
    description= Column(String(250))
    id_user = Column (Integer, ForeignKey("user.id"))
    



class Coment(Base):
    __tablename__ = 'coment'
    id = Column(Integer, primary_key=True)
    text = Column(String(250))
    id_user = Column (Integer, ForeignKey("user.id"))
    id_post = Column (Integer, ForeignKey("post.id"))
    to_coment = relationship('user')



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e