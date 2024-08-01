from flask import Blueprint, render_template, request, flash, \
    jsonify, redirect, url_for, session
from flask_login import login_user, login_required, current_user
from models import User, db
from flask_bcrypt import Bcrypt, check_password_hash

bcrypt = Bcrypt()

user_bp = Blueprint('user', __name__)

@user_bp.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        # 회원가입 로직 구현
        email = request.form['user_id'] + "@" + request.form['domain']
        password = request.form['password']
        # 비밀번호 해싱
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        username = request.form['username']
        phone = request.form['phone']
        address = request.form['adres1'] + request.form['adres2']
        
        # 데이터베이스에 사용자 정보 저장 등
        user = User(email=email,
                    password=password_hash,
                    username=username,
                    phone=phone,
                    address=address)
        db.session.add(user)
        db.session.commit()

        # 회원가입 성공 후 alert 메시지 표시 후 로그인 페이지로 리다이렉션
        return '''
            <script>
                alert('회원가입에 성공하셨습니다!');
                window.location.href = '/login';
            </script>
        '''
        
def check_pw(password, password_hash):
    return bcrypt.check_password_hash(password_hash, password)        
        
        
@user_bp.route('/check_id', methods = ['GET'])
def checkid():
    user_id = request.args.get('user_id')
    domain = request.args.get('domain')
    
    # user_id 또는 domain이 None이 아닌지 확인하고, None일 경우에는 기본값을 설정합니다.
    user_id = user_id if user_id else ''
    domain = domain if domain else ''

    email = user_id + "@" + domain

    # 이메일 중복 확인
    user = User.query.filter_by(email=email).first()
    if user:
        # 중복된 이메일 존재
        return jsonify({'exists': True})  
    else:
        # 중복된 이메일 존재하지 않음
        return jsonify({'exists': False})  