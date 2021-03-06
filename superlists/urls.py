from django.conf.urls import include, url
from lists import views as list_views  #1
from lists import urls as list_urls  #2

urlpatterns = [
    url(r'^$', list_views.home_page, name='home'),
    url(r'^home', list_views.todo_list, name='todo_list'),
    url(r'^blog', list_views.blog, name='blog'),
    url(r'^lists/', include(list_urls)),
    # url(r'^admin/', include(admin.site.urls)),
]