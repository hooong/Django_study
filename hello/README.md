# Hello world 띄워보기

1. 가상환경을 실행



   `$ source myvenv/Script/activate `

2. django 프로젝트를 생성하기



   `$ django-admin startproject <프로젝트 이름>`



   - 위의 명령어를 실행해주면 아래와 같은 프로젝트 폴더가 생긴다.

   ```c
   <프로젝트 이름>/		//<프로젝트 이름>폴더에 같은 이름의 폴더가 생기므로 상위 폴더의 이름을 바꿔주는 것이 좋다.
       manage.py
       <프로젝트 이름>/
       	__init__.py
       	settings.py
       	urls.py
       	wsgi.py
   ```



3. django 서버 작동시키기



   `$cd <프로젝트 이름> `

   - 프로젝트가 만들어진 폴더로 이동해준다.


   `$ python manage.py runserver`

   - 서버가 성공적으로 작동하면 http://127.0.0.1:8000/의 주소로 서버가 작동하기 시작한다.

   - 서버를 끄려면 `ctrl` + `c`를 누르면 된다.

4. app만들기

   - django에서 app이란 프로젝트의 구성단위로 app이 모여 하나의 프로젝트를 구성한다고 생각하면 쉽다.


   `$ python manage.py startapp hello`



   - app을 만들면 hello라는 폴더가 생긴다.

   ```c
   hello/
       templates	//html파일들을 담을 폴더로 생성을 해준다.
       migrations
       __init.py
       admin.py
       apps.py
       models.py
       tests.py
       views.py
   ```



   1. settings.py를 통해 프로젝트에 app존재를 알리기



      - <프로젝트 이름>/settings.py를 열어준다.

      - `hello.apps.HelloConfig`를 추가해준다.

      ```python
      INSTALLED_APPS = [
          'hello.apps.HelloConfig',	//이 부분을 추가해준다.
          'django.contrib.admin',
          'django.contrib.auth',
          ...
          'django.contrib.staticfiles',
      ]
      ```

      - hello폴더 안의 apps.py파일 안에는 HelloConfig라는 클래스가 정의되어있다.

   2. template만들기



      - app폴더 안에 template폴더를 생성해준다.

      - template폴더 안에는 페이지에 보여줄 home.html파일을 생성해준다.

      ```html
      <h1>
          Hello World!
      </h1>
      ```

   3. views.py에 함수 만들기



      ```python
      from django.shortcuts import render
      ...
      def home(request):
          return render(request, 'home.html')
      
      ```

      - 요청이 들어오면 `home.html`을 열어주라는 home이라는 함수를 정의해준다.

   4. urls.py를 통해 views와 요청을 연결해준다.



      - urls.py파일을 연 후 아래와 같이 `import hello.views`와 `path('', hello.views.home, name='home'),`를 추가해준다.

      ```python
      from django.contrib import admin
      from django.urls import path
      import hello.views
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('', hello.views.home, name='home'),
      ]
      ```



      - path의 인자 

        - 첫번째는 route인데 쉽게 말해 도메인 뒤에 붙는 url이라 보면 된다.

          - 예를 들어 `admin/`이면 `http://127.0.0.1:8000/admin/`을 의미한다.

        - 두번째로는 views안에 정의된 함수이다.

        - 세번째는 path의 이름을 `home`로 하겠다는 의미이다.

5. 웹사이트에서 확인해보기

   - 웹브라우저에서 `http://127.0.0.1:8000/`으로 접속을 해보면 `hello.html`의 내용이 브라우저에 나타날 것이다.



#END