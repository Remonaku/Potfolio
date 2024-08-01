from flask import Flask, render_template, request
import test

app = Flask(__name__)

@app.route('/')
def home():
    # test.getData() 함수의 결과를 변수에 할당
    user_id, user_name, user_email, user_birth = test.getData()
    
    # render_template 함수에 전달
    return render_template('test.html', user_id=user_id, user_name=user_name, user_email=user_email, user_birth=user_birth)


if __name__ == '__main__':
    app.run(debug=True)