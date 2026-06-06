from django.urls import include, path
from rest_framework.authtoken import views as token_views
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = SimpleRouter()
router.register("posts", PostViewSet)
router.register("groups", GroupViewSet)
router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)

urlpatterns = [
    path("api-token-auth/", token_views.obtain_auth_token),
    path("", include(router.urls)),
]
