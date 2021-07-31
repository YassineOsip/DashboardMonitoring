from django.conf.urls import url

from DashboardMonitoring import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^production$', views.production, name='production'),
    url(r'^quality$', views.quality, name='quality'),
    url(r'^chainDetail/(?P<chainId>\d+)/$', views.chainDetail, name='chainDetail'),
    url(r'^productivityPerHour$', views.productivityPerHour, name='productivityPerHour'),
]
