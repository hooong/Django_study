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



##Show구현하기(게시글 보여주기)

>- `home.html`같은 경우에는 모든 Blog객체를 담아 보여준다.
>- `detail.html`에서는 특정id의 객체를 담아서 보여준다.
>- 127.0.0.1:8000/blog/x(객체번호) -> path Converter(url을 계층적으로 디자인)



1. `home`에서 내용을 100글자 제한으로 두기

   1. models.py에서 메서드추가해주기

   ```python
       def summary(self):
           return self.body[:100]
   ```

   2. `home.html` 수정하기 -> {{blog.summary}}
   3. 더보기로 누르면 `detail.html`로 가는 "...more"를 만들어준다.
   4. `{% url 'detail' blog.id %}` 는 detail로 갈때 `blog.id` 값을 같이 넘겨준다.

   ```html
   {% for blog in blogs.all %}
       <h1>제목 :  {{blog.title}} </h1>
       <p>날짜 :  {{blog.pub_date}} </p>
       <p>본문 미리보기 :  {{blog.summary}}<a href="{% url 'detail' blog.id %}">...more</a> </p>
       <br><br>
   {% endfor %}
   ```



2. `views.py`에 메서드 작성

```python
from django.shortcuts import render, get_object_or_404 #get_object_or_404를 import해준다.

def detail(request, blog_id):			#여기선 request와 blog_id 두개의 인자를 받는다.
    blog_detail = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'detail.html', {'blog':blog_detail})
```

- `get_object_or_404(어떤 클래스, 검색조건(몇번데이터,pk))` 
  - 검색을 했는데 일치하는 데이터가 없다면 404에러를 띄어준다.
- `pk = primary key`(객체들의 이름표, 구분자, 데이터의 대표값(대표값은 정하기 나름))

3. `urls.py`에 url을 추가해준다.

```python
path('blog/<int:blog_id>', blog.views.detail, name="detail"),
```

- `<int:blog_id>`는 `blog_id`라는 인자를 int형(정수)으로 받아주겠다는 뜻이다.

4. `detail.html` 작성하기.

```html
<h1>자세한 본문 내용</h1>
<br><br>
<h1> 제목 : {{blog.title}} </h1>
<p> 작성 날짜 : {{blog.pub_date}} </p>
<p> 자세한 본문 : {{blog.body}} </p>
```



# End