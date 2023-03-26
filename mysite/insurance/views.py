from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    html_content = "<html><body><h1>Hello, world!</h1></body></html>"
    return HttpResponse(html_content)

def my_template_view(request):
    context = {'name': 'World'}
    return render(request, 'my_template.html', context)

def survey(request):
    return render(request, 'survey.html')