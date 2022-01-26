from django.urls import path, include


urlpatterns = [
    path('user/', include('api.v1.user.urls')),
    path('core/', include('api.v1.core.urls'))
]