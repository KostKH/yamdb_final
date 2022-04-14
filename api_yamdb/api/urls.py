from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router_v1 = DefaultRouter()

router_v1.register('genres', views.GenreViewSet)
router_v1.register('categories', views.CategoriesViewSet)
router_v1.register('titles', views.TitlesViewSet)
router_v1.register(r'titles/(?P<title_id>\d+)/reviews',
                   views.ReviewViewSet, basename='reviews')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentViewSet, basename='comments')
router_v1.register('users', views.UserViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', views.APISignup.as_view()),
    path('v1/auth/token/', views.GetTokenView.as_view(), name='token')
]
