from rest_framework import routers
from  .viewsets import CategoriaViewSet

router=routers.SimpleRouter()
router.register('Categoria', CategoriaViewSet)

urlpatterns=router.urls