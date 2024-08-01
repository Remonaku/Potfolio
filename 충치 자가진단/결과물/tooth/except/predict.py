#=========================================================================

# # YOLO 모델 불러오기

# # OpenCV의 dnn 모듈을 사용하여 YOLO 모델 로드
# # YOLO 모델의 아키텍처와 훈련된 가중치 정의
# # model = cv2.dnn.readNet('weights_file', 'cfg_file')

# model_path = "models/epoch200_batch5.pt"
# model = YOLO(model_path)

# # 객체 클래스의 이름 저장 리스트
# classes = []

# # YOLO 모델이 인식할 수 있는 객체 클래스들의 이름이 나열된 파일
# # 읽기 전용
# with open('models/data.yaml', 'r') as f:
#     # 각 줄을 클래스 이름으로 나눠 리스트 형태로 저장
#     classes = f.read().splitlines()

# # 클래스 이름 사용하여 객체 감지 후 결과 표시 가능

# @detect_bp.route('/img_upload', methods=['POST'])
# def img_upload():
#     # 결과 이미지 로컬 변수로 초기화
#     result_image = None

#     if request.method == 'POST':
#         if 'file' not in request.files:
#             return render_template('detect.html')
        
#         # 업로드 파일 가져오기
#         userimg = request.files['file']
        
#         # # 이미지를 바이트 형식으로 읽기
#         # image_bytes = userimg.read()
        
#         # # 바이트를 이미지로 디코딩
#         # nparr = np.fromstring(image_bytes, np.uint8)
#         # userimg = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

#         # # 이미지 전처리
#         # resized_img = cv2.resize(userimg, (model.width, model.height))

#         # 이미지를 임시 파일로 저장
#         # with tempfile.NamedTemporaryFile(delete=False) as temp_img:
#         #     temp_img.write(image_bytes)
#         #     temp_img_path = temp_img.name

#         # YOLO 모델 사용하여 객체 감지
#         detected_img = cv2.imread(userimg)
        
#         # 결과 이미지를 JPEG 형식으로 인코딩
#         result_image = np.array(detected_img.copy())
#         _, imgEncoded = cv2.imencode('.jpg', result_image)
        
#         # 바이트 형식의 이미지를 base64로 인코딩하여 문자열로 변환
#         # imgEncoded_base64 = base64.b64encode(imgEncoded)
        
#         return imgEncoded


# @detect_bp.route('/detect_upload', methods=['POST'])
# def result_upload():
        
#     if request.method == 'POST':
        
#         # img_upload() 함수를 호출
#         # 결과 이미지와 인코딩된 이미지 데이터 받기
#         imgEncoded_base64 = img_upload()

#         # JSON 응답 생성
#         response = {'image_data': imgEncoded_base64}
        
#         return jsonify(response)

#=========================================================================
#=========================================================================

# @predict_bp.route('/upload', methods=['POST'])
# def detectObj():
#     if request.method == 'POST':
        
#         #  업로드 파일 가져오기
#         userimg = request.files['file']
        
#         # 이미지 읽기
#         userimg = cv2.imdecode(np.fromstring(userimg.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        
#         # 이미지 전처리
#         resized_img = cv2.resize(userimg, (model.width, model.height))
        
#         # YOLO 모델 사용하여 객체 감지
#         detectedImg = model.detect_objects(resized_img)
        
#         # 결과 이미지를 jpg 형식으로 변환
#         _, imgEncoded = cv2.imencode('.jpg', detectedImg)
        
#         # 이미지 인코딩 후 클라이언트에게 전송
#         imgEncoded_data = base64.b64encode(imgEncoded).decode('utf-8')
#         response_img = {'imgData' : 'data:imge/jpg;base64' + imgEncoded_data}
        
#         return jsonify(response_img)
        
        # 인코딩된 이미지를 바이트 스트림으로 변환
        # return send_file(imgEncoded.tobytes(), mimetype='image/jpg')


#======================================================================
#======================================================================

# YOLO 모델 불러오기

#  OpenCV의 dnn 모듈을 사용하여 YOLO 모델 로드
# YOLO 모델의 아키텍처와 훈련된 가중치 정의
# model = cv2.dnn.readNet('weights_file', 'cfg_file')

# model_path = "models/epoch200_batch5.pt"
# model = YOLO(model_path)

# 객체 클래스의 이름 저장 리스트
# classes = []

# # YOLO 모델이 인식할 수 있는 객체 클래스들의 이름이 나열된 파일
# # 읽기 전용
# with open('models/data.yaml', 'r') as f:
#     # 각 줄을 클래스 이름으로 나눠 리스트 형태로 저장
#     classes = f.read().splitlines()
    
