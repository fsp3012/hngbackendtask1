from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime

# Create your views here.

@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        slack_name = request.GET.get('slack_name')
        track = request.GET.get('track')
        utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        current_day = datetime.utcnow().strftime("%A")

        return Response({
            'slack_name': slack_name,
            'track': track,
            'utc_time': utc_time,
            'current_day': current_day,
            'github_file_url':'',
            'github_repo_url':'',
            'status_code':200
        })
