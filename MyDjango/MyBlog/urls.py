from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/$', views.get_blogs),
    url(r'^detail/(\d+)/$',views.get_details, name='blog_get_detail'),

]