# # 클래스 이름 사용하여 객체 감지 후 결과 표시 가능

# #======================================================================

# # 이미지를 읽고 디코딩하여 OpenCV의 이미지 형식으로 변환하는 과정

# @predict_bp.route('/upload', methods=['POST'])
# def upload():
    
#     # 업로드된 파일 가져오기
#     user_img = request.files['file']
    
# #------------------------------------------------------------------
    
#     # 이미지 읽기
#     img = cv2.imdecode(np.fromstring(user_img.read(), np.uint8), cv2.IMREAD_UNCHANGED)
        
#     # userImg.read()
#     # 이미지 파일의 내용을 바이트 스트림으로 읽어오기
    
#     # np.fromstring()
#     # 넘파이 배열(8비트 부호 없는 정수)로 변환
    
#     # cv2.IMREAD_UNCHANGED
#     # 넘파이 배열을 이미지로 디코딩
#     # 디코딩된 이미지는 userImg에 저장
    
# #------------------------------------------------------------------
    
#     # 이미지 크기 가져오기
#     height, width, _ = img.shape
        
#     # (높이, 넓이, 채널 수) 튜플 형태
#     # 채널 수 사용하지 않는 경우, _로 표시
    
# #------------------------------------------------------------------
    
#     # YOLO 입력 이미지에 대한 출력 레이어 이름 가져오기
    
#     # 모델의 모든 레이어 이름 반환
#     layer_names = model.getLayerNames()
#     # 모델의 출력 레이어 이름
#     output_layers = [layer_names[i[0]-1] for i in model.getUnconnectedOutLayers()]
    
#     # model.getUnconnectedOutLayers()
#     # 연결되지 않은 출력 레이어의 인덱스 반환
#     # 출력 레이어 : 객체 감지 담당 마지막 레이어
    
#     # layer_names[i[0]-1]
#     # 해당 레이어의 이름 가져오기
#     # 인덱스는 0부터 시작하지 않기 때문에 -1
    
#     #------------------------------------------------------------------
    
#     # 이미지 전처리
    
#     resizeImg = cv2.resize(img, (416,416))
#     preprocessingImg = cv2.dnn.blobFromImage(img, 0.00392, (416,416), swapRB=True, crop=False )
    
#     # Blob
#     # 딥러닝 모델에 입력되는 이미지 데이터의 형식을 정의하는 컨테이너
    
#     # userImg : 입력 이미지
    
#     # scalefactor
#     # 이미지 크기 조정을 위한 스케일 팩터
#     # 입력 이미지의 각 픽셀 값에 곱하여 크기 조정
#     # 0.00392
#     # 이미지의 각 픽셀값을 255로 나눈 것과 같음
    
#     # size
#     # Blob의 크기를 지정하는 튜플
#     # 일반적으로 YOLO 모델은 (416,416)크기의 이미지를 입력으로 사용
    
#     # mean
#     # 입력 이미지에서 빼줄 평균값
#     # (0,0,0) : 변화 없음
    
#     # swapRB
#     # 이미지 색상 채널 변경 여부 결정 플래그
#     # BRG가 기본, True로 설정하여 RGB 순서로 변경
    
#     # crop
#     # Blob을 잘라낼지 여부 결정 플래그
#     # False : 잘라내지 않음
    
#     #------------------------------------------------------------------
    
#     # 전처리된 이미지를 네트워크에 전달하여 객체 감지 수행
    
#     # YOLO 모델에 입력 이미지 설정
#     model.setInput(preprocessingImg)
#     # 순방향 실행
#     out_img = model.forward(output_layers)
    
#     #------------------------------------------------------------------
    
#     # 감지된 객체 정보를 저장할 리스트 초기화
    
#     # 경계 상자 좌표 저장 리스트 초기화 (x, y, width, height)
#     boxes = []
#     # 신뢰도 저장 리스트 초기화
#     # 해당 객체가 실제로 존재하는 정도를 나타내는 지표 (0 ~ 1)
#     confidences = []
#     # 클래스 식별자(class id) 저장 리스트 초기화
#     # 각 객체가 어떤 클래스에 속하는지를 나타내는 정수값
#     class_ids = []
    
#     #------------------------------------------------------------------
    
#     # 각 레이어의 처리 결과
    
#     # YOLO 모델의 출력으로부터 얻은 이미지에 대한 감지 결과를 담은 리스트
#     for result in out_img:
#         for detection in result:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
            
#             if confidence > 0.5:
#                 # 객체의 중심 좌표와 너비/높이 계산
#                 box = detection[0:4] * np.array([width, height, width, height])
#                 centerX, centerY, w, h = box.astype("int")
                
