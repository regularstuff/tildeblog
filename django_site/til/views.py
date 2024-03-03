from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LearningForm


def learning_data_entry(request):
    if request.method == "GET":
        context = {"page_title": "Learning Data Entry Form"}
        context["learning_form"] = LearningForm()
        return render(request, template_name="til/learning.html", context=context)
    if request.method == "POST":
        learning_form = LearningForm(request.POST)
        if learning_form.is_valid():
            learning_form.save()
            return render(request, 'til/post_thanks.html')
    return HttpResponseRedirect("")