# flask 클래스 import
from flask import Blueprint, render_template, request, flash, \
    jsonify, redirect, url_for, session
from flask_login import LoginManager, logout_user
from user import user_bp
from models import User,db
from markupsafe import escape
from flask_bcrypt import Bcrypt, check_password_hash

auth_bp = Blueprint('auth', __name__)

# =====================================================================

# 로그인
@auth_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User.query.filter_by(email=email).first()
        
        # db에 저장된 password와 입력 password가 같은 경우
        if user and check_password_hash(user.password, password):
            
            # 세션에 사용자 email과 username 저장
            session['email'] = user.email
            session['username'] = user.username
        
        else:
            # 로그인 실패 시 js를 통해 경고창 표시
            return """
            <script>
                alert("이메일과 비밀번호를 확인하세요.");
                window.location.href='/login';
            </script>
            """
            
        # 로그인 후 메인 페이지로 이동
        return redirect(url_for('main'))
    
    return render_template('login')

# =====================================================================

# 로그아웃
@auth_bp.route('/logout')
def logout():
    # 세션에서 사용자 정보 제거
    session.pop('email', None)
    
    # 로그아웃 후 메인 페이지로 이동
    return redirect(url_for('main'))