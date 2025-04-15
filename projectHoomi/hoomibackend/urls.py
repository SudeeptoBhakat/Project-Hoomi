from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PropertyViewSet, BookingViewSet, PaymentViewSet, ReviewViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('properties', PropertyViewSet)
router.register('bookings', BookingViewSet)
router.register('payments', PaymentViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = router.urls
