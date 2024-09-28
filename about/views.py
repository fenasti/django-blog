from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


# Create your views here.


def about_views(request):

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS,
             "Collaboration request received! I endeavor to respond within 2 working days."
             )

    about = About.objects.order_by('-updated_on').first()

    collaborate_form = CollaborateForm()
    
#    about = get_object_or_404(queryset, updated_on=updated_on)

    return render(
        request,
        "about/about.html",
        {"about": about,
        "collaborate_form": collaborate_form,
        },
    )

