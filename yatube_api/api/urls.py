from django.urls import include, path
from rest_framework.authtoken import views as token_views
from rest_framework.routers import SimpleRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router_v1 = SimpleRouter()
router_v1.register("posts", PostViewSet, basename="post")
router_v1.register("groups", GroupViewSet, basename="group")
router_v1.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)

urlpatterns = [
    path("api-token-auth/", token_views.obtain_auth_token),
    path("", include(router_v1.urls)),
]
