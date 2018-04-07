from django.conf.urls import url
from . import views
app_name = 'LonFon'
urlpatterns = [
    url(r'^$',views.home , name='home'),
    url(r'^add$',views.add_entry,name='add'),
    url(r'^search$',views.search,name='search'),
]
