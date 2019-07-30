from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog 

def home(request):
    blogs = Blog.objects 
    # queryset = .objects로 모델로부터 전달 받은 객체 목록 
    # method
    return render(request, 'home.html', {'blogs':blogs})

    # 쿼리셋과 메소드의 형식
    # 모델.쿼리셋(objects).메소드

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    # 이용자가 원한 몇 번 블로그 객체 
    return render(request, 'detail.html', {'blog':blog_detail})

# new.html을 띄워주는 함수
def new(request):
    return render(request, 'new.html')

# 입력받은 내용을 데이터베이스에 넣어주는 함수
def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() # queryset method 중 하나 
    # <-> 객체.delete()
    return redirect('/blog/'+str(blog.id)) # render 함수와 차이! 
    # redirect는 인자를 URL로 받음