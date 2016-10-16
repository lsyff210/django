# coding:utf-8
from django.shortcuts import render, redirect
from django.conf import settings
from models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Sum
from forms import RegForm, LoginForm, CommentForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from time import strftime


def global_set(request):
    # 基本信息
    s = {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESC,
    }
    SITE_NAME = s['SITE_NAME']
    SITE_DESC = s['SITE_DESC']
    # category list
    category_list = Category.objects.all()

    # ads
    ad_list = Ad.objects.all()
    if len(ad_list) > 4:
        ad_list = Ad.objects.all()[:4]

    # tags
    tag_list = Tag.objects.all()

    # articles file
    date_list = Article.objects.values('date_publish')
    distinct_list = []
    for date_original in date_list:
        date = date_original['date_publish'].strftime('%Y.%m')
        if date not in distinct_list:
            distinct_list.append(date)
    archive_list = distinct_list

    # browse list
    articles_by_cilck = Article.objects.all().order_by('-click_count')

    # browse list
    articles_by_recommend = Article.objects.all().order_by('-is_recommend')

    # comment list
    articles_by_comment = Article.objects.filter().annotate(
        comment_count=Count('comment')).order_by('-comment_count')

    # Friendship link
    links_list = Links.objects.all()
    return locals()  # 分页函数


def paginator_article(request, ars, limit):
    # article list
    paginator = Paginator(ars, limit)  # paginator
    page = request.GET.get('page')
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)
    return article_list


def base(request):
    return render(request, 'base.html', locals())


# 注册
def register(request):
    args = {}
    if request.method == 'POST':
        regform = RegForm(request.POST)
        if regform.is_valid():
            user = User(username=regform.cleaned_data['username'],
                        email=regform.cleaned_data['email'],
                        url=regform.cleaned_data['url'],
                        password=make_password(regform.cleaned_data['password']),
                        )
            user.save()
            # 登录
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # 指定默认的登录验证方式
            login(request, user)
            return redirect(request.POST.get('source_url'))
        else:
            # 获取错误信息，只为测试使用
            errors = regform.non_field_errors()
    else:
        if request.user.is_authenticated():
            messages.success(request, '您的账户已经登录！')
            return redirect('/')
        regform = RegForm()
    return render(request, 'reg.html', locals())


def do_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                user.backend = 'django.contrib.auth.backends.ModelBackend'  # 指定默认的登录验证方式
                login(request, user)
            else:
                login_error = '用户名或密码错误'
                return render(request, 'login.html', locals())
            return redirect(request.POST.get('source_url'))
        else:
            login_error = login_form.non_field_errors()
            return render(request, 'login.html', locals())
    else:
        if request.user.is_authenticated():
            messages.success(request, '您的账户已经登录！')
            return redirect('/')
        login_form = LoginForm()
    return render(request, 'login.html', locals())


# 退出登录
def do_logout(request):
    try:
        logout(request)

    except Exception as e:
        print e
    return redirect(request.META['HTTP_REFERER'])


def index(request):
    title = "最新文章"
    # article list
    articles = Article.objects.all()
    article_list = paginator_article(request, ars=articles, limit=10)
    return render(request, 'index.html', locals())


# archive articles
def archive(request):
    # article for year and month
    year = request.GET.get('year')
    month = request.GET.get('month')
    date_publish = '{0}-{1}'.format(year, month)
    try:
        page_judge = "&year={0}&month={1}".format(year, month)
        title = "{0}年{1}月文章".format(year, month)
        # article list
        articles = Article.objects.filter(date_publish__icontains=date_publish)
        article_list = paginator_article(request, ars=articles, limit=2)

        return render(request, 'archive.html', locals())
    except Exception as e:
        print(e)


def tag(request):
    # article for year and month
    tag_get = request.GET.get('tag')
    try:
        # 页码判断
        page_judge = "&tag={}".format(tag_get)
        # article list
        article_tag = Tag.objects.get(id=int(tag_get))
        title = 'Tag: {0}'.format(article_tag)
        articles = article_tag.article_set.all()
        # articles2 = Article.objects.filter(tag__article__tag=int(tag_get)).distinct()
        # print articles2
        article_list = paginator_article(request, ars=articles, limit=2)

        return render(request, 'archive.html', locals())
    except Exception as e:
        print(e)


def category(request):
    # article for year and month
    category_get = request.GET.get('category_get')
    try:
        # 页码判断
        page_judge = "&category_get={}".format(category_get)
        # article list
        article_category = Category.objects.get(id=int(category_get))
        title = article_category
        articles = article_category.article_set.all()
        article_list = paginator_article(request, ars=articles, limit=2)

        return render(request, 'archive.html', locals())
    except Exception as e:
        print(e)


def article(request):
    get_id = request.GET.get('id')
    try:
        comment_form = CommentForm({'username': request.user.username,
                                    'email': request.user.email,
                                    'url': request.user.url,
                                    'article': get_id} if request.user.is_authenticated() else{'article': get_id})
        url = request.get_host() + request.get_full_path()
        # article
        get_article = Article.objects.get(id=get_id)
        comments = Comment.objects.filter(article=get_article).order_by('id')
        comment_count = len(comments)
        comment_list = comments
        return render(request, 'article.html', locals())
    except Exception as e:
        print(e)


# 获取评论内容，Comment使用pid时使用
# def comment_list_get(comments):
#     comment_list = []
#     for comment in comments:
#         if comment.pid is None:
#             comment_list.append(comment)
#             setattr(comment_list[-1], 'child_comment', [])
#         else:
#             for item in comment_list:
#                 if comment.pid == item:
#                     item.child_comment.append(comment)
#     return comment_list


# 提交评论
def comment_post(request):
    try:
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                pid = comment_form.cleaned_data['pid']
                rid = comment_form.cleaned_data['rid']
                if pid:
                    table = Response()
                    table.pid_id = pid
                    table.rid_id = rid
                else:
                    table = Comment()
                content = comment_form.cleaned_data['content']
                article_get = comment_form.cleaned_data['article']
                table.content = content
                table.article_id = article_get

                if request.user.is_authenticated():
                    table.user = request.user
                    # comment = Comment(user=request.user, content=content, article_id=int(article_get))
                else:
                    username = comment_form.cleaned_data['username']
                    email = comment_form.cleaned_data['email']
                    url = comment_form.cleaned_data['url']
                    table.username = username
                    table.email = email
                    table.url = url
                    # comment = Comment(username=username, email=email, url=url, article=article_get, content=content)
                table.save()
            else:
                messages.error(request, '您的数据有问题，请重新输入数据')
            return redirect(request.META['HTTP_REFERER'])
        else:
            return redirect('/')
    except Exception as e:
        print(e)


def comment_delete(request):
    delete_id = None
    table = None
    try:
        if request.method == 'POST':
            post_key = [i for i in request.POST]
            if u'delete_comment_id' in post_key:
                delete_id = int(request.POST['delete_comment_id'])
                table = Comment
            if u'delete_response_id' in post_key:
                delete_id = int(request.POST['delete_response_id'])
                table = Response

            if delete_id:
                delete_comment = table.objects.get(id=int(delete_id))
                try:
                    delete_comment.delete()
                except Exception as e:
                    messages.error(request, '您的评论已经被回复，无法删除，请联系管理员。')
                    print(e)
        return redirect(request.META['HTTP_REFERER'])
    except Exception as e:
        print e
        print(e)
