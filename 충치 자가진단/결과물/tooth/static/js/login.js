// 회원가입 폼


const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

if (signUpButton) {
	signUpButton.addEventListener('click', () => {
		container.classList.add("right-panel-active");
	});
} else {
	console.error('signup을 찾을 수 없다.')
}

if (signInButton){
	signInButton.addEventListener('click', () => {
		container.classList.remove("right-panel-active");
	});
}else {
	console.error('signin을 찾을 수 없다.')
}

//회원가입 폼
const firstSignUp = document.getElementById('firstSignUp');
const secondSignUp = document.getElementById('secondSignUp');
const nextBtn = document.getElementById('nextBtn');
const signUpBtn = document.getElementById('signUpBtn');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

var idcheck = 0;

// 이메일 도메인 박스
// const domainListElement = document.querySelector('.domain')
// const domainInputElement = document.querySelector('#domainText')

// // select 옵션 변경 시
// domainListElement.addEventListener('change', (e) => {
// 	// option에 있는 도메인
// 	if(e.target.value !== "type") {
// 		// 선택 도메인을 input에 입력하고 disabled
// 		domainInputElement.value = e.target.value
// 		domainInputElement.disabled = true
// 	} else {
// 		// 직접 입력 시 내용 초기화 및 변경 가능
// 		domainInputElement.value = ''
// 		domainInputElement.disabled = false
// 	}
// })

// // 도메인 선택 시 onchange 이벤트 핸들러 설정
// function domainChange() {
// 	// domainList 요소 가져오기
// 	var selectDomain = document.getElementById('domainList');
// 	// 선택 옵션 값 가져오기
// 	var selectValue = selectDomain.options[selectDomain.selectedIndex].value;
// 	// 선택 도메인 가져오기
// 	var selectText = selectDomain.options[selectDomain.selectedIndex].text;

// 	// 선택값이 type이면 입력란 활성화 아니면 비활성화
// 	if(selectValue === "type") {
// 		document.getElementById('domain').disabled = false;
// 		document.getElementById('domain').value = "";
// 	} else {
// 		document.getElementById('domain').disabled = true;
// 		document.getElementById('domain').value = selectText;
// 	}

// }

function updateInput() {
    var selectBox = document.getElementById("domainList");
    var inputBox = document.getElementById("domainInput");
    var selectedValue = selectBox.value;
    if (selectedValue !== "type") {
        inputBox.value = selectedValue;
    } else {
        inputBox.value = "";
    }
}


// 중복체크 버튼 클릭 이벤트 : 아이디 중복체크 하는 api호출 
	// 이름란에 쓴 값(value) 가지고와서 그걸 아이디 중복체크 하는 api 파라미터로 넘기기
	// true false로 받아와
	// idcheck 로 아이디 중복체크 하는 api 리턴값을 넣는다.

function idCheck() {
	// 입력된 email 값 가져오기
	var user_id = document.getElementsByName('user_id')[0].value;
	var domain = document.getElementsByName('domain')[0].value;
	var id_en_num = /^[a-zA-Z0-9]+$/;
	var email = user_id + "@" + domain;

		// 이메일 입력 여부 확인
		if (user_id.trim() === '' && domain.trim() === '') {
			alert('이메일을 입력해주세요.');
			return; 
			// 이메일이 입력되지 않았으면 함수를 종료하고 
			//더 이상 실행하지 않음
		}

		if (!id_en_num.test(user_id)) {
			alert("아이디는 영문자와 숫자로만 입력해주세요.");
			return;
		}
	

		// XMLHttpRequest 객체 생성
		// 비동기적으로 서버와 상호작용하기 위해 사용
		// 비동기적 : 동시에 일어나지 않는다.
		// 요청을 했을 때 바로 그자리에서 결과가 주어지지 않는다.
		// 동기 방식은 해당 업무를 쭉 나아가면서 지나가는 반면
		// 비동기는 원래 가는 방식대로 가되, 원할때마다 나오게 할 수 있다.
		var xhr = new XMLHttpRequest();

		// 서버로 요청 보내기
		// .open(http 메소드, 요청을 보낼 url 비동기적으로 처리할 지 여부)
		xhr.open('GET', '/check_id?email=' + email, true);

		// 상태 변화 감지하고 처리
		// onreadystatechange 말 그대로 객체의 상태가 변하면 호출되는 이벤트 핸들러
		// xhr.readyState === 4 : 요청의 상태가 완료되었다.
		// xhr.status === 200 : 서버로부터 성공적인 응답을 받았다.
		// 요청에 성공한다면, 서버로부터 받은 JSON 형식의 응답을 파싱하여
		// 해당 응답에 따라 알림을 사용자에게 표시
		xhr.onreadystatechange = function() {
			if (xhr.readyState === 4 && xhr.status === 200) {
				var response = JSON.parse(xhr.responseText);
				if (response.exists) {
					alert('이미 가입된 이메일입니다.');
				} else {
					alert('사용 가능한 이메일입니다.');
					idcheck = 1;
				}
			}
		};
		// 서버에 요청 보내기
		xhr.send();
}

