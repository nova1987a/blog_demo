from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import ReportSerializer
from .models import Report
from django.views.decorators.csrf import csrf_exempt 


# Create your views here.


class ReportAPIView(APIView):
	def get_object(self, pk):
		report = get_object_or_404(Report, pk=pk)
		return report
	def get(self, request, *args, **kwargs):
		pk = self.kwargs['pk']
		report = self.get_object(pk)
		serializer = ReportSerializer(report)
		return Response(serializer.data)



class ReportList(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'report_api.html'

	def get(self, request):
		queryset = Report.objects.all()
		return Response({'reports': queryset})

@csrf_exempt
def report_lst(request):
	"""A view returning all in list """
	reports = Report.objects.all()
	serializer = ReportSerializer(reports, many=True)
	serializer_data = {"data": serializer.data}
	return JsonResponse(serializer_data, safe=False)

def report_detail(request, pk):
	""" Retrive a code of report"""
	try:
		report = Report.objects.get(pk=pk)
	except Report.DoesNotExist:
		return HttpResponse(status=404)

	serializer = ReportSerializer(report)
	return JsonResponse(serializer.data)

def render_js(request):
	return render(request, 'json2js.html')

