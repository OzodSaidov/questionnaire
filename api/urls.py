from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from user.token import MyTokenObtainPairView

urlpatterns = [
    path('v1/', include('api.v1.urls')),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
