from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
	now = datetime.datetime.now()
	html =  '<html><body>Agora sao: %s </body></html>' % now 
	return HttpResponse(html)

def hours_ahead(request,offset):
	try:
		offset = int(offset)
	except Exception, e:
		raise Http404()
	dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
	assert True
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)