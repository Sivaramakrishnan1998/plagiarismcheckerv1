from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import Check
import re
import login.views

from django.conf import settings
from django.conf.urls.static import static


app_name = 'checker';
urlpatterns = [
	url(r'^$',views.indexpage,name='indexpage'),
	url(r'^deepcheck/',Check.as_view(),name = 'deepcheck'),
	url(r'^viewdocument/(?P<string>[^/]+)$',views.viewdocument,name = 'viewdocument'),
	url(r'^login/$', login.views.user_login_and_register,name='login'),
	url(r'^institutionlogin/$', login.views.institution_login_and_register,name='institutionlogin'),
	url(r'^logout/', login.views.logout_page),
	url(r'^contact	/', login.views.logout_page	),
	url(r'^register/', login.views.register),
    url(r'^plagchecker',views.geturls,name='geturls'),
    url(r'^subusers/$',views.subusers,name='subusers'),
    url(r'^addusers/$',views.addusers,name='addusers'),
	url(r'^upload/$', views.model_form_upload, name='model_form_upload'),
	url(r'^show/(.*)/$',views.show,name='show'),
	# url(r'^show/(?P<string>[^/]+)$',views.viewdocument,name='viewdocument'),
	# url(r'^download/(.*)/$',views.report,name='report'),
	url(r'^dashboard/',views.dashboard,name='dashboard'),
	url(r'^imageUpload/', views.FileView.as_view()),
	]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
