#django 기본환경 셋팅하기

- pip패키지 : Python으로 작성된 패키지 소프트웨어를 설치 및 관리하는 패키지 관리 시스템
  - Django == pip패키지
- **가상환경**
  - 가상환경이란 프로젝트를 담을 독립된 공간이라 할 수 있다.
  - 가상환경 생성
    - python -m venv <가상환경이름>
  - 가상환경 실행
    - source <가상환경이름>/Scripts/activate
    - 나 같은경우에는 source <가상환경이름>/bin/activate로 실행이 됨.
  - 가상환경 종료
    - deactivate
  - django 설치하기
    - pip install django (가상환경이 실행된 상태에서)
    - pip install django==<version> (특정버전을 설치하는 방법)
    - pip uninstall django (지우기 명령어)