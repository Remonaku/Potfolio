# from datetime import datetime

# from models import db

# class UserImage(db.Model):
#     __tablename__ = "user_images"
    
#     id = db.Column(db.Integer, primary_key=True)
#     # user_id는 models 테이블의 username 컬럼을 외부 키로 설정
#     user_id = db.Column(db.Integer, db.ForeignKey("user.index"))
#     image_path = db.Column(db.String(255))
#     is_detected = db.Column(db.Boolean, default=False)
#     created_at = db.Column(db.DateTime, default=datetime.now)
#     updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
# class UserImageTag(db.Model):
#     # 테이블명 지정
#     __tablename__ = "user_image_tags"
#     id = db.Column(db.Integer, primary_key=True)
#     # user_img_id는 user_images 테이블의 id 컬럼을 외부 키로 설정
#     user_img_id = db.Column(db.Integer, db.ForeignKey("user_images.id"))
#     tag_name = db.Column(db.String(255))
#     created_at = db.Column(db.DateTime, default=datetime.now)
#     updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    