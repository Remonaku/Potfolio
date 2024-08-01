from flask import Blueprint, render_template, request, redirect, url_for, session
from ultralytics import YOLO

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

# /upload_image 경로로 POST 요청 처리
@detect_bp.route("/upload_image", methods=["POST"])
# 사용자로부터 전송된 이미지 파일을 받아와서 저장하는 역할
def upload_image():    
    
    # POST 방식의 요청인지 확인하기
    if request.method == 'POST':
        # 업로드 이미지 파일 취득
        file = request.files['file']
        # 이미지 파일 저장 경로 설정
        upload_image_path = "static/user_img/upload_img/" + file.filename
        # 이미지 경로에 이미지 파일 저장     
        image = file.save(upload_image_path)
        
    
        # YOLO 모델 불러오기
        model = YOLO('models/best.pt')
        # 모델과 저장된 이미지 파일을 사용하여 Predict
        result_images = model.predict(source=upload_image_path)
        print("result : ", result_images)
        
        # 결과 이미지를 저장할 디렉토리 경로 설정
        save_dir = "static/user_img/detected_img/"

        # label list
        labels = ['abnormal', 'abnormal area']

        # 결과를 list에 저장
        result_image_paths = []
        result_count_paths = []
        result_area_count_paths = []
        result_score_paths = []
        result_grade_paths = []
        
        # count/score 초기화
        abnormal_count = 0
        abnormal_area_count = 0
        tooth_score = 100
        
        for i, image in enumerate(result_images):
            # 파일명에 순차적인 인덱스 추가
            result_image_path = save_dir + f"result_image_{i}.jpg"  
            image.save(result_image_path)
            
            print("result_img_path : ", result_image_path)
            
            # abnormal label
            if result_images[0].names[0] == labels[0] and result_images[0].names[1] == labels[1]:
                # 라벨 1, 0 리스트 출력하기
                box_count = result_images[0].boxes.cls.tolist()
                print(box_count)
                
                # abnormal count
                abnormal_label_count = sum(box_count)
                abnormal_count += abnormal_label_count
                print("abnormal_count : ", abnormal_count)
                
                # abnormal area count
                area_count = box_count.count(0.0)
                print("area_count : ", area_count)
                abnormal_area_count += area_count
            
                # abnormal 3점, abnormal_area 5점 > 치아 score
                tooth_score = tooth_score - ((abnormal_count * 3)+(abnormal_area_count * 5))
                print("tooth_score : ", tooth_score)
                
                # score에 따른 grade
                if tooth_score >= 90:
                    tooth_grade = "A"
                elif tooth_score < 90 and tooth_score >= 80:
                    tooth_grade = "B"
                elif tooth_score < 80 and tooth_score >= 70:
                    tooth_grade = "C"
                elif tooth_score < 70 and tooth_score >= 60:
                    tooth_grade = "D"
                elif tooth_score < 60 and tooth_score >= 40:
                    tooth_grade = "E"
                else:
                    tooth_grade = "F"
                print("tooth_grade : ", tooth_grade)
            
            # Path list에 추가 
            result_image_paths.append(result_image_path)
            result_count_paths.append(int(abnormal_count))
            result_area_count_paths.append(abnormal_area_count)
            result_score_paths.append(tooth_score)
            result_grade_paths.append(tooth_grade)
        
        print(result_image_paths)
        print(result_count_paths)
        print(result_area_count_paths)
        print(result_score_paths)
        print(result_grade_paths)

        # 결과 이미지 파일 경로 리스트 반환
        return redirect(url_for('detect.result', 
                                result_image_paths=result_image_paths,
                                result_count_paths=result_count_paths, 
                                result_area_count_paths=result_area_count_paths, 
                                result_score_paths=result_score_paths, 
                                result_grade_paths=result_grade_paths))

#=========================================================================

@detect_bp.route("/result")
def result():
    # URL 쿼리 문자열에서 매개변수 값 추출 > list 형태로 가져오기
    result_image_paths = request.args.getlist('result_image_paths')
    result_count_paths = request.args.getlist('result_count_paths')
    result_area_count_paths = request.args.getlist('result_area_count_paths')
    result_score_paths = request.args.getlist('result_score_paths')
    result_grade_paths = request.args.getlist('result_grade_paths')
    
    print("result_image_path : ", result_image_paths)
    print("result_count_path : ", result_count_paths)
    print("result_area_count_path : ", result_area_count_paths)
    print("result_score_path : ", result_score_paths)
    print("result_grade_path : ", result_grade_paths)
    
    # result 페이지로 이동
    return render_template('result.html', result_image_paths=result_image_paths, 
                            result_count_paths=result_count_paths, 
                            result_area_count_paths=result_area_count_paths, 
                            result_score_paths=result_score_paths, 
                            result_grade_paths=result_grade_paths)
