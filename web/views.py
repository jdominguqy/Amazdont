from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('web/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def register(request):
    template = loader.get_template('web/register.html')
    context = {}
    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('web/login.html')
    context = {}
    return HttpResponse(template.render(context, request))


def create_product(request):
    template = loader.get_template('web/create_product.html')
    context = {}
    return HttpResponse(template.render(context, request))
