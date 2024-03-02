from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LearningForm

from .models import Learned


def landing_page(request):
    mylearnings = Learned.objects.all()
    learnt_things = [
        {"headline": x.title, "url": f"https://x/{x.id}", "tags": [1, 2, 3]}
        for x in mylearnings
    ]

    return render(
        request,
        "til/landing.html",
        context={"title": "ABC: Always Be Learning", "learnings": learnt_things},
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
            return render(request, 'til/post_thanks.html')
    return HttpResponseRedirect("")