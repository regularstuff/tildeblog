from django.shortcuts import render


def learning_data_entry(request):
    context = {"page_title": "Learning Data"}
    return render(request, template_name="til/learning.html")
