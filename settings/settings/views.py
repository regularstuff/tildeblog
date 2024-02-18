from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.http import request

def styx(request: request):
    cdict = dict(sidebar=dict(title="Sidetitle"), content=dict(title="Love It here"))
    return render(request, 'settings/styx.html', context=cdict)
