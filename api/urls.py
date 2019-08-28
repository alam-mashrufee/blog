from django.conf.urls import url, include
from .views import CreateView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = {
    url(r'^bucketlists/$', CreateView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)