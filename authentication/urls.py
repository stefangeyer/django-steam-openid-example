from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from authentication.views import IndexView, LogoutView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^logout', login_required(LogoutView.as_view(), login_url='/'), name='logout')
]
