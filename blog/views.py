from django.shortcuts import render

# Create your views here.

def post_list(request):
    context = {
        'judul': 'INI POST_LIST',
    }
    return render(request, 'blog/post_list.html', context)