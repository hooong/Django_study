# Social로그인

>- 기존 login방식 : db와 db를 다루는 로직이 한 공간에 있다.
>
>- social계정 login방식 : db와 db를 다루는 로직이 다른 공간에 있다.(구글이나 페이스북서버에서 토큰을 주고받으며 request를 받아온다.)



### 구글 로그인



1. `$ pip install allauth` 

   > `allauth`는 소셜로그인기능을 관리해주는 패키지이다.



2. `urls.py` 수정

   ```python
   from django.urls import path, include
   from login import views
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', views.home, name='home'),
       path('accounts/', include('allauth.urls')),
   ]
   ```



3. `settings.py` 수정

   - INSTALLED_APPS 추가

   ```python
   INSTALLED_APPS = [
       'django.contrib.sites',     # allauth 사용을 위해 
   
       # allauth
       'allauth',
       'allauth.account',
       'allauth.socialaccount',
   
       # provider 구글,페이스북,카톡,깃헙
       'allauth.socialaccount.providers.google',
       'allauth.socialaccount.providers.facebook',
   ]
   ```

   - 아래 내용 추가

   ```python
   AUTHENTICATION_BACKENDS = (
   
       #
       'django.contrib.auth.backends.ModelBackend',
   
       #
       'allauth.account.auth_backends.AuthenticationBackend',
   )
   
   SITE_ID = 1
   
   LOGIN_REDIRECT_URL = '/'        #로그인시 리다이렉트 되는 url
   ```



4. 템플릿 수정

   ```html
   {% load socialaccount %}
   {% providers_media_js %}        <!--provider에서 제공하는 로그인페이지의 템플릿을 사용할 수 있다.-->
   
   <h1>hello world!</h1>
   
   <a href="/accounts/signup">회원가입</a>
   
   {% if user.is_authenticated %}
   <a href="/accounts/logout">로그아웃</a>
   {{user.username}} 님이 로그인 중
   {% else %}
   <a href=" {% provider_login_url 'google' %}">구글 로그인</a>
   로그인 해야됨
   {% endif %}
   ```



5. admin페이지에서 `sites` 에서 site를 추가
   - Domain name : 127.0.0.1:8000
   - Display name : 127.0.0.1:8000



6. `Social Accounts -> Social Application` 에 추가
   - [구글 API](console.developers.google.com)에서 새 프로젝트를 만든다
   - 사용자인증정보 메뉴로 들어간다
   - 사용자인증정보 만들기에서 `OAuth 클라이언트 ID`를 만들고 웹애플리케이션을 선택(선택이 안되면 위의 동의 화면으로 가서 애플리케이션 이름을 써주고 저장한다.)
   - 웹애플리케이션을 선택하면 밑에 `승인된 자바스크립트 원본` 와 `승인된 리디렉션 URI`  이 뜨는데 로컬이므로 둘 다 `http://127.0.0.1:8000`으로 채워준다.
   - 그렇게 되면 클라이언트 ID와 클라이언트 보안비밀이 나오는데 이것을 Social Application에 추가할때 채워 넣어준다.
7. 만약 400에러가 뜬다면 웹클라이언트 설정에 들어가서 `승인된 리디렉션 URI`에 오류페이지에 뜨는 url을 채워서 설정해준다.



# API

> API(Application Programming Interface) : 응용프로그램(우리의 프로젝트)에서 사용할 수 있도록, 운영체제나 프로그래밍 언어가 제공하는 기능(끌어다 쓰고 싶은 기능)을 제어할 수 있는 인터페이스(쉽게말해 다리)를 뜻한다.



### 네이버 지도 API

> 특정 지점의 위치 명시해보기

1. ncloud.com 회원가입, 결제수단등록
2. 서비스에서 maps검색 이용신청하기
3. application 등록
4. 애플리케이션 이름을 입력 후 maps에서 web dynamic map을 체크
5. web서비스 url에  http://127.0.0.1:8000 추가
6. 인증정보에서 클라이언트id와 클라이언트secret확인가능
7. 서비스구분에서 web dynamic map옆의 버튼 클릭해서 설명서 페이지의 web dynamic map v3사이트 바로가기 클릭
8. 시작하기 누르면 예시코드들이 나온다.
9. example에 가면 활용코드들도 많다.



