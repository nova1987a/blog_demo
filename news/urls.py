from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

#from rest_framework import renderers
#from rest_framework.urlpatterns import format_suffix_patterns


#router = DefaultRouter()

#router.register(r'report', views.ReportList, basename = 'report')
#urlpatterns = router.urls

#report = views.ReportViewSet.as_view({
#	'get': 'list',
#	'post': 'create'
#})
urlpatterns = [
	path('', views.ReportList.as_view(), name='report'),
	path('render_js/', views.render_js, name='render_js'),
	path('report_json/', views.report_lst, name='report_json'),
	path('report_json/<int:pk>', views.report_detail, name='report_detail'),
]
