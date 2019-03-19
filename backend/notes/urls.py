from rest_framework import routers

from .views import NoteViewSet

# создаём роутер и регистрируем viewset
router = routers.DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = router.urls