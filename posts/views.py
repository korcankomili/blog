from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from .models import Post,Author
from marketing.models import Signup

def index(request):
    
    featured = Post.objects.filter(featured = True)
    latest = Post.objects.filter(featured = True).order_by('-timestamp')[0:3]

    if request.method == "POST":
        email = request.POST["email"]
        newsignup = Signup()
        newsignup.email = email
        newsignup.save()

    context =  {
        'object_list' : featured,
        'latest' : latest
    }

    return render(request, 'index.html', context)

def blog(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list,3)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    most_recent = Post.objects.order_by('-timestamp')[0:3]

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'most_recent':most_recent,
        'page_request_var':page_request_var
    } 

    return render(request, 'blog.html', context)



def post(request, id):
    return render(request, 'post.html', {})