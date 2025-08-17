from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "blog/base.html")

def posts(request):
    return render(request, "blog/posts.html")

def login_view(request):
    return HttpResponse("Logi page (to be built)")

def register(request):
    return HttpResponse("Register page (to be built)")