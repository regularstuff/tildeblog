from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LearningForm


def landing_page(request):
    return render(
        request,
        "til/landing.html",
        context={
            "title": "ABC - Always be learning",
            "learnings": [
                {
                    "url": "https://x.y",
                    "headline": "placheholder 1",
                    "tags": ["tag1", "tag2", "tag3"],
                },
                {
                    "url": "https://xx.yy",
                    "headline": "placheholder 2",
                    "tags": ["tag11", "tag12", "tag13"],
                },
            ],
        },
    )


def learning_data_entry(request):
    if request.method == "GET":
        context = {"page_title": "Learning Data Entry Form"}
        context["learning_form"] = LearningForm()
        return render(request, template_name="til/learning.html", context=context)
    if request.method == "POST":
        learning_form = LearningForm(request.POST)
        if learning_form.is_valid():
            learning_form.save()
            return HttpResponseRedirect("")
    return HttpResponseRedirect("")
