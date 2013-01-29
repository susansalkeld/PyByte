# Create your views here.
from django.shortcuts import render_to_response
from blog.models import Entry
from django.template import RequestContext

def index(request):
    entry_info = Entry.objects.all()
    return render_to_response('blog/preview.html',
                                {'entries':entry_info},
                                context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html',
                                context_instance=RequestContext(request))

def main(request):
    return render_to_response('landing.html',
                                 context_instance=RequestContext(request))

def entry(request, entry_id):
    entry_info = Entry.objects.get(id=entry_id)
    return render_to_response('blog/entry.html',
                                {'entry':entry_info},
                                 context_instance=RequestContext(request))

