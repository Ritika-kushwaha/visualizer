from django.urls import path
from api.views import get_history, upload_csv, register_user
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # 1. The Signup Door
    path('api/register/', register_user),
    
    # 2. The Login Door (gives you the token)
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # 3. The Refresh Door (extends your stay)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # 4. The Data Door
    path('api/upload/', upload_csv),
    path('api/history/', get_history),
]