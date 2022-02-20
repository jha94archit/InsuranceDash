from django.urls import path
from .views import PolicyViewSet, PolicyByMonthView, PolicyByRegion
from rest_framework import routers

app_name = 'insurance'

router = routers.DefaultRouter()
router.register('policy', PolicyViewSet)

urlpatterns = [
    path('policy_by_month/', PolicyByMonthView),
    path('policy_by_region/', PolicyByRegion),
]

urlpatterns += router.urls
