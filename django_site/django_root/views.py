from django.http import HttpResponseRedirect
from django.shortcuts import render


def til_redirect(request):
    return HttpResponseRedirect("/til")


def styx(request):
    cdict = {"sidebar": {"title": "Sidetitle"}, "content": {"title": "Love It here"}}
    return render(request, "django_root/styx.html", context=cdict)
