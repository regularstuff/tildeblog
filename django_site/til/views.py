from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LearningForm

from .models import Learned

from .tag_utils import TagHelper


def show(request, learnt_id):
    learnt = Learned.objects.get(id=learnt_id)
    body = learnt.content
    title = learnt.title
    page_title = "placeholder123"
    tldr = learnt.tldr
    tags = learnt.tags
    context = {
        "learn_title": title,
        "learnt_content": body,
        "learnt_tldr": tldr,
        "learnt_tags": tags,
        "page_title": page_title,
    }

    return render(request, template_name="til/display_learnt.html", context=context)


def landing_page(request):
    mylearnings = Learned.objects.all()
    learnt_things = []
    for learnt in mylearnings:
        headline = learnt.title
        tag_id = learnt.id
        tags = []
        for tag in learnt.tags.all():
            tags.append(tag.name)
        item = {"headline": headline, "id": tag_id, "tags": tags}
        learnt_things.append(item)
    return render(
        request,
        "til/landing.html",
        context={"title": "ABC: Always Be Learning", "learnings": learnt_things},
    )


def learning_data_entry(request):
    if request.method == "GET":
        context = {
            "page_title": "Learning Data Entry Form",
            "learning_form": LearningForm(),
        }
        return render(request, template_name="til/learning.html", context=context)
    if request.method == "POST":
        learning_form = LearningForm(request.POST)
        if learning_form.is_valid():
            learnt_object = learning_form.save()
            delimited_tags = learning_form.cleaned_data["delimited_tag_field"].strip()
            if delimited_tags:
                helper = TagHelper(delim=",")
                helper.tags = delimited_tags(delimited_tags, learnt_object.id)
            return render(request, "til/post_thanks.html")
    return HttpResponseRedirect("")
