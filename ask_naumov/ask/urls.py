from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ask$', views.ask, name='ask'),
    url(r'^hot$', views.hot, name='hot'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^question/(?P<question_id>\d+)$', views.question, name='question'),
    url(r'^settings$', views.settings, name='settings'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^tag/(?P<tag>\w+)$', views.tag, name='tag'),
    url(r'^$', views.index, name='index'),
]
