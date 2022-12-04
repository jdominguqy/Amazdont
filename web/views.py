from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

from web.forms import NewUserForm
from web.models import Product


def index(request):
    context = {}
    context["dataset"] = Product.objects.all().order_by("-id")[:2]
    return render(request, 'web/index.html', context)


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("web:index")
        messages.error(
            request, form.errors)
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"form": form})


@login_required
def profile(request):
    context = {}
    return render(request, 'web/search.html', context)
