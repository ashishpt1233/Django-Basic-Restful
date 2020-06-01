
from django.urls import path ,include
from .views import article_list,article_detail,ArticleAPIView,Articledetails,GenericAPIView,ArticleViewSet
from rest_framework import DefaultRouter

router = DefaultRouter()
router.register('Article',ArticleViewSet,basename='article')

urlpatterns = [
    # path('Article/',article_list),
    path('viewset/',include(router.urls)),
    path('Article/',ArticleAPIView.as_view()),
    # path('detail/<int:pk>/',article_detail),
    path('detail/<int:id>/',Articledetails.as_view()),
    path('generic/Article/<int:id>/',GenericAPIView.as_view()),

]