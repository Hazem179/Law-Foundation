from multiprocessing import context
from django.shortcuts import render
from .models import Blog, Course, News,Event

# Create your views here.
def home(request):
    top_courses = Course.objects.all()[:4]
    top_news = News.objects.all()[:3]
    next_event = Event.objects.all()[:1]
    team = Event.objects.all()[:3]
    context = {'top_courses':top_courses,'top_news':top_news,'next_event':next_event,'team':team, 'titele':'الرئيسية'}
    return render(request,'core/home.html',context=context)

def academy(request):
    courses = Course.objects.all()
    context = {'courses':courses,'title':'الأكاديمية'}
    return render(request,'core/academy.html',context=context)


def university(request):
    return render(request,'core/university.html')


def events(request):
    return render(request,'core/events.html')


def about(request):
    return render(request,'core/about-us.html')


def team(request):
    return render(request,'core/team.html')


def blog(request):
    posts = Blog.objects.all()
    context = {'posts':posts,'title':'المدونة'}
    return render(request,'core/blog-3.html',context=context)


def activities_blog(request):
    all_news = News.objects.all()
    context={'all_news':all_news,'title':'المدونة والأخبار'}
    return render(request,'core/blog-2.html',context=context)


def contact(request):
    return render(request,'core/page-contact.html')


def specialization(request):
    return render(request,'core/specialization.html')
