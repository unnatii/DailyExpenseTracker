from django.conf.urls import url
from .views import ( 
           PostListView,
           PostCreateView,
            PostUpdateView
)           
           
from . import views

urlpatterns = [
      url(r'^index/', views.index, name='index'),
   # url(r'^Home/', views.Home, name='Home'),
    url(r'^list/', PostListView.as_view(), name='list'),
    url(r'Home/', PostCreateView.as_view(), name='Home'),
   # url(r'^index/<int:pk>/Update/', PostUpdateView.as_view(), name='Home'),
    url('^delete/(?P<expense_id>[0-9]+)',views.delete,name="delete"),
    url('^edit/(?P<pk>[0-9]+)',PostUpdateView.as_view(),name="edit"),
    url(r'^total/', views.total, name='total'),
]