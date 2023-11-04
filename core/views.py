from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def academy(request):
    return render(request,'core/academy.html')


def university(request):
    return render(request,'core/university.html')


def events(request):
    return render(request,'core/events.html')


def about(request):
    return render(request,'core/about-us.html')


def team(request):
    return render(request,'core/team.html')


def blog(request):
    return render(request,'core/blog-3.html')


def activities_blog(request):
    return render(request,'core/blog-2.html')


def contact(request):
    return render(request,'core/page-contact.html')


def specialization(request):
    return render(request,'core/specialization.html')
