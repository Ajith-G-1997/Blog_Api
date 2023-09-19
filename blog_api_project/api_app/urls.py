from rest_framework import routers
from .views import ItemViewSet, create_item  # Import the create_item view function
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/create_item/', create_item, name='create_item'),  # Add the create_item URL
]
