from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$',views.home,name='home'),
    url(r'^prof$',views.prof,name='prof'),
    url(r'^project$',views.project,name='project'),
    url(r'^search$',views.search,name='search'),
    url(r'^login$',views.login,name='login'),
    url(r'^new_prof$',views.new_prof,name='new_prof'),
    url(r'^new_project$',views.new_project,name='new_project'),
    url(r'^registration_form$',views.registration_form,name='registration_form'),
    url(r'^review$',views.review,name='review'),
    url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',views.ProfileDescription.as_view()),
    url(r'api/project/project-id/(?P<pk>[0-9]+)/$',views.ProjectDescription.as_view())
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
