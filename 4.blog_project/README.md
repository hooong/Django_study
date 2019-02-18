# Blog project

- bootstrap에서 `navbar`, `card title` 등등 적용

- 글 내용 100글자만 뜨게 하고 `...more`버튼 추가

- 글쓰기 페이지 추가

- 포트폴리오 페이지 추가

- static, media 파일 다루기

- 계정관리 추가 (회원가입, 로그인, 로그아웃)

  

----

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



----

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



----

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



----

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



----

# 계정관리

> `accounts`라는 앱을 만들고 회원가입, 로그인, 로그아웃의 함수들을 작성. 

1. `$ python3 manage.py startapp accounts`  - accounts앱을 만들어준다.

2. `urls.py` 작성해준다

   ```python
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('signup/', views.signup, name='signup'),
       path('login/', views.login, name='login'),
       path('logout/', views.logout, name='logout'),
   ]
   ```

3. `signup.html` 을 작성

   ```html
   {% extends 'base.html' %}
   
   {% block contents %}
   <div class="container">
       <h1>Sign Up!</h1>
   
       <form action="{%url 'signup' %}" method="POST">
           {% csrf_token %}
           Username:
           <br>
           <input type="text" name="username" value="">
           <br>
           Password:
           <br>
           <input type="password" name="password1" value="">
           <br>
           Confirm Password:
           <br>
           <input type="password" name="password2" value="">
           <br>
           <br>
           <input type="submit" class="btn btn-primary" value="Sign Up!">
       </form>
   </div>
   {% endblock %}
   ```

   - *csrf_token* : csrf공격을 막아주기 위해 난수를 발생시켜준다. 이 난수를 이용해 암호화할 수 있다.

4. `login.html` 을 작성

   ```html
   {% extends 'base.html' %}
   
   {% block contents %}
   <div class="container">
       <h1>Login</h1>
   
       <form action="{%url 'login' %}" method="POST">
           {% csrf_token %}
           Username:
           <br>
           <input type="text" name="username" value="">
           <br>
           Password:
           <br>
           <input type="password" name="password1" value="">
           <br>
           <br>
           <input type="submit" class="btn btn-primary" value="Sign Up!">
       </form>
   </div>
   {% endblock %}
   ```

5. `views.py` 에 함수 작성

   ```python
   from django.shortcuts import render, redirect
   from django.contrib.auth.models import User		#유저관리를 위해 import해주기
   from django.contrib import auth					#유저관리를 위해 import해주기
   
   def signup(request):
       if request.method == 'POST':
           if request.POST['password1'] == request.POST['password2']:
               user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])  #db에 실제로 있는 회원명단이 있는지 확인해주는 메서드
               auth.login(request, user)
               return redirect('index')
       return render(request, 'signup.html')
   
   def login(request):
       if request.method == 'POST':
           username = request.POST['username']
           password = request.POST['password1']
           user = auth.authenticate(request, username = username, password = password)
           if user is not None:
               auth.login(request, user)
               return redirect('index')
           else:
               return render(request, 'login.html', {'error': 'username or password is incorrect.'})
       else:
           return render(request, 'login.html')
   
   def logout(request):
       if request.method == 'POST':
           auth.logout(request)
           redirect('index')
       return render(request, 'login.html')
   ```

6. `base.html` 에 회원가입, 로그인, 로그아웃 버튼 추가

   ```html
   {% if user.is_authenticated %}
   <li class="nav-item dropdown">
       <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
           환영합니다. {{ user.username }}님!
       </a>
       <div class="dropdown-menu" aria-labelledby="navbarDropdown">
           <a class="dropdown-item" href="{%url 'new'%}">글쓰기</a>
           <a class="dropdown-item" href="javascript:{document.getElementById('logout').submit()}">로그아웃</a>
           <form id='logout' action="{%url 'logout'%}" method="POST">
               {% csrf_token %}
               <input type="hidden">
           </form>
       </div>
   </li>
   {% else %}
   <li class='nav-item'>
       <a class="nav-item nav-link" href="{%url 'signup'%}">회원가입</a>
   </li>
   <li>
       <a class="nav-item nav-link" href="{%url 'login'%}">로그인</a>
   </li>
   {% endif %}
   ```

   

------

### http Method

[][]

|    상황     | Method |
| :---------: | :----: |
| 데이터 조회 |  GET   |
| 데이터 생성 |  POST  |
| 데이터 수정 |  PUT   |
| 데이터 삭제 | DELETE |



----

### Pagination

> 게시글을 일정 개수만큼만 페이지별로 관리를 할 수 있게하는 것.

- *paginator class* : 잘라진 식빵상태의 객체

- *page class* : 잘라진 식빵 중 한 개의 식빵객체

