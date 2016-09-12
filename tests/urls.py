from django.conf.urls import include, url
from django.contrib import admin

from tests.models import Dummy

admin.site.register(Dummy)

urlpatterns = [
    url('^admin/', include(admin.site.urls)),
]
