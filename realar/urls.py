from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name = 'realindex'),
    path('about/', views.about, name = 'aboutindex'),
    path('agent/', views.agent, name = 'agentindex'),
    path('contact/', views.contact, name = 'contactindex'),
    path('dashboard/', views.dashboard, name = 'dashboardindex'),
    path('properties/', views.properties, name = 'propertiesindex'),
    path('property/', views.property, name = 'propertyindex'),

    # path('blogs/', views.blogs, name = 'blogsindex'),
    
    # path('<slug:slug>/', views.blog, name='blogindex'),

    path('faq/', views.faq, name = 'faqindex'),
    path ('property/<int:listing_id>/', views.property, name='property'),
    path ('property/search', views.searchh, name='searchh'),
    
    path('blog/blogs/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),

    
    path('blogs/', views.blogs, name = 'blogsindex'),
    
    path('<slug:slug>/', views.blog, name='blog1index'),
]

