# flask 클래스 import
from flask import Flask, render_template, request, jsonify, session, \
redirect, url_for, make_response

from models import User, db
from flask_migrate import Migrate

from flask_login import LoginManager

from user import user_bp
from auth import auth_bp
from detect import detect_bp


import secrets

#=========================================================================

# 무작위 시크릿 키 생성
secret_key = secrets.token_hex(16)

#=========================================================================

# flask 클래스 인스턴스화
app = Flask(__name__)

#=========================================================================

# 로그인 관련 설정
login_manager = LoginManager()
login_manager.init_app(app)
# 로그인이 필요한 페이지로 리디렉션할 라우트 설정
login_manager.login_view = 'login'

#=========================================================================

# 임의의 시크릿 키 설정
app.config['SECRET_KEY'] = secret_key

#=========================================================================

# DB주소 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://code:final0508!@dental.mysql.database.azure.com/cavity'

# models.py에서 생성한 db 객체를 초기화
db.init_app(app)

# Migrate 객체 초기화 및 애플리케이션과 SQLAlchemy 연결
migrate = Migrate(app, db)

#=========================================================================

# 회원가입과 로그인에 관련된 블루프린트 등록
# user
app.register_blueprint(user_bp)

# 로그아웃 및 세션 블루프린트 등록
# auth
app.register_blueprint(auth_bp)

# detect 
app.register_blueprint(detect_bp)

#=========================================================================

# URL과 실행 함수 매핑

# 메인페이지
@app.route('/')

def main():
    return render_template('main.html')
    
#=========================================================================

# 로그인/회원가입 페이지
@app.route('/login')
def login():
    return render_template('login.html')

# 아이디/비밀번호 찾기 페이지
# @app.route('/find')
# def project_04():
#     return render_template('page04.html')

#=========================================================================

# login_manager.user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#=========================================================================

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)