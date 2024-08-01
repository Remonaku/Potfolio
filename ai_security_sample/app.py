# 모듈 불러오기
from flask import Flask, url_for, render_template, request, session, redirect
import database


# app 인스턴스 생성 //////////////////////////////////////////////////////////
app = Flask(__name__)

# 시크릿 키
app.secret_key = '_@0339@033@33@3_'


# 라우팅 /////////////////////////////////////////////////
@app.route('/')
def main_page():
    if 'userID' in session:
        return render_template('main.html', username = session.get('userID'), login_status = True)
    else:
        return render_template('main.html', login_status = False)


@app.route('/login', methods = ['POST'])
def login_page():
    if request.method == "POST":
        input_id = request.form['login_id']
        input_pw = request.form['login_pw']
        
        login_id = database.selectId(input_id)
        login_pw = database.selectPw(input_id, input_pw)
        
        print(input_id, input_pw)
        print(login_id, input_pw)

    if login_id == input_id and login_pw == input_pw:
        # print(_id_, _password_)
        session['userID'] = input_id
        print('Identification Data is Certificated')
        return redirect(url_for('main_page'))
    
    
    else:
        return redirect(url_for('main_page'))


@app.route('/logout')
def logout_page():
    session.pop('userID')
    return redirect(url_for('main_page'))


@app.route('/signup')
def signup_page():
        return render_template('signup.html')


@app.route('/signup_done', methods = ['POST'])
def signup_done_page():
    # database.createTable()
    if request.method == "POST":
        signup_name =  request.form['signup_name']
        signup_id =  request.form['signup_id']
        signup_pw =  request.form['signup_pw']
        signup_email =  request.form['signup_email']
        
    print(signup_name, signup_id, signup_pw, signup_email)
    
    database.createData(signup_name, signup_id, signup_pw, signup_email)
        
    return redirect(url_for('main_page'))




# 실행 /////////////////////////////////////////////////
if __name__ == '__main__':
    # with app.test_request_context():
        Flask.debug
        app.run()