from django.conf.urls import url
from .views import upload_pdf


urlpatterns = [
    url(r'^$', upload_pdf)
]
