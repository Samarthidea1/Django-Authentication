from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'Register/$',views.Register.as_view(),name='register'),
    url(r'Login/$',views.Login.as_view(),name='login'),
    url(r"^activate/b'(?P<uidb64>[0-9A-Za-z_\-]+)'/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$",views.activate, name='activate')
]
