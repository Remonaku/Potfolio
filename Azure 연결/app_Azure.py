from flask import Flask, render_template, request
import database_Azure

app = Flask(__name__)

@app.route('/')
def home():
    # render_template 함수에 전달
    return render_template('info.html')


@app.route('/submit', methods = ['POST'])
def saveInfo():
    # POST 메소드 받으면 
    if request.method == 'POST':
        # 보낸 변수 할당
        user_name = request.form['user_name']
        user_id = request.form['user_id']
        user_pw = request.form['user_pw']
        user_birth = request.form['user_birth']
        user_email_f = request.form['user_email_front']
        user_email_b = request.form['user_email_behind']
        
        # database.py의 함수 사용
        database_Azure.inputData(user_name, user_id, user_pw, user_birth, user_email_f, user_email_b)
        
        print(user_name, user_id, user_pw, user_birth, user_email_f, user_email_b)
        
        # 반환 시에 jinja명 = 변수명도 같이 반환해야 jinja에서 사용가능
        return render_template('result.html', user_name = user_name, user_id = user_id, user_pw = user_pw, user_birth = user_birth, user_email_f = user_email_f, user_email_b = user_email_b)

if __name__ == '__main__':
    app.run(debug=True)