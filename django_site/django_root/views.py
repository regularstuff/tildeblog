from django.http import request
from django.shortcuts import render


def styx(request: request):
    cdict = {"sidebar": {"title": "Sidetitle"}, "content": {"title": "Love It here"}}
    return render(request, "settings/styx.html", context=cdict)
