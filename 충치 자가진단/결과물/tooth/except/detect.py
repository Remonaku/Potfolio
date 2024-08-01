from flask_login import login_required,current_user,login_manager
from flask import Blueprint, render_template, request, flash, \
    jsonify, redirect, url_for, session

from PIL import Image
from io import BytesIO
import ultralytics
import math
from ultralytics import YOLO
import random
import uuid
from pathlib import Path
import cv2
import numpy as np
import torch
import torchvision
import base64

from werkzeug.utils import secure_filename
import os

#=========================================================================

detect_bp = Blueprint('detect',__name__)

#=========================================================================

@detect_bp.route('/detect')
def detect():
    if 'email' in session:
        return render_template('detect.html')
    else:
        return redirect(url_for('login'))
    
#=========================================================================

# YOLO 모델 불러오기
model_path = 'models/best.pt'
model = YOLO(model_path)

#=========================================================================

# img_upload
@detect_bp.route('/img_upload', methods=['POST', 'GET'])
def img_upload():
    
    if request.method == 'POST':
        
        # 업로드된 이미지 받아오기
        upload_img = request.files['file']
        
        # 안전한 파일명으로 변환
        filename = secure_filename(upload_img.filename)
        
        # 업로드된 이미지를 지정 디렉토리에 저장하기
        upload_save_path = os.path.join('user_img', 'upload_img', filename)
        upload_img.save(upload_save_path)
        
        # 이미지를 NumPy 배열로 변환
        userimg = np.array(Image.open(upload_save_path))

        # # 원하는 크기로 이미지 조정
        # target_width = 416
        # target_height = 416
        # resized_img = cv2.resize(userimg, (target_width, target_height))
        
        # # 채널 순서 변경
        # resized_img = cv2.cvtColor(resized_img, cv2.COLOR_RGB2BGR)

        # 정규화
        # normalized_img = userimg.astype(np.float32) / 255.0

        # 모델이 입력으로 요구하는 형식에 맞게 차원 변경
        # input_tensor = np.expand_dims(userimg.transpose(2, 0, 1), axis=0)
        
        project_path = 'project_path/predict'
        
        # yolo 모델 적용 및 반환
        result = model.predict(source=upload_save_path, save=True, save_txt=True, classes=[0], conf=0.65, project=project_path, device='cpu')
        print(result)
        
        # # 바운딩 박스와 클래스 정보 추출
        # boxes = result[0]['boxes']
        # labels = result.names
        
        # # 원본 이미지에 바운딩 박스 그리기
        # for box in boxes:
        #     x_min, y_min, x_max, y_max, confidence, class_index = box
        #     cv2.rectangle(userimg, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (255, 0, 0), 2)
        #     cv2.putText(userimg, labels[int(class_index)], (int(x_min), int(y_min) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
        # 결과 이미지를 PIL 이미지로 변환
        result_img = Image.fromarray(np.uint8(result))
        
        # 결과 이미지를 base64로 인코딩
        buffered = BytesIO()
        result_img.save(buffered, format="PNG")
        result_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        # 감지 결과와 base64 이미지를 json 형태로 반환
        return jsonify({"result": result.tolist(), "base64_image": result_base64})
    
#=========================================================================
        
        
        