from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
	now = datetime.datetime.now()
	return render(request,'current_date.html',{'current_date':now})

def hours_ahead(request,offset):
	try:
		offset = int(offset)
	except Exception, e:
		raise Http404()
	dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
	return render (request,'hours_ahead.html',{'hour_offset':offset,'next_time':dt})