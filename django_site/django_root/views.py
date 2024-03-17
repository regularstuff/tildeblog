from django.http import HttpResponseRedirect


def til_redirect(request):
    return HttpResponseRedirect("/til")
