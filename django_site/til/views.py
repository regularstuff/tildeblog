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
        "learnt_id": learnt_id,
        "learnt_title": title,
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


def learning_data_entry(request, learnt_id=None):
    learnt = None
    tag_string = ""
    if learnt_id is not None:
        learnt = Learned.objects.get(id=learnt_id)
        tag_helper = TagHelper(delim=",")
        tag_string = tag_helper.tags_as_delim_string(learnt.id)
    if request.method == "GET":
        context = {"page_title": "Learning Data Entry Form"}
        context["learning_form"] = LearningForm(
            instance=learnt, initial={"delimited_tag_field": tag_string}
        )
        return render(request, template_name="til/learning.html", context=context)
    if request.method == "POST":
        learning_form = LearningForm(request.POST, instance=learnt)
        if learning_form.is_valid():
            learnt_object = learning_form.save()
            delimited_tags = learning_form.cleaned_data["delimited_tag_field"].strip()
            if delimited_tags:
                helper = TagHelper(delim=",")
                helper.tags = helper.set_tags_on_learnt(
                    delimited_tags, learnt_object.id
                )
            return render(request, "til/post_thanks.html")
    return HttpResponseRedirect("")
