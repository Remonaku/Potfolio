
// const resultImage = document.getElementById('resultImage');
// const resultMessage = document.getElementById('resultMessage');

//========================================================================

const form = document.querySelector('.bannertextbox form');
const imageContainer = document.getElementById('imageContainer');
const beforeupload = document.getElementById('beforeupload');
const fileupload = document.getElementById('file');

fileupload.addEventListener('change', function(event) {
    var file = event.target.files[0]; // 업로드한 파일을 가져옴
    var reader = new FileReader(); // FileReader 객체 생성

    reader.onload = function(event) {
        var imageUrl = event.target.result; // 이미지의 데이터 URL을 가져옴
        document.getElementById('upload_image').src = imageUrl; // 이미지의 URL을 img 요소의 src 속성에 할당
        imageContainer.style.display = 'block'; // 이미지를 보여주는 컨테이너를 표시
    };

    reader.readAsDataURL(file); // 파일을 읽어 데이터 URL로 변환
});




// 파일 업로드를 위한 input 요소가 변경되었을 때 이벤트 처리
// document.getElementById('fileUpload').addEventListener('change', async (event) => {
//     const file = event.target.files[0]; // 업로드된 파일 가져오기
//     const formData = new FormData();
//     formData.append('file', file);

//     // POST 요청을 보냄
//     const response = await fetch('/detect/upload', {
//         method: 'POST',
//         body: formData
//     });

//     const result = await response.json();
//     console.log(result); // 감지 결과 확인
// });

//========================================================================

// // 파일 업로드를 위한 input 요소가 변경되었을 때 이벤트 처리
// fileupload.addEventListener('change', () => {

//    // beforeupload를 숨김
//     beforeupload.style.display = "none";

//     // 선택한 파일을 가져와서 이미지 표시
//     const file = fileupload.files[0];
//     const reader = new FileReader();

//     reader.onload = function(e) {
//         // 이미지가 로드되면 imageContainer에 추가
//         const img = document.createElement('img');
//         img.src = e.target.result;
//         imageContainer.appendChild(img);

//         const resimg = document.createElement('img');
//         resimg.src = e.target.result;
//         resultImage.appendChild(resimg);
//     };
//     // 파일을 읽어오도록 요청
//     reader.readAsDataURL(file);

//     // 결과 메시지를 숨김
//     resultMessage.style.display = "none";

//    // 나타나게 함
//     imageContainer.style.display = "block";

//     // 결과 이미지를 보여줌
//     resultImage.style.display = "block";
    
// });

// 폼 제출 이벤트 처리
// form.addEventListener('submit', async (e) => {
//     e.preventDefault(); // 폼의 기본 동작(새로고침) 방지

//     const formData = new FormData(form); // FormData 생성

//     // 파일 업로드 처리
//     const response = await fetch('/upload', {
//         method: 'POST',
//         body: formData
//     });

//     const data = await response.json(); 
//     // 업로드된 파일의 정보를 JSON 형식으로 받음

//     // 업로드된 파일의 경로를 이용하여 이미지 표시
//     const img = document.createElement('img');
//     img.src = data.filePath;
//     imageContainer.appendChild(img);

//     // 업로드된 파일의 경로를 이용하여 결과 이미지 표시
//     const resimg = document.createElement('img');
//     resimg.src = data.filePath;
//     resultImage.appendChild(resimg);

// });

//========================================================================