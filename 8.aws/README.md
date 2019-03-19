# aws(elasticbeanstalk) 배포하기

- `$ pip install awsebcli --upgrade --user` 

- 프로젝트를 github에 올려주기

- 의존성 파일 만들기

  - manage.py가 있는 폴더에 `requirements.txt` 만들어주기

  - `.ebextensions`폴더 만들고 그 안에 `django.config` 파일 만들기

  - `django.config` 에 다음 내용 써주기

    ```config
    option_settings:
        aws:elasticbeanstalk:container:python:
            WSGIPath: firstproject/wsgi.py
    ```

    - WSGIPath 는 `wsgi.py` 가 있는 폴더를 찾아서 경로를 작성해준다.





