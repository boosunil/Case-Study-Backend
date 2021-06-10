from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns
from charts import views


router = SimpleRouter()
router.register(r'charts', views.ImportView)

urlpatterns = [
    url(r'^', include(router.urls))
]

urlpatterns = format_suffix_patterns(urlpatterns)
