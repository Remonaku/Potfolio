# import streamlit as st 
# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import img_to_array, load_img
# from tensorflow.keras.applications import ResNet50
# from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
# import numpy as np
# from PIL import Image

# model = ResNet50(weights='imagenet')

# st.title('Image Classification')
# st.header('Choose as Image')

# uploaded_file = st.file_uploader('upload image...', type=['jpg', 'jpeg', 'png'])

# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption='uploaded image', use_column_width=True)
#     st.write("")
#     st.write('classifying...')
    
#     img = load_img(uploaded_file, target_size=(224,224))
#     img_array = img_to_array(img)
#     img_array_expanded_dims = np.expand_dims(img_array, axis=0)
#     processed_img = preprocess_input(img_array_expanded_dims)
    
#     predictions = model.predict(processed_img)
#     label = decode_predictions(predictions)
    
#     for i, (imagenet_id, desc, score) in enumerate(label[0]):
#         st.write(f"(i+1): {desc} ({score*100: .2f}%)")
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

from moviepy.editor import VideoFileClip
import torchvision.transforms as transforms


from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

import tempfile
import cv2


from moviepy.editor import concatenate_videoclips, VideoClip
from moviepy.video.io.ffmpeg_writer import FFMPEG_VideoWriter
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
        
        
        
        #####
        

# 두 번째 탭의 내용
# 두 번째 탭: 비디오 업로드
# 두 번째 탭의 내용: 비디오 업로드
# 두 번째 탭의 내용: 비디오 업로드
# 두 번째 탭의 내용: 비디오 업로드
# 두 번째 탭의 내용: 비디오 업로드
# 두 번째 탭: 비디오 업로드
with tab2:
    st.title('Mainboard parts Detect Tool - Video')
    