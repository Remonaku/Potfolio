import torch
import numpy as np

import streamlit as st
from PIL import Image

import time
import os
import torch
import sys
import sys
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


import torchvision.transforms as transforms


import tempfile
import cv2


# CSS
st.markdown("""
<style>
	img {
        width: 46rem;
        padding: 5px;
        border: 2px solid #c8c8c8;
    }
</style>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Image Upload", "Video Upload"])



# 첫 번째 탭의 내용
with tab1:
    st.title('Mainboard parts Detect Tool',)

    uploaded_file = st.file_uploader('Please Upload files in this area', type=['jpg', 'jpeg', 'png'])
                                                                            #'jpg', 'jpeg', 'png','avi','mp4', 'mkv', 'wav'
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True) #caption='Uploaded Image'
        
        #####
        sys.path.insert(0, 'yolov5')

        sys.path.append('yolov5')  # YOLOv5 폴더 경로로 변경

        # 'custom' 모델 로드를 위한 hubconf.py 내의 함수 사용
        # 'path/to/best.pt'를 모델 파일의 실제 경로로 변경
        model = torch.hub.load('yolov5', 'custom', path='best.pt', source='local')

        # 모델을 평가 모드로 설정
        model.eval()


        # model = torch.load(r'yolov5\best.pt')
        # model.eval()

        temp = model(image)
        
        
        
        result = temp.save()
        
        re_img = Image.open('runs/detect/exp/image0.jpg')
        
        st.image(re_img)

        time.sleep(0.1)
        os.remove('runs/detect/exp/image0.jpg')
        time.sleep(0.1)
        os.rmdir('runs/detect/exp/')
    