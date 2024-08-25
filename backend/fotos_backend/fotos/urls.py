from django.urls import path
#from fotos.views import FotoListAPiView, FotoDetailAPIView
from fotos.views import FotoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('fotos', FotoViewSet, basename='fotos')
urlpatterns = router.urls



""" urlpatterns = [
    path('fotos/', FotoListAPiView.as_view()),
    path('fotos/<int:pk>', FotoDetailAPIView.as_view())
] """
