import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    follower_ID = Column(Integer, ForeignKey('follower.ID'))
    email = Column(String(250), nullable = False)

    # def __init__(self, name):
    #     if not name 
class Comment(Base):
    __tablename__ = 'comment'
    ID = Column(Integer, primary_key=True)
    Comment_text = Column(String(500), nullable=False)
    user_ID = Column(Integer, ForeignKey('user.ID'))
    post_ID = Column(Integer, ForeignKey('post.ID'))

class CommentLike(Base):
    __tablename__ = 'comment_like'
    ID = Column(Integer, primary_key=True)
    Comment_ID = Column(Integer, ForeignKey('comment.ID'))
    like = Column(Boolean, nullable=False)
    count = Column(Integer)

class CommentDisLike(Base):
    __tablename__ = 'comment_dislike'
    ID = Column(Integer, primary_key=True)
    Comment_ID = Column(Integer, ForeignKey('comment.ID'))
    like = Column(Boolean, nullable=False)
    count = Column(Integer)

class FollowerRequest(Base):
    __tablename__ = 'follow_request'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    follwer_ID = Column(Integer, ForeignKey('user.ID'))
    follwed_ID = Column(Integer, ForeignKey('user.ID'))
    accepted = Column(Boolean, nullable=False)

class Post(Base):
    __tablename__ = 'post'
    ID = Column(Integer, primary_key=True)
    Post = Column(String(500))
    user_ID = Column(Integer, ForeignKey('user.ID'))
    comment_ID = Column(Integer, ForeignKey('comment.ID'))


class Like(Base):
    __tablename__ = 'like'
    ID = Column(Integer, primary_key=True)
    post_ID = Column(Integer, ForeignKey('post.ID'))
    like = Column(Boolean, nullable=False)
    count = Column(Integer)


class DisLike(Base):
    __tablename__ = 'dislike'
    ID = Column(Integer, primary_key=True)
    post_ID = Column(Integer, ForeignKey('post.ID'))
    like = Column(Boolean, nullable=False)
    count = Column(Integer)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
