from django.shortcuts import render
from .models import PhpbbAlbum, Article, PhpbbAlbumCat, Answer

def home(request):
    arts = PhpbbAlbum.objects.all()
    albums = PhpbbAlbumCat.objects.all()
    context = {'hola': arts, 'albums': albums}
    return render(request, 'app/home.html', context)
def forum(request):
    posts = Article.objects.all()
    answers = Answer.objects.all()
    context = {'posts': posts, 'answers': answers}
    return render(request, 'app/forum.html', context)