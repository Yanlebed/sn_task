from django.conf.urls import url
from . import views as views

app_name = 'user'

urlpatterns = [
    url(r'^register$', views.RegisterView.as_view(), name='register'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^logout$', views.LogoutView.as_view(), name='logout'),
    url(r'self', views.UserSelfView.as_view(), name='self'),
]