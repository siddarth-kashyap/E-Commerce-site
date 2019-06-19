from django.conf.urls import url
from . import views
from .views import emailView, enqView

urlpatterns = [
	url(r'^email/$', views.emailView, name='email'),
	url(r'^enq/$', views.enqView, name='enq'),
#    url(r'^success/$', views.successView, name='success'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
