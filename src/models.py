import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class Register(Base):
    __tablename__ = 'register'
    ID = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable = False)
    password = Column(String(250), nullable = False)


class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    Register_ID = Column(Integer, ForeignKey('register.ID'))


class FollowRequest(Base):
    __tablename__ = 'follow_request'
    ID = Column(Integer, primary_key=True)
    user_from_ID = Column(Integer, ForeignKey('user.ID'))
    user_to_ID = Column(Integer, ForeignKey('user.ID'))
    accepted = Column(Boolean, default=False)

class Follower(Base):
    __tablename__ = 'follower'
    ID = Column(Integer, primary_key=True)
    user_from_ID = Column(Integer, ForeignKey('user.ID'))
    user_to_ID = Column(Integer, ForeignKey('user.ID'))

class Post(Base):
    __tablename__ = 'post'
    ID = Column(Integer, primary_key=True)
    user_ID = Column(Integer, ForeignKey('user.ID'))

class Media(Base):
    __tablename__ = 'media'
    ID = Column(Integer, primary_key=True)
    post_ID = Column(Integer, ForeignKey('post.ID'))
    type = Column(String(500))
    url = Column(String(250))
    
class Comment(Base):
    __tablename__ = 'comment'
    ID = Column(Integer, primary_key=True)
    Comment_text = Column(String(500), nullable=False)
    author_ID = Column(Integer, ForeignKey('user.ID'))
    post_ID = Column(Integer, ForeignKey('post.ID'))    
    like = Column(Boolean, nullable=False)
    dislike = Column(Boolean, nullable=False)

class CommentLike(Base):
    __tablename__ = 'comment_like'
    ID = Column(Integer, primary_key=True)
    Comment_ID = Column(Integer, ForeignKey('comment.ID'))
    count = Column(Integer)

class CommentDisLike(Base):
    __tablename__ = 'comment_dislike'
    ID = Column(Integer, primary_key=True)
    Comment_ID = Column(Integer, ForeignKey('comment.ID'))
    count = Column(Integer)

class PostLike(Base):
    __tablename__ = 'like'
    ID = Column(Integer, primary_key=True)
    post_ID = Column(Integer, ForeignKey('post.ID'))
    like = Column(Boolean, nullable=False)
    count = Column(Integer)


class PostDisLike(Base):
    __tablename__ = 'dislike'
    ID = Column(Integer, primary_key=True)
    post_ID = Column(Integer, ForeignKey('post.ID')) 
    dislike = Column(Boolean, nullable=False)   
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
