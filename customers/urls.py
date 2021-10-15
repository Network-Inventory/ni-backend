from rest_framework import routers

from . import views


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'owners', views.OwnerViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'locations', views.LocationViewSet)
