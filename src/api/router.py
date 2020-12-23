from .viewsets import CategoryViewSet, ProductViewSet, ProductItemViewSet, UserProfileViewSet, AddressViewSet, OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'productitems', ProductItemViewSet)
router.register(r'userprofile', UserProfileViewSet)
router.register(r'address', AddressViewSet)
router.register(r'order', OrderViewSet)
