from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import PornVideo, PornCategory
from urllib.parse import urlparse, parse_qs

def home(request):
    videos = PornVideo.objects.all()
    categories = PornCategory.objects.all()
    return render(request, 'pornomovie/home.html', {
        'videos': videos,
        'categories': categories,
        "secili_kategori": None
    })

def porno_detail(request, video_id):
    video = get_object_or_404(PornVideo, id=video_id)
    categories = PornCategory.objects.all()
    return render(request, 'pornomovie/porno_detail.html', {
        'video': video,
        "categories" : categories
        })

def category_videos(request, category_id):
    categories = PornCategory.objects.all()
    category = get_object_or_404(PornCategory, id=category_id)
    videos = PornVideo.objects.filter(category=category)
    return render(request, 'pornomovie/home.html', {
        'videos': videos,
        'category': category,
        'categories': categories,
        "secili_kategori": category
    }) 

def porno_watch(request, video_id):
    video = get_object_or_404(PornVideo, id=video_id)
    categories = PornCategory.objects.all()
    videos = PornVideo.objects.all()  # tüm videoları aldık

    context = {
        'video': video,
        'categories': categories,
        'videos': videos,            # bunu kesin ekle
        'secili_kategori': None,
    }
    return render(request, 'pornomovie/porno_watch.html', context)




def extract_external_id(url):
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)
    return qs.get('viewkey', [None])[0]
