from django.urls import include, path
from rest_framework import routers

from api.views import (PostViewSet, CommentViewSet,
                       GroupViewSet, FollowViewSet)


router_var1 = routers.DefaultRouter()
router_var1.register('posts', PostViewSet, basename='posts')
router_var1.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                     basename='comments')
router_var1.register('groups', GroupViewSet, basename='groups')
router_var1.register('follow', FollowViewSet, basename='following')

urlpatterns = [
    path('v1/', include(router_var1.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
