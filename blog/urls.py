#from blog.viewsets import ArticleViewSet
#from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path

#router = DefaultRouter()
#router.register(r'articles', ArticleViewSet, basename='article')
#urlpatterns = router.urls
urlpatterns = [
#    path('', views.BlogList.as_view(), name='home'),
    path('', views.blog_list),
    path('blog/<int:pk>', views.BlogDetail.as_view(), name='blog_detail'),
#    path('lottery', views.get_random),
]
