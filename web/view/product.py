from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from web.forms import ProductForm
from web.models import Product


@login_required
def create(request: HttpRequest) -> HttpResponse:
    context = {}
    form = ProductForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.userId = request.user
        obj.save()
        messages.success(request, "Product created correctly.")
        return redirect("web:index")

    context['form'] = form
    return render(request, 'web/product/create.html', context)


def list(request: HttpRequest):
    context = {}
    context["dataset"] = Product.objects.all()
    return render(request, "web/product/list.html", context)


def details(request: HttpRequest, id):
    context = {}
    context["data"] = Product.objects.get(id=id)
    return render(request, "web/product/details.html", context)


@login_required
def update(request: HttpRequest, id):
    context = {}
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.userId = request.user
        obj.save()
        return redirect("web:product_details", id=id)

    context["form"] = form
    return render(request, "web/product/update.html", context)


@login_required
def delete(request, id):
    context = {}
    obj = get_object_or_404(Product, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect("web:product_getAll")

    return render(request, "web/product/delete.html", context)
