from rest_framework.routers import SimpleRouter
from main.views import PostViewSet, CommentViewSet


router = SimpleRouter()
router.register("posts", PostViewSet)
router.register("comments", CommentViewSet)

urlpatterns = router.urls
