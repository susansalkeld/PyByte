# Create your views here.
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('books/index.html',
                                context_instance=RequestContext(request))

