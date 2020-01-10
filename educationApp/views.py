from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from educationApp.models import Datas
from educationApp.services import NameMatcherService, DataService
from django.views.decorators.http import require_http_methods
from django.template.loader import render_to_string
import json
@csrf_exempt
@require_http_methods(["POST"])
def search(request):
    words = request.POST.get('search')
    dataService = DataService()
    datas = dataService.getAllIndex(words)
    render = render_to_string('education_data_list.html',{'datas': datas})
    return HttpResponse(render)

@require_http_methods(["GET"])
def getDatas(request):
    dataService = DataService()
    datas = dataService.getDatas(request.GET['name'])
    render = render_to_string('education_data.html', {'datas': datas.datas})
    return HttpResponse(render)

@require_http_methods(["GET"])
def index(request):
    render = render_to_string('search.html')
    return HttpResponse(render)

