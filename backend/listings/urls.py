from rest_framework import routers

from .views import ListingsViewSet

# создаём роутер и регистрируем viewset
router = routers.DefaultRouter()
router.register(r'listings', ListingsViewSet)

urlpatterns = router.urls