// Enter 키 눌렀을 때 keydown 이벤트 핸들링
document.addEventListener("keydown", function (event) {
    if (firstSignUp.style.display !== "none") {
        // 만약 현재 키가 Enter 키인지 확인
        if (event.key === "Enter") {
            // 만약 현재 active element가 password 또는 email 입력란인 경우
            if (document.activeElement === password || document.activeElement === document.getElementsByName('user_id')[0] || document.activeElement === document.getElementsByName(
                'domain'
            )[0]) {
                // 만약 active element가 password이고 비밀번호가 4자 이하인 경우
                if (document.activeElement === password && password.value.length <= 12) {
                    // 비밀번호가 12자 이하임을 알리는 에러 메시지를 표시
                    alert("비밀번호를 12자 이상 입력해주세요.")
					// 만약 active element가 email이고 값이 비어 있는 경우);
                } else if (document.activeElement === document.getElementsByName('user_id')[0] && document.getElementsByName(
                    'user_id'
                )[0].value === '' || document.activeElement === document.getElementsByName(
                    'domain'
                )[0] && document.getElementsByName('domain')[0].value === '') {
                    // 이메일을 입력하라는 에러 메시지를 표시
                    alert("이메일을 입력해주세요.");
                }
                // 이벤트의 기본 동작을 중지하여 폼이 제출되지 않도록 함
                event.preventDefault();
            } else {
                // firstSignUp를 숨김 firstSignUp.style.display = "none"; 이벤트의 기본 동작을 중지하여 폼이 제출되지
                // 않도록 함
                event.preventDefault();
                // secondSignUp를 나타나게 함 secondSignUp.style.display = "block";
            }
        }
    }
})


// 회원가입시 처음 입력란의 next버튼 클릭이벤트
nextBtn.addEventListener('click', () => {

	// 아이디 중복체크 validation
	if(idcheck != 1){
		alert("아이디 중복체크를 해주세요.");
		return;
	}

	// 비밀번호 길이 validation
	if(password.value.length < 12){
		alert("비밀번호 12자 이상 입력해주세요.");
		return;
	}
	
	// 비밀번호 동일 validation
	if(password.value != password2.value){
		alert("비밀번호를 확인해주세요.");
		return;
	}

	// firstSignUp를 숨김
	firstSignUp.style.display = "none";

	// secondSignUp를 나타나게 함
	secondSignUp.style.display = "block";
});

function validateForm(){
	// 이름
	var username = document.getElementsByName("username")[0].value;
	var id_korean = /^[a-zA-Z가-힣]+$/;
	if (!id_korean.test(username)) {
		alert("이름은 한글,영어로만 입력해주세요.");
		return false;
	}

	// 번호
	var phone = document.getElementsByName("phone")[0].value;
	var phone_regex = /^\d{3}-\d{4}-\d{4}$/;
	if (!phone_regex.test(phone)) {
		alert("올바른 핸드폰 번호 형식이 아닙니다. 예시: 010-1234-5678");
		return false;
	}
	
	return true;
}



function execDaumAdres(){
	new daum.Postcode({
		oncomplete: function(data) {
			// 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

			// 각 주소의 노출 규칙에 따라 주소를 조합한다.
			// 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
			var addr = ''; // 주소 변수
			var extraAddr = ''; // 참고항목 변수

			//사용자가 선택한 주소 타입에 따라 해당 주소 값을 가져온다.
			if (data.userSelectedType === 'R') { // 사용자가 도로명 주소를 선택했을 경우
				addr = data.roadAddress;
			} else { // 사용자가 지번 주소를 선택했을 경우(J)
				addr = data.jibunAddress;
			}

			// 사용자가 선택한 주소가 도로명 타입일때 참고항목을 조합한다.
			if(data.userSelectedType === 'R'){
				// 법정동명이 있을 경우 추가한다. (법정리는 제외)
				// 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
				if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
					extraAddr += data.bname;
				}
				// 건물명이 있고, 공동주택일 경우 추가한다.
				if(data.buildingName !== '' && data.apartment === 'Y'){
					extraAddr += (extraAddr !== '' ? ', ' + data.buildingName : data.buildingName);
				}
				// 표시할 참고항목이 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
				if(extraAddr !== ''){
					extraAddr = ' (' + extraAddr + ')';
				}
				// 조합된 참고항목을 해당 필드에 넣는다.
				document.getElementById("adres2").value = extraAddr;
			
			} else {
				document.getElementById("adres2").value = '';
			}

			// 우편번호와 주소 정보를 해당 필드에 넣는다.
			document.getElementById("adres1").value = addr;
			// 커서를 상세주소 필드로 이동한다.
			document.getElementById("adres2").focus();
		}
	}).open();
}

