# Blog project

- bootstrap에서 `navbar`, `card title` 등등 적용

- 글 내용 100글자만 뜨게 하고 `...more`버튼 추가
- 글쓰기 페이지 추가
- 포트폴리오 페이지 추가
- static, media 파일 다루기



### 글쓰기 페이지 만들기

1. navbar에 글쓰기버튼 만들기

   - `new.html`로 연결

   - `path('blog/new', blog.views.new, name='new'),` 을 `urls.py`에 추가

   - `view.py`에 `new` 함수 추가

   - ```python
     def new(request):
         return render(request, 'new.html')
     ```

2. `views.py`에 `create` 함수 추가

   1. ```python
      from django.shortcuts import render, get_object_or_404, redirect
      from django.utils import timezone
      
      def create(request):
          blog = Blog()							#새로운 Blog객체를 하나 생성
          blog.title = request.GET['title']		#form에서 넘어온 데이터를 blog객체에 저장
          blog.body = request.GET['body'] 
          blog.pub_date = timezone.datetime.now()	#현재 시간을 저장
          blog.save()								#blog라는 객체를 DB에 저장
          return redirect('/blog/'+str(blog.id)) 	#blog.id는 int형으로 받으므로 str로 형변환
      ```

      - new페이지에서 입력받은 내용을 DB에 넣어주는 함수이다.
      - `redirect`는 `redirect(URL)`의 형식으로 URL로 이동하라는 뜻이다.
      - `redirect` 를 쓰기위해서 `from django.shortcuts import  redirect`추가
      - `timezone` 을 쓰기위해서 `from django.utils import timezone`추가

   - `render` 와 `reirect` 는 인자에 따라 쓰임이 나뉜다.
   - `recirect` 는 URL을 인자로 받음으로 다른 사이트로도 이동을 할 수 있다.
   - `render` 는 데이터를 담아서 처리하고 싶을 때 사용을 할 수 있다.

3. `urls.py`에 path추가

   - `path('blog/create', blog.views.create, name="create"),`

     > `path('어떤 url이 들어오면', (어디에있는)어떤 함수를 실행시켜라)`
     >
     > path는 위와 같은 형식으로 꼭 어느 페이지로 이동하는 것이 아닌 함수를 실행시키라는 의미이다.

4. `new.html` 작성

   - ```html
     <form action="{%url 'create'%}">
         <h4>제목: </h4>
         <input type="text" name='title'>
         <br><br>
         <h4>본문: </h4>
         <textarea name="body" cols="40" rows="10"></textarea>
         <br><br>
         <input class="btn btn-dark" type="submit" value="제출하기">
     </form>
     ```

     - `	<form action="{%url 'create'%}">`  은 `form` 에서 입력받은 값을 `create` 함수에서 처리하겠다는 것.



### 포트폴리오 페이지 만들기

- Django에서 다루는 파일의 종류

  >static file(정적파일) : 미리 서버에 저장되어 있는 파일, 따라서 서버에 저장된 그대로를 서비스 해주는 파일이다.
  >
  >- static : 개발할 때 미리 준비해둔 파일로 프로젝트 입장에서 이미 무엇인지 아는 파일 (외부와 통신 X)
  >- media : 웹서비스 이용자들이 업로드하는 파일 (외부와 통신 O)
  >
  >dynamic file(동적파일) : 서버의 데이터들이 가공된 다음 서비스되는 파일, 따라서 상황에 따라 받는 내용이 달라질 수 있다.

- static 파일 다루기

  1. static폴더를 만들고 그 안에 파일 넣기
  2. settings.py에서 파일을 어디에 모을지 알려주기
  3. static파일들을 한곳에 모아주기
  4. html상에서 static파일을 사용한다고 써주기

- media 파일 다루기

  1. 어느 URL을 타고 올 것인지 정해주기
  2. 어디로 모을 것인지 알려주기

  >1. settings.py에서 media설정(디렉토리,URL설정)
  >2. urls.py설정
  >3. models.py에서 업로드 될 데이터 class 정의
  >4. DB migrate해주기
  >5. admin.py에서 register등록해주기
  >6. views.py에 함수 정의
  >7. html 띄우기



1. portfolio앱을 만들어주기

   1. `$ python3 manage.py startapp portfolio`
   2. `urls.py`, `settings.py` 등 입력해주기. 
   3. `portfolio.html` 부트스트랩에서 `album` example 가져오기

2. `portfolio`폴더 안에 `static` 폴더 생성하고 이미지파일 넣어주기

   1. `settings.py`에 밑의 내용 추가

      ```python
      STATIC_URL = '/static/'   # 원래 있는 내용, 이 밑으로 작성하면 됨.
      
      STATICFILES_DIRS = [
          os.path.join(BASE_DIR, 'portfolio', 'static')   #static 파일들이 현재 어디에 있는지를 쓰는 곳.
      ]   
      
      STATIC_ROOT = os.path.join(BASE_DIR, 'static')  #static 파일들이 어디로 모일 것인지를 쓰는 곳.
      ```

   2. `$ python manage.py collectstatic` 을 실행

      >이 명령어를 실행해주면 최상위 폴더(mydjangoproject)에 static폴더가 생긴다.
      >
      >생기는 이유는 `STATIC_ROOT = os.path.join(BASE_DIR, 'static')` 이 부분에서 static파일들이 모이는 곳을 설정해주었기 때문이다.

3. `portfolio.html` 파일에서 사진파일 넣어주기

   1. `{% load staticfiles %}` 를 `<html>`태그 밖인 맨 위에 넣어준다.
   2. 사진을 넣을 위치에 `<img>를 넣어준다.`
      - `<img src="{% static 'newyork.jpg' %}" height=300 alt="사진이 안 뜰경우 표시">` 

