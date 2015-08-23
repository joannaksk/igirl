from django.conf.urls import urls
from . import views

urlpatterns = [
  url(r'^$', views.IndexView.as_view(), name = 'index'),
  url(r'^article/', include ([
  	url(r'^(?P<aid>[0-9]+)/$', views.article, name = 'article'),
    url(r'^disease/(?P<aid>[0-9]+)/$', views.disease, name = 'disease'),
    url(r'^contraceptive/(?P<aid>[0-9]+)/$', views.contraceptive, name = 'contraceptive'),
    url(r'^product/(?P<aid>[0-9]+)/$', views.product, name = 'product'),
    ])),
  url(r'^healthcentre/(?P<hcid>[0-9]+)/$', views.healthcentre, name = 'healthcentre'),
  url(r'^user/(?P<uid>[0-9]+)/$', views.user, name = 'user'),
]