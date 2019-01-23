# DataBase 활용

- DB = 정보저장공간(장고와는 별개 -> db는 여러개가 있을 수 있다.)

  > models.py : 공장
  >
  > class : 틀
  >
  > 객체 : 생성된 데이터


- models.py에 class로 저장할 데이터형식을 정의

```python
class Blog(models.Model):
    title = models.CharField(max_length=200)			#짧은 문자열
    pub_date = models.DateTimeField('date published')	#날짜와 시간
    body = models.TextField()							#긴 문자열
```



- `$ python manage.py makemigrations`  - migration파일 만드는 명령어

- `$ python manage.py migrate` - 실제로 db에 적용하는 명령어



- `$ python manage.py createsuperuser` - 어드민계정을 만드는 명령어

  > admin.py에 데이터 등록
  >
  > admin계정은 /admin에 접속할때 필요한 계정이다.



- admin.py에 blog객체를 등록

```python
from django.contrib import admin
from .models import Blog

admin.site.register(Blog)	#Blog를 admin에 등록해주면 /admin에서 Blog를 다룰 수 있음.
```



- admin에서 제목을 title보여주기

  > models.py에 있는 Blog class안에 추가

```python
def __str__(self):
        return self.title		#제목을 title로 보여주게 하는 메소드
```



## template에 db내용 띄우기

> view를 통해서 데이터를 받아온다.



- views.py에 다음을 추가

```python
from .models import Blog		#models의 Blog를 import하기

def home(request):
    blogs = Blog.objects		#쿼리셋(전달받은 객체)
    return render(request, 'home.html', {'blogs': blogs})	#Blog에서 objects를 받아서 render 해주기
```



- 쿼리셋, 메소드

> 형식 : 모델.쿼리셋(objects).메소드
>
> ex) `Blog.objects.all`,  `Blog.objects.first` ...



- `home.html`작성

```html
{% for blog in blogs.all %}
    <h1> {{blog.title}} </h1>
    <p> {{blog.pub_date}} </p>
    <p> {{blog.body}} </p>
    <br><br>
{% endfor %}
```



# End