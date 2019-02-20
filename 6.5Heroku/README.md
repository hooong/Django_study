# Heroku를 이용한 배포하기

>  배포란 만든 애플리케이션을 인터넷 즉, 서버에 올려서 다른 사람들도 보고 사용할 수 있게끔 해주는 것을 말한다.
>
> `runserver` 로는 로컬에서만 접속이 가능하다. 하지만 Heroku, aws, pythonanywhere등 다양한 웹 호스팅 서버를 이용해야한다. 



1. Heroku 설치하기

   - [heroku.com](https://heroku.com) 으로 들어가서 sign up을 하고 , 로그인을 한다.

   - [heroku 다운](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)에서 heroku를 설치한다.

   

2. github repo에 프로젝트폴더(manage.py를 포함하는 폴더를 말한다.)를 `push`한다.

   > github에 올릴때에는 `.gitignore`를 사용해준다.

   

----



3. `settings.py` 수정

   >DEBUG기능은 개발시에 페이지가 없다거나 url이 잘못되었다거나를 알려주는 것인데 배포할때에는 이 기능을 꺼주어야한다.
   >
   >SECRET_KEY는 보안을 위해서 사용되는 랜덤값이므로 이것을 공개해버리면 암호화가 무용지물이 된다.
   >
   >ALLOWED_HOSTS는 허용되는 호스트주소인데 모두 허용해준다.

   ```python
   # SECRET_KEY = <KEY>
   SECRET_KEY = os.environ.get('DJANO_SECRET_KEY',<KEY>)
   
   # DEBUG = True
   DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))	#False로 바꾸면 꺼줄 수 있다. 뒤에 오류가 날 수도 있으므로 일단은 True로 둔다.
   
   ALLOWED_HOSTS = ['*']		#이 부분을 찾아서 '*'를 넣어준다.
   ```

   

4. `Procfile` 작성

   >이 파일은 manage.py가 있는 최상위 폴더에 만들며 확장자는 따로 없다. `Procfile` 이라는 파일을 생성한다.

   ```python
   web: gunicorn <project이름>.wsgi --log-file -	#<project이름>에는 project이름(처음 django startproject 할때 적었던 이름)을 넣어주면 된다.
   ```

   - Procfile은 애플리케이션을 Heorku에 배포 해서 실행할때, Heroku 클라우드가 맨 처음 실행하는 명령어를 지정하는 파일이다. 보통 애플리케이션을 기동하기 위한 명령어를 기술한다. 여기서 `web:` 은 웹 애플리케이션임을 정의하는 것이다.

   

5. gunicon 설치하기

   > `gunicorn`은 장고서버를 관리하는 툴이다. 데몬으로 구동하고 워커를 생성하는 기능이 있다고 한다.(추후 공부)

   

   - `$ pip install gunicorn`으로 설치를 해준다.

   

6. Database 설정하기

   >heroku에서는 sqlite를 사용할 수 없다고 한다. 그래서 다른 db를 사용해야한다.

   

   - `$ pip install dj-database-url`

   - `$ pip install psycopg2-binary`

   두 개를 설치해주고 `settings.py`에 아래 내용을 붙여넣는다.

   ```python
   # Heroku: Update database configuration from $DATABASE_URL.
   import dj_database_url
   db_from_env = dj_database_url.config(conn_max_age=500)
   DATABASES['default'].update(db_from_env)
   ```

   

7. static file을 위한 설정

   - `$ pip install whitenoise`

     >static파일들을 collectstatics 명령수행시 지정경로에 파일들을 모아주는 역할을 한다.

   `whitenoise` 를 설치해주고 `settings.py` 를 아래처럼 `whitenoise....` 이 부분을 추가해준다.

   ```python
   MIDDLEWARE = [
       'whitenoise.middleware.WhiteNoiseMiddleware',		#이 부분 추가
       'django.middleware.security.SecurityMiddleware',
       'django.contrib.sessions.middleware.SessionMiddleware',
       'django.middleware.common.CommonMiddleware',
       'django.middleware.csrf.CsrfViewMiddleware',
       'django.contrib.auth.middleware.AuthenticationMiddleware',
       'django.contrib.messages.middleware.MessageMiddleware',
       'django.middleware.clickjacking.XFrameOptionsMiddleware',
   ]
   ```

   

8. python관련 라이브러리 설치

   - `$ pip freeze > requirements.txt`

     - 여러가지 설치한 내용들을 호스팅할 서버에서도 설치해야하므로 관련 목록 리스트업을 해주는 것이다.

     

9. heroku에게 python 버전 명시하기

   - `runtime.txt` 라는 파일을 최상위 폴더(manage.py가 있는)에 만들고 밑의 내용을 넣어준다.

   - ```txt
     python-3.7.2
     ```

     >python의 버전 확인 방법은 `$ python3 --version`이다.

     

10. github에 다시 push를 해준다.

    

11. Heroku app 만들기

    - `$ heroku login` 
      - 입력하고 `q` 를 제외한 아무키나 누르면 로그인 웹브라우저 창이 뜬다. 그럼 로그인해준다.
    - `$ heroku create` 
      - 자동으로 app을 생성해준다. remote도 해준다.
    - `$ git push heroku master` 
      - heroku로 push가 된다.
    - `$ heroku run python manage.py migrate` 
      - migrate를 해준다.
    - `$ heroku run python manage.py createsuperuser`
      - db가 바뀌었으므로 superuser도 새로 만들어주어야 한다.
    - `$ heroku open`
      - 배포된 홈페이지가 나온다.



# End

