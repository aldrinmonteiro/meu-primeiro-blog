from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone


def lista_postagem(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/lista_postagem.html', {'posts':posts})

def post_detalhe(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detalhe.html', {'post': post}) 
