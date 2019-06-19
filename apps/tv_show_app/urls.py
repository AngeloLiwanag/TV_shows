from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^shows$', views.index), #display page 1
    url(r'^shows/new$', views.display_page2), #display page 2
    url(r'^create$', views.create), #create new show
    url(r'^shows/(?P<user_id>\d+)$', views.display_page3), #display page 3 
    url(r'^edit/(?P<user_id>\d+)$', views.display_page4), #display page 4
    url(r'^edit_info/(?P<user_id>\d+)$', views.edit_info), # updates the users info
    url(r'^delete/(?P<user_id>\d+)$', views.delete), #deletes show
]