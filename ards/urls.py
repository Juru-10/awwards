urlpatterns = [
    url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',
        views.MerchDescription.as_view())
    url(r'api/project/project-id/(?P<pk>[0-9]+)/$',
        views.MerchDescription.as_view())
]
