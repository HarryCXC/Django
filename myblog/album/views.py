from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from .models import AlbumInfo


# Create your views here.

def album(request, id, page):
    albumList = AlbumInfo.objects.filter(user_id=id).order_by('id')
    paginator = Paginator(albumList, 8)
    try:
        pageInfo = paginator.page(page)
    except PageNotAnInteger:
        pageInfo = paginator.page(1)
    except EmptyPage:
        pageInfo = paginator.page(paginator.num_pages)
    return render(request, 'about.html', locals())
