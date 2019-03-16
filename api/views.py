from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def post_organisation(request):
    body_unicode = request.body.decode('utf-8')
    content = json.loads(body_unicode)
    print(content)
    print(content['name'])
    return JsonResponse({'success': True})