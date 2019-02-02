# Blog project

- bootstrap에서 `navbar`, `card title` 등등 적용

- 글 내용 100글자만 뜨게 하고 `...more`버튼 추가



## 글쓰기 페이지 만들기

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



