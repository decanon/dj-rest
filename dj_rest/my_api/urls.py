from django.urls import path, include
from .views import article_list, article_detail, article_b_list, article_b_detail, ArticleAPIView, ArticleDetails, \
    ArticleGAList, ArticleGADetail, ArticleViewSet, ArticleGenViewSet, ArticleMVSet, ArticleGAJwtList
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('gvs-article', ArticleGenViewSet, basename='gvs-article')
router.register('mvs-article', ArticleMVSet, basename='mvs-article')

urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>/', article_detail),
    path('article-b/', article_b_list),
    path('detail-b/<int:pk>/', article_b_detail),
    path('article-c/', ArticleAPIView.as_view()),
    path('detail-c/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/', ArticleGAList.as_view()),
    path('generic/article/<int:id>/', ArticleGADetail.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('generic/articlejwt/', ArticleGAJwtList.as_view()),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
