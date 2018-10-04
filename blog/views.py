from django.shortcuts import render

def lista_postagem(request):
    return render(request, 'blog/lista_postagem.html', {})

