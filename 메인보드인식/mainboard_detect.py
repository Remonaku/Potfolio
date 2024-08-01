import torch
import sys
from PIL import Image

import sys

# 
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


sys.path.insert(0, 'yolov5')

import sys
sys.path.append('yolov5')  # YOLOv5 폴더 경로로 변경

# 'custom' 모델 로드를 위한 hubconf.py 내의 함수 사용
# 'path/to/best.pt'를 모델 파일의 실제 경로로 변경
model = torch.hub.load('yolov5', 'custom', path='best.pt', source='local')

# 모델을 평가 모드로 설정
model.eval()


# model = torch.load(r'yolov5\best.pt')
# model.eval()
img = 'sample.jpg'

temp = model(img)

temp.print()

temp.save()
