from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from alembic import op
import sqlalchemy as sa

db = SQLAlchemy()

class User(db.Model, UserMixin):
    
    #테이블 명 지정
    __tablename__ = "user"
    
    index = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    
    # is_active 속성 추가
    # is_active = db.Column(db.Boolean, default=True)
    
    # 역참조 가능
    # user_images = db.relationship("UserImage", backref="user")
    
    
# class UserImage(db.Model, UserMixin):
    # __tablename__ = "user_images"
    
    # id = db.Column(db.Integer, primary_key=True)
    # user_id는 models 테이블의 username 컬럼을 외부 키로 설정
    # user_id = db.Column(db.String(255), db.ForeignKey("user.email"), unique=True, nullable=False)
    # image_path = db.Column(db.String(255), nullable=False)
    # is_detected = db.Column(db.Boolean, default=False)
    # created_at = db.Column(db.DateTime, default=datetime.now)
    # updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    
    
    