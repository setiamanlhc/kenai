from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def index(request):
    return render_to_response("web//index.html",'',context_instance=RequestContext(request))
    #return HttpResponse("web//index.html")

def smsbroadcast(request):
    return render_to_response("web/smsbroadcast.html",'',context_instance=RequestContext(request))

def services(request):
    return render_to_response("web/services.html",'',context_instance=RequestContext(request))

def webmobile(request):
    return render_to_response("web/webmobile.html",'',context_instance=RequestContext(request))

def contact(request):
    return render_to_response("web/contact.html",'',context_instance=RequestContext(request))
