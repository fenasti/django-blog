from django.shortcuts import render, get_object_or_404
from .models import About

# Create your views here.


def about_views(request):

    about = About.objects.order_by('-updated_on').first()
#    about = get_object_or_404(queryset, updated_on=updated_on)

    return render(
        request,
        "about/about.html",
        {"about": about},
    )