------

### js를 static으로 사용하기

<script type="text/javascript" src="{% static 'js/basic.js' %}"></script>



## Thumbnail

> Thumbnail이란 이미지들을 대표하는 대표이미지를 말한다.
>
> 썸네일을 사용하면 파일지정에 용이하고 용량관리(확장자, 압축방식을 지정가능)에 좋고 파일 분류에 효율적으로 가능해진다.

1. 일단 썸네일을 만들기 위해서 Pictures라는 모델을 하나 만들어준다.

   1. `models.py` 에 `Pictures` 클래스를 추가해준다.

      ```python
      class Pictures(models.Model):
          text  = models.TextField()
          image = models.ImageField(upload_to = "pic")
      ```

   2. media파일을 사용할 것이기 때문에 `settings.py`에 아래 내용 추가

      ```python
      MEDIA_URL = '/media/'
      MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
      ```

   3. media파일을 사용하기 위해 `urls.py`에 아래 내용 추가

      ```python
      from django.conf import settings
      from django.conf.urls.static import static
      
      urlpatterns = [
          ...
      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
      
      ```

   4. `admin.py`에 `Pictures` 등록해준다.

      ```python
      from .models import Pictures
      
      admin.site.register(Pictures)
      ```

   5. `views.py` 함수 수정

      ```python
      from .models import Pictures
      
      def home(request):
          blog = Pictures.objects
          return render(request, 'home.html', {'blog':blog})
      ```

   6. `home.html`에 이미지를 띄워주는 코드 추가

      ```html
      {% for blog in blog.all %}
      
          <img src="{{blog.image.url}}" width=500>
          <br>
          {{blog.text}}
       
      {% endfor %}
      ```

   7. `admin` 페이지에 가서 `Pictures` 객체 하나를 생성해준다.(사진 하나를 업로드해준다.)

      

2. Thumbnail을 처리해주는 패키지인 `django-imagekit`설치

   `$ pip install pillow django-imagekit`

   - `settings.py`의 `installed app`에 `'imagekit'` 을 추가해준다.

   

3. `models.py` 에 필요한 것들을 import해주기

   ```python
   from imagekit.models import ImageSpecField      # 이 함수로서 썸네일을 만들어냄
   from imagekit.processors import ResizeToFill    # 크기조정을 쉽게 해주는 기능
   ```

   

4. `Pictures`클래스에 썸네일 변수를 정의해주기

   ```python
   class Pictures(models.Model):
       text  = models.TextField()
       image = models.ImageField(upload_to = "pic")
       image_thumbnail = ImageSpecField(source = 'image', processors=[ResizeToFill(120,60)], format='JPEG', options={'quality':60})      # 이미지파일을 지정(source)해서 썸네일을 만들어준다. processors는 사이즈를 지정.
   ```

   - 속성값 :  format(확장자 지정), options(압축방식)

     

5. `home.html` 에 썸네일 띄워주는 코드 추가하기

   ```html
   <img src="{{blog.image_thumbnail.url}}">
   ```



## app 재사용하기

> 재사용 할 app을 패키징을 해서 다시 사용할 수 있다.
>
> - 패키지란 쉽게 재사용하기 위해 연관된 python코드를 묶어 놓은 것으로 module이라고도 한다.

