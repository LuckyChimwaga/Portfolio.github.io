from django.urls import path
from .import views


urlpatterns=[
    path('' ,views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('about', views.about, name='about'),
    path('blogger', views.blogger, name='blogger'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('tester', views.tester, name='tester')
]