from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from .choices import price_choices,bedroom_choices,state_choices
from .models import List

from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger





def index(request):
    listings = List.objects.order_by ('-list_data').filter (is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render (request, 'real/index.html', context)

def about(request):
    return render(request, 'real/about.html')


def agent(request):
    return render(request, 'real/agent-single.html')


def contact(request):
    return render(request, 'real/contact.html')


def dashboard(request):
    return render(request, 'real/dashboard.html')




def properties(request):
    listings = List.objects.order_by ('-list_data').filter (is_published=True)
    paginator = Paginator (listings, 8)
    page = request.GET.get ('page')
    paged_listings = paginator.get_page (page)
    context = {
    'listings': paged_listings,
    'state_choices': state_choices,
    'price_choices': price_choices,
    'bedroom_choices': bedroom_choices,
    }
    return render (request, 'real/properties.html', context)




def property(request, listing_id):

    property = get_object_or_404 (List, pk=listing_id)

    context = {
        'property': property
    }

    return render (request, 'real/property.html', context)




def faq(request):
    return render(request, 'real/faq.html')



def searchh(request):
    queryset_list = List.objects.order_by ('list_data')
    # keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
            Q(title__icontains=keywords) |
            Q(description__icontains=keywords) |
            Q(address__icontains=keywords) |
            Q(city__icontains=keywords) |
            Q(state__icontains=keywords) |
            Q(zipcode__icontains=keywords)
        )

    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter (city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter (state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter (bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter (price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings': queryset_list,
        'values': request.GET
    }
    return render (request, 'real/search.html', context)






def blog_list(request):
    posts = Post.objects.filter(status='published')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    return render(request, 'blog/blog_detail.html', {'post': post})


# def blogs(request):
#     posts = Post.objects.filter(status='published')
#     return render(request, 'real/blogs.html', {'posts': posts})

def blog(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    return render(request, 'real/blog.html', {'post': post})

def blogs(request):
    post_list = Post.objects.filter(status='published')
    paginator = Paginator(post_list, 8)  # Show 5 posts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'real/blogs.html', {'posts': posts})