| 함수                        | 뜻                                      |
| --------------------------- | --------------------------------------- |
| page.count()                | 총 객체 수                              |
| paginator.num_pages()       | 총 페이지 개수                          |
| page.page(n)                | n번째 페이지 리턴                       |
| page.page_range()           | (1부터 시작하는)페이지 리스트 반환      |
| page.get_page(n)            | n번 페이지 갖고오기                     |
| page.has_next()             | 다음 페이지가 있으면 True, 없으면 False |
| page.has_previous()         | 이전 페이지가 있으면 True, 없으면 False |
| page.previous_page_number() | 이전 페이지 번호 반환                   |

1. `views.py` 수정하기

   ```python
   from django.core.paginator import Paginator	#paginator를 import하기
   
   def index(request):
       blogs = Blog.objects
       
       #블로그 모든 글들을 리스트에 담아준다.
       blog_list = Blog.objects.all()
       #게시글을 최신순으로 하기위해 역순으로 저장.
       blog_list_reverse = blog_list[::-1]
       #블로그 객체 세 개를 한 페이지로 자르기
       paginator = Paginator(blog_list_reverse,3)
       #request된 페이지가 뭔지 알아내기
       page = request.GET.get('page')
       #request된 페이지를 얻어오고 딕셔너리로 return 해주기
       posts = paginator.get_page(page)
       return render(request, 'index.html', {'blogs': blogs, 'posts':posts})
   ```

   - 페이지 번호 알아내기

     `page = request.GET.get('page')`

     - request - 사용자가 요청하는 것에 대한 모든 정보를 담고 있는 객체

     - GET - request안에서 GET방식을 불러오는 함수

     - .get() - (딕셔너리 형에 대해서) key값을 인자로 주면 value값을 반환해주는 함수

       > request.GET은 딕셔너리 자료형으로 들어온다.
       >
       > ex) URL -> www.google.com?thisIsAGetVarKey=3&thisIsAnotherOne=hello
       >
       > ​	request.GET -> {"thisIsAGetVarKey": 3, "thisIsAnotherOne": hello}

2. `index.html` 수정하기

   ```html
   <div class='container'>
       {#First Prev#}
       {%if posts.has_previous%}
       <a href="?page=1">First</a>
       <a href="?page={{posts.previous_page_number}}">Prev</a>
       {%endif%}
       
       {# 3of4 #}
       <span>{{posts.number}}</span>
       <span>of</span>
       <span>{{posts.paginator.num_pages}}</span>
       
       {#Next Last#}
       {%if posts.has_next%}
       <a href="?page={{posts.next_page_number}}">Next</a>
       <a href="?page={{posts.paginator.num_pages}}">Last</a>
       {%endif%}
   </div>
   ```



----



### Form

> 자동으로 html `form`형식을 만들어준다.
>
> 또한 함수를 사용해 입력되는 값을 검증해준다.



1. `blog app` 폴더에 `form.py` 파일 생성

   - 만들어져 있는 모델을 이용해서 입력공간 만들기

     ```python
     from django import forms
     from .models import Blog	#같은 blog app에 있는 models.py에서 Blog 모델을 import
     
     class BlogPost(forms.ModelForm):	#모델을 이용하려면 .ModelForm 사용.
          class Meta:					#meta class는 쉽게 말해 클래스 안의 클래스
              model = Blog				#기반으로 할 모델을 입력해준다.
              fields = ['title', 'body']	#입력받을 필드를 입력해준다.
     ```

   - 임의의 입력공간 만들기

     ```python
     from django import forms
     from .models import Blog
     
     class BlogPost(forms.Form):		#모델을 이용하는 것과 다르게 .Form을 사용.
         email = forms.EmailField()
         files = forms.FileField()
         url = forms.URLField()
         words = forms.CharField(max_length=200)
         max_number = forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three')])
     ```

2. `newblog.html` 을 생성하고 `url` 설정

   ```html
   {% extends 'base.html' %}
   
   {% block contents %}
   <br>
   <div class="container">
       <form method="POST">
           {% csrf_token %}
           <table>
               {{form.as_table}}		<!-- table로 만들어준다(as_p, as_ul등도 있다) -->
           </table>
           <br>
           <input class="btn btn-dark" type="submit" value="제출하기">
       </form>
   </div>
   {% endblock %}
   ```

3. `views.py`에 함수 정의해주기

   ```python
   from .form import BlogPost			#form.py에서 BlogPost객체를 import
   from django.utils import timezone	#pub_date에서 현재시간을 저장하기위해 import
   
   
   def blogpost(request):
       # 1. 입력된 내용을 처리하는 기능 -> POST
       if request.method == 'POST':
           form = BlogPost(request.POST)
           if form.is_valid(): #예외처리를 해주는 함수(이메일 형식에 맞지않다거나 입력을 하지 않았다거나...)
               post = form.save(commit=False) #저장하지 않고 모델객체를 불러온다.
               post.pub_date = timezone.now()
               post.save()
               return redirect('index')
       # 2. 빈페이지를 띄워주는 기능 -> GET
       else:
           form = BlogPost()
           return render(request, 'newblog.html', {'form':form})
   ```

   

# END
