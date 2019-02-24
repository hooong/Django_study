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



# End