#                 # 객체의 좌상단 좌표 계산
#                 x = int(centerX - (w / 2))
#                 y = int(centerY - (h / 2))

#                 # 객체의 중심을 중심으로 하는 경계 상자 얻을 수 있음
                
#                 #------------------------------------------------------
                
#                 # 객체의 정보 및 신뢰도 저장
#                 # 결과 리스트에 추가
#                 boxes.append([x, y, int(w), int(h)])
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)
                
#     # -----------------------------------------------------------------
#     # 경계 상자 그리기 및 레이블 표시
#     for i in range(len(boxes)):
#         x, y, w, h = boxes[i]
#         label = f"{classes[class_ids[i]]}: {confidences[i]:.2f}"
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 2)
#         cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
        
    
#     # 결과 이미지 반환
#     _, imgEncoded = cv2.imencode('.jpg', img)
#     response = send_file(imgEncoded.tobytes(), mimetype='image/jpg')
    
#     return response

#=========================================================================
#=========================================================================

# # YOLO 모델 불러오기
# model_path = 'models/best.pt'
# model = YOLO(model_path)

# # # 객체 클래스의 이름 저장 리스트
# classes = []

# # YOLO 모델이 인식할 수 있는 객체 클래스들의 이름이 나열된 파일
# # 읽기 전용
# with open('models/best.yaml', 'r') as f:
#     # 각 줄을 클래스 이름으로 나눠 리스트 형태로 저장
#     classes = f.read().splitlines()

# # 클래스 이름 사용하여 객체 감지 후 결과 표시 가능

# #=========================================================================
# #=========================================================================

# @detect_bp.route('/img_upload', methods=['POST'])
# def img_upload():
    
#     if request.method == 'POST':
    
#         try:
#             # 업로드 이미지 파일 가져오기
#             file = request.files['imgData']
#             print("이미지 업로드 성공")
            
#             # 임시 파일로 저장
#             with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as saveimg:
#                 file.save(saveimg.name)
#                 save_path = saveimg.name
            
#             user_img = cv2.imread(save_path)
#             project_path = 'models/detected_img'
#             result = model.predict(source=user_img, save=True, save_txt=True, classes=[0], conf=0.65, project=project_path, device='cpu')
#             print("detect 성공")
            
#             # 임시 파일 삭제
#             os.unlink(save_path)
            
#             return result
        
#         except Exception as e:
#             # 오류 처리
#             print("이미지 업로드 및 처리 중 오류 발생:", e)
#             return jsonify({'error': str(e)})  # 오류 메시지 반환
# #=========================================================================

# @detect_bp.route('/detect_upload', methods=['GET'])

# def detect_upload():
    
#     result = img_upload()  
#     if request.method == 'GET':
#         return jsonify(result)

#============================================================================
#============================================================================

# @detect_bp.route('/img_upload', methods=['POST'])
# def img_upload():
#     # 결과 이미지 로컬 변수로 초기화
#     result_image = None

#     if request.method == 'POST':
        
#         # 업로드 파일 가져오기
#         userimg = request.files['imgData']
#         print("이미지 업로드 성공")
        
#         # # 이미지를 바이트 형식으로 읽기
#         image_bytes = userimg.read()

#         # 이미지를 임시 파일로 저장
#         with tempfile.NamedTemporaryFile(delete=False) as temp_img:
#             temp_img.write(image_bytes)
#             temp_img_path = temp_img.name
            
#         # 바이트를 이미지로 디코딩
#         userimg = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)

#         # YOLO 모델 사용하여 객체 감지
#         # detected_img = cv2.imread(userimg)
#         result = model.predict(userimg)
#         print("detect 성공")
    
#         # 임시 파일 삭제
#         os.unlink(temp_img_path)
                
#         # 결과 이미지를 JPEG 형식으로 인코딩
#         _, imgEncoded = cv2.imencode('.jpg', userimg)
        
#         # 바이트 형식의 이미지를 base64로 인코딩하여 문자열로 변환
#         imgEncoded_base64 = base64.b64encode(imgEncoded).decode('utf-8')
        
#         return imgEncoded_base64


# @detect_bp.route('/detect_upload', methods=['POST'])
# def result_upload():
        
#     if request.method == 'POST':
        
#         # img_upload() 함수를 호출
#         # 결과 이미지와 인코딩된 이미지 데이터 받기
#         imgEncoded_base64 = img_upload()

#         # JSON 응답 생성
#         response = {'image_data': imgEncoded_base64}
        
#         return jsonify(response)