from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def blog(request):
    return render(request, 'blog-single.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def work(request):
    return render(request, 'work.html')

def blogger(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')

def tester(request):
    return render(request, 'testing.html')