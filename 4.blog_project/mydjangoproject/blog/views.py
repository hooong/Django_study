from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog

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

def new(request): #new.html을 띄워주는 함수
    return render(request, 'new.html')

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def create(request):  #입력바은 내용을 DB에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body'] 
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id)) #blog.id는  int로 받아오므로 str로 형변환을 해줌.

    #render와 redirect의 차이점은 redirect는 URL을 받음(다른 사이트로도 이동할 수 있다.)  render는 데이터를 담아서 처리하고 싶을 때 사용
    #따라서 인자를 무엇을 주느냐에 따라 사용하는 것이 달라진다.