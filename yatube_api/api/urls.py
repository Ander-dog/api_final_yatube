from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt import views

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'
version = 'v1'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path(f'{version}/', include(router.urls)),
    path(
        f'{version}/jwt/create/',
        views.TokenObtainPairView.as_view(),
        name='token_create'
    ),
    path(
        f'{version}/jwt/refresh/',
        views.TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        f'{version}/jwt/verify/',
        views.TokenVerifyView.as_view(),
        name='token_verify'
    ),
]
