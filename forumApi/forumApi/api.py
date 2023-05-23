from rest_framework import routers
from posts import api_views


router = routers.DefaultRouter()

router.register(r'categories', api_views.CategoryViewset)
router.register(r'posts', api_views.PostsViewset)
router.register(r'user_profiles', api_views.UserProfileViewset)
