from flask import Flask, render_template, redirect, Response
import stream

app = Flask(__name__)

stream.video_detection()
    
@app.route('/video_feed')
def video_feed():
    return Response(stream.video_detection(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    # 'index.html'은 실시간 비디오를 보여줄 페이지
    return render_template('stream.html')

if __name__ == '__main__':
    app.run(debug=True, threaded=True, use_reloader=False)
