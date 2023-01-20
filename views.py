from django.shortcuts import HttpResponse, render
from product.models import Product, Review
import datetime

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def product_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        context = {
            'product': product
        }
        return render(request, 'product/product.html', context=context)


def product_detail_view(request, product_id):
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)
        review = Review.objects.filter(produc=product)
        print(review)

        context = {
            'product': product,
            'review': review

        }

        return render(request, 'product/detail.html', context=context)

def project(request):
    if request.method == 'GET':
        return HttpResponse('Hi! its my first project')

def good_bye(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user!')
def date(request):
    if request.method == 'GET':
        return HttpResponse(datetime.datetime.now().date)

