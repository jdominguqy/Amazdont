from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from web.forms import NewUserForm, SearchForm
from web.models import Product
from .models import Product


def index(request):
    context = {}
    form = SearchForm(request.POST or None)
    context["form"] = form
    context["dataset"] = Product.objects.all().order_by("-id")[:2]
    return render(request, 'web/index.html', context)


def search(request):
    context = {}
    form = SearchForm(request.POST or None)
    context["form"] = form

    if request.method == "POST":
        if form.is_valid():
            context["dataset"] = Product.objects.all().filter(
                name=form.searchRequest)
            print(context)
    return render(request, 'web/search.html', context)


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
    context["products"] = Product.objects.filter(userId=request.user)
    return render(request, 'registration/profile.html', context)


def search(request):
    context = {}
    return render(request, 'web/search.html', context)
