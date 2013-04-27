from django.http import HttpResponse
from django.template import Template, Context
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
	now = datetime.datetime.now()
	template = Template('<html><body>It is now: {{current_date}} </body></html>');
	html =   template.render(Context({'current_date':now}))
	return HttpResponse(html)

def hours_ahead(request,offset):
	try:
		offset = int(offset)
	except Exception, e:
		raise Http404()
	dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)