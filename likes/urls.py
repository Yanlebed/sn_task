from django.conf.urls import include, url
from django.contrib import admin

apipatterns = [
    url(r'^', include('posts.urls')),
]

urlpatterns = [
    url(r'^api/v1/', include(apipatterns, namespace='api')),
    url(r'^admin/', admin.site.urls),
]