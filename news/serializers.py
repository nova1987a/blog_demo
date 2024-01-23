from rest_framework import serializers
from .models import Report 

class ReportSerializer(serializers.ModelSerializer):
	title = serializers.CharField(max_length=100)
	content = serializers.CharField()
	created_on = serializers.DateTimeField()

	class Meta:
		model = Report 
		fields = ['title', 'content', 'created_on', 'author']
