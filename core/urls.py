from django.urls import path
from core.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('token-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginView.as_view()),
    path('create-user/', UsercreationView.as_view()),
    path('edit-luggagepost/', EditluggageView.as_view()),
    path('order/', OrderView.as_view()),
    path('orders/',StafforderView.as_view())
]
