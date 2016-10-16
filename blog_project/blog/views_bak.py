from django.shortcuts import render
import logging
from django.conf import settings
from models import Category, Article, Ad
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
logget = logging.getLogger('blog.views')


def global_set(request):
    
    s = {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESC
    }
    return s


def base(request):
    try:
        return render(request, 'base.html', locals())
    except Exception as e:
        logget.error(e)


def index(request):
    try:
        category_list = Category.objects.all()
        # article list
        articles = Article.objects.all()
        paginator = Paginator(articles, 10)  # paginator
        page = request.GET.get('page')
        try:
            article_list = paginator.page(page)
        except PageNotAnInteger:
            article_list = paginator.page(1)
        except EmptyPage:
            article_list = paginator.page(paginator.num_pages)

        # ads
        ad_list = Ad.objects.all()
        if len(ad_list) > 4:
            ad_list = Ad.objects.all()[:4]

        # articles file
        archive_list = Article.objects.distinct_date()

        return render(request, 'index.html', locals())
    except Exception as e:
        logget.error(e)


# archive articles
def archive(request):
    # article for year and month
    year = request.GET.get('year')
    month = request.GET.get('month')
    date_publish = '{0}-{1}'.format(year, month)
    try:
        category_list = Category.objects.all()
        # article list
        articles = Article.objects.filter(date_publish__icontains=date_publish)
        paginator = Paginator(articles, 10)  # paginator
        page = request.GET.get('page')
        try:
            article_list = paginator.page(page)
        except PageNotAnInteger:
            article_list = paginator.page(1)
        except EmptyPage:
            article_list = paginator.page(paginator.num_pages)

        # ads
        ad_list = Ad.objects.all()
        if len(ad_list) > 4:
            ad_list = Ad.objects.all()[:4]

        # articles file
        archive_list = Article.objects.distinct_date()

        return render(request, 'archive.html', locals())
    except Exception as e:
        logget.error(e)