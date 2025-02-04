# iot-python-2025
Iot 개발자 기초 프로그래밍 언어 repository

## 1 일차
- 개발환경 설정 
    - 압축, 폰트, 개발용 에디터 설치
        - 반디집 설치(교육, 회사에 전무 무료)
        - 나눔글꼴 중 D2Coding. 추후 나눔고딕코딩 필요 
        - NotePad++  
    - Visual Studio Code 설치
        - 확장 Korean
        - Font Family D2Coding 추가, Mouse Wheel Zoom  체크 설정    

- 프로그래밍 언어 종류
    - 컴파일러(exe 파일 생성하는 언어)
        - C , C++, C#, Java, ...

    - 인터프리터(소스코드를 바로 실행, 실행파일 없음 )
        - 파이썬, JavaScript            
    - 컴파일러(exe 파일 생성하는 언어) vs 인터프리터(소스코드를 바로 실행)
        - 파이썬 -> 인터프리터 언어이다. 

- 파이썬 
    - 1990년에 개발한 인터프리터 언어
    - 네덜란드 개발자 귀도 반 로섬
    - 객체지향 프로그래밍 언어(Object Oriented Program)
    - 아주 쉽게 학습할 수 있는 언어

- 파이썬 개발환경 Pyenv
    - 파이썬 버전을 손쉽게 변경할 수 있는 툴 
    - 파워 셀 관리자모드로 오픈, 아래의 명령어 실행
        ```shell
        >Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
        ```

    - https://pyenv-win.github.io/pyenv-win/ Quick Start 1번 실행
    - pyenv 로 파이썬 버전 설치 및 전역설정 

- Visual Studio Code
    - Python 확장 설치
    - *.py 파일 생성 후 코딩
    - Ctrl + f5 실행


## 2일차
- 파이썬 기초 
    - 변수 
        - `데이터를` 담아서 여러군데에서 쓰기 위해 사용 

    - 자료형
        - None, int, float , double, String, boolean, list, tuple, dict, set,...    
        - type() 함수로 <class 'str'> => 확인가능

    - 입출력
      - 화면입출력 : 콘솔에서 입력하고 결과를 출력
        - input(), print()

    - 문자열 포맷팅 : 문자열을 좀 더 깔끔하게 표현
        - %s, %d, %f,...
        -{0}, {1}, {2}.format(), f('{2:5 + 1}')...  
    
    - 연산자
        - 사칙연산 : +, -, *, /, //, %, **, (,) 
        - 리스트연산 : list[0], list[0:3 +1]
        - 문자열연산 : split(), replace(), lstrip(), rstrip(), strip(), find(),...  

- 깃허브[Desktop] 
    1) **fetch origin** : 로컬의 변경사항을 리모트로 올리기
    2) pull : 리모트에 변경사항을 로컬로 내려받기
    3) commit : 로컬, 리모트에 변경사항을 확정
    4) push : 리모트에 변경사항을 로컬로 내려받기
    
    
## 3일차 
- 파이썬 기초
    - 흐름제어
    - 파일 입출력
    - 함수
    - 객체지향
    - 모듈, 패키지
    - 예외처리
    - 디버깅
  
