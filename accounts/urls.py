from django.urls import path, include
from accounts.views import SignOutView, SignInView, UserProfileView, SignUpView


urlpatterns = (
    path('accounts/profile/', UserProfileView.as_view(), name='current user profile'),
    path('accounts/signin/', SignInView.as_view(), name = 'signin user'),
    path('accounts/profile/<int:pk>/', UserProfileView.as_view(), name='user profile'),
    path('accounts/signup/', SignUpView.as_view(), name='signup user'),
    path('accounts/signout/', SignOutView.as_view(), name='signout user'),
    path('accounts/', include('django.contrib.auth.urls')),
)

from .receivers import *
