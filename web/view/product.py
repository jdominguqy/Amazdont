from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from web.forms import ProductForm
from web.models import ProductModel


def create_view(request: HttpRequest) -> HttpResponse:
    context = {}
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'web/product/create.html', context)


def list_view(request: HttpRequest):
    context = {}
    context["dataset"] = ProductModel.objects.all()
    return render(request, "web/product/list.html", context)


def detail_view(request: HttpRequest, id):
    context = {}
    context["data"] = ProductModel.objects.get(id=id)
    return render(request, "web/product/details.html", context)


def update_view(request: HttpRequest, id):
    context = {}
    obj = get_object_or_404(ProductModel, id=id)
    form = ProductForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("web:product_details", id=id)

    context["form"] = form
    return render(request, "web/product/update.html", context)


def delete_view(request, id):
    context = {}
    obj = get_object_or_404(ProductModel, id=id)

    if request.method == "POST":
        obj.delete()
        return redirect("web:product_getAll")

    return render(request, "web/product/delete.html", context)
