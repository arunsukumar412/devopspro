from django.shortcuts import render
# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader

def r(request):
    template = loader.get_template('recipe.html')
    return HttpResponse(template.render({},request))



