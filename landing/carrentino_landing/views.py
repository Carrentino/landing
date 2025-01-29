from django.shortcuts import render
from .forms import ApplicationForm


def landing_page(request):
    form = ApplicationForm()
    success = False

    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            success = True

    return render(request, "landing.html", {"form": form, "success": success})