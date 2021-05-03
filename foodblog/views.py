from django.shortcuts import render
from .models import Post
import datetime
# Create your views here.
def index(request):

    week_ago = datetime.date.today()-datetime.timedelta(days=7)
    khanataiyarhai = Post.objects.filter(time_upload__gte = week_ago).order_by('-read_count')

    params = {
        'posts': Post.objects.all(),
        'trends': khanataiyarhai[:5],
    }

    return render(request,'index.html', params)
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'blog.html')
def post(request):
    return render(request,'blogpost.html')
def about(request):
    return render(request,'about.html')