- 패키징하기

  1. 원래 프로젝트 밖에 폴더를 하나 만들고 패키징 할 app을 넣어준다.

     - 여기에서는 `project` 라는 이름으로 폴더를 만들고 넣어주었다.

  2. 패키징을 하기 위해서는 4가지의 파일이 필요하다.

     - README.rst : 사용설명서와 기능설명서
     - LICENSE : 배포될때 문제이므로 로컬에서는 상관이 없지만 라이센스 없이 공개된 코드는 쓸모없다는 것을 알아두면 된다.
     - setup.py : app을 빌드하고 설치하는 방법에 대한 세부사항을 제공하는 파일
     - MANIFEST.in : 파이썬 파일이 아닌 파일들을 포함시키기 위한 파일

  3. `README.rst` 만들기

     ```rst
     =====
     login
     =====
     
     Polls is a simple Django app to conduct Web-based polls. For each
     question, visitors can choose between a fixed number of answers.
     
     Detailed documentation is in the "docs" directory.
     
     Quick start
     -----------
     
     1. Add "polls" to your INSTALLED_APPS setting like this::
     
         INSTALLED_APPS = [
             ...
             'login',
         ]
     
     2. Include the polls URLconf in your project urls.py like this::
     
         path('polls/', include('polls.urls')),
     
     3. Run `python manage.py migrate` to create the polls models.
     
     4. Start the development server and visit http://127.0.0.1:8000/admin/
        to create a poll (you'll need the Admin app enabled).
     
     5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
     ```

     위와 같이 설명서를 만들어주면 된다.

  4. `LICENSE` 파일 만들기

     ```
     Copyright (c) 2019, login
     All rights reserved.
     
     Redistribution and use in source and binary forms, with or without modification,
     are permitted provided that the following conditions are met:
     
         1. Redistributions of source code must retain the above copyright notice,
            this list of conditions and the following disclaimer.
     
         2. Redistributions in binary form must reproduce the above copyright
            notice, this list of conditions and the following disclaimer in the
            documentation and/or other materials provided with the distribution.
     
         3. Neither the name of Django nor the names of its contributors may be used
            to endorse or promote products derived from this software without
            specific prior written permission.
     
     THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
     ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
     WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
     DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
     ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
     (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
     LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
     ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
     (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
     SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
     ```

     이런식으로 써주지만 로컬에서는 상관이 없다. 만들어주는 습관만이라도 길러보자!

  5. `setup.py` 파일 만들기

     ```python
     import os
     from setuptools import find_packages, setup
     with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
         README = readme.read()
     # allow setup.py to be run from any path
     os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
     setup(
         name='login',
         version='0.1',
         packages=find_packages(),
         include_package_data=True,
         license='BSD License',  # example license
         description='login',
         long_description=README,
         url='https://www.example.com/',
         author='Your Name',
         author_email='yourname@example.com',
         classifiers=[
             'Environment :: Web Environment',
             'Framework :: Django',
             'Framework :: Django :: X.Y',  # replace "X.Y" as appropriate
             'Intended Audience :: Developers',
             'License :: OSI Approved :: BSD License',  # example license
             'Operating System :: OS Independent',
             'Programming Language :: Python',
             'Programming Language :: Python :: 3.5',
             'Programming Language :: Python :: 3.6',
             'Topic :: Internet :: WWW/HTTP',
             'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
         ],
     )
     ```

     위의 내용을 복붙해준다.

  6. `MANIFEST.in` 파일 만들기

     ```in
     include LICENSE
     include README.rst
     recursive-include login/templates *
     ```

  7. 패키지를 빌드하기

     `$ python setup.py sdist`

     - 위의 명령어를 실행하되 패키징하려는 폴더로 가서 입력을 해준다.
     - 명령어를 실행해주면 프로젝트 폴더 안에 `dist`라는 폴더가 생기고 그 안에 `~.tar.gz` 와 같은 파일이 생길 것이다. 이것이 바로 패키지이다.



- 패키징한 패키지를 사용하기

  - 패키지를 사용하려면 패키지가 있는 폴더의 위치에서 다음 명령어를 실행해준다.

    `$ pip install dist/login.tar.gz`

  - 그 다음 원래의 프로젝트 폴더로 위치를 옮기고 서버를 켜주면 패키지가 같은 폴더에 있지않은데도 정상 작동하는 것을 확인 할 수 있다.



# End