4. 이미지파일을 업로드 할 수 있게 media를 다뤄보기

   1. `settings.py`에 밑의 코드 추가

      ```python
      MEDIA_ROOT = os.path.join(BASE_DIR, 'media')    #medai폴더로 파일들을 모으겠다는 의미
      
      MEDIA_URL = '/media/'   #URL설정
      ```

   2. `urls.py`에 배열에 추가될 url을 더해주는 방식으로 추가해준다.

      ```python
      from django.conf import settings
      from django.conf.urls.static import static
      #위의 내용을 import 해주어야 한다.
      
      urlpatterns = [
          path('admin/', admin.site.urls),
          path('', blog.views.index, name="index"),
          path('blog/<int:blog_id>', blog.views.detail, name="detail"),
          path('blog/new', blog.views.new, name='new'),
          path('blog/create', blog.views.create, name="create"),
          path('portfolio/', portfolio.views.portfolio, name='portfolio'),
      ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
      ```

   3. `models.py`에 class정의 해주기

      ```python
      class Portfolio(models.Model):
          title = models.CharField(max_length = 255)
          image = models.ImageField(upload_to='images/')  #media폴더안에 존재하는 images폴더를 가리킴.
          description = models.CharField(max_length=500)
      
          def __str__(self):
              return self.title
      ```

   4. `$ pip install pillow`

      - `pillow` 는 django에서 이미지를 효율적으로 관리해주는 패키지이다.

   5. `$ python manage.py makemigrations` - 마이그레이션 파일 생성

   6. `$ python manage.py migrate`

   7. `admin.py`에 register등록해주기

      ```python
      from .models import Portfolio
      
      admin.site.register(Portfolio)
      ```

   8. `views.py` 에 함수 수정해주기

      ```python
      from .models import Portfolio
      
      def portfolio(request):
          portfolios = Portfolio.objects
          return render(request, 'portfolio.html', {'portfolios': portfolios})
      ```

   9. `portfolio.html` 수정해주기

      ```html
      {% for portfolio in portfolios.all %}
          <div class="col-md-4">
              <div class="card mb-4 shadow-sm">
                  <img src="{{portfolio.image.url}}" height=300>
                  <div class="card-body">
                      <p class="card-text">{{portfolio.description}}</p>
                      <div class="d-flex justify-content-between align-items-center">
                          <div class="btn-group">
                              <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                              <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                          </div>
                          <small class="text-muted">9 mins</small>
                      </div>
                  </div>
              </div>
          </div>
      {% endfor %}
      ```

      - `{{portfolio.image.url}}` 로 이미지를 불러온다. 이미지는 url을 통하기 때문에 `.url` 을 꼭 붙혀주어야 한다.

5. admin페이지로 가서 사진 업로드 후 확인해보기



### 템플릿 상속

>1. 프로젝트 폴더에 `templates` 폴더 생성
>2. `base.html` 파일 생성
>3. `base.html` 에 중복되는 코드 채워넣기
>4. `settings.py`에 `base.html` 위치 알리기
>5. 사용하고자 하는 `html`파일에서 겹치는 내용 삭제 및 `base.html` 불러오기



1. 프로젝트폴더(`settings.py` 가 있는 폴더)에 `templates` 폴더 생성

2. `templates` 폴더 안에 `base.html` 파일 생성하기

3. html파일들에서 중복되는 코드를 `base.html`에 넣어주기

   ```html
   --------------------------
   		 중복내용
   --------------------------
   
   {% block contents %}
   {% endblock %}
   
   --------------------------
   		 중복내용
   --------------------------
   ```

   - `contents`라는 이름의 `block` 를 지정해주면 저 부분은 각자의 html의 내용을 표시해준다.

4. `settings.py`에 `base.html`위치 알려주기

   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': ['myproject/templates'],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```

   - `'DIRS': ['myproject/templates'],`  비워있으면 채워넣어준다.

5. 사용하고자하는 html파일 수정하기

   ```html
   {% extends 'base.html' %}	<!-- base.html을 사용하겠다고 알려준다. -->
   
   {% block contents %}	<!-- base.html에서 contents부분에 채워진다. -->
   <body>
   <br>
   {% for blog in blogs.all %}
   <div class="container">
   <div class="card">
           <div class="card-body">
               <h2 class="card-title">{{blog.title}}</h2>
               <h6 class="card-subtitle mb-2 text-muted">{{blog.pub_date}}</h6>
               <p class="card-text">{{blog.summary}}</p>
           <a href="{%url 'detail' blog.id%}" class="card-link">...more</a>
           </div>
           </div><br>
       </div>
   {% endfor %}
   
   </body>
   {% endblock %}
   ```

   

### app별로 url관리하기

>app을 다른 프로젝트에서도 사용할 수 있으므로 url을 효율적으로 관리하기 위해서 app별로 url을 관리하면 효율적으로 개발을 할 수 있다.
>
>1. app폴더 안에 `urls.py`를 생성
>2. 프로젝트의 `urls.py`에 app의 url을 알려주기



1. `blog` 폴더안에 `urls.py` 를 생성

2. `blog` 폴더의 `urls.py`에 url작성

   ```python
   from django.contrib import admin
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('<int:blog_id>/', views.detail, name="detail"),
       path('new/', views.new, name='new'),
       path('create/', views.create, name="create"),
   ]
   ```

3. `myproject` 폴더의 `urls.py`를 수정

   ```python
   from django.urls import path, include		#include를 import해준다.
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', blog.views.index, name="index"),
       path('blog/', include('blog.urls')),	#이와 같이 추가해준다.
       path('portfolio/', portfolio.views.portfolio, name='portfolio'),
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

   



# END

