from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from crud import views

router = SimpleRouter()
router.register(r'contact-info', views.ContactInfo)

urlpatterns = [
    url(r'^', include(router.urls))
]

urlpatterns = format_suffix_patterns(urlpatterns)
