
# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from shop.forms import ContactForm, EnquiryForm
from .models import Category, Product
from django.views.generic import TemplateView


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})

def enqView(request):
    if request.method =='GET':
        form1 = EnquiryForm()
    else:
        form1 = EnquiryForm(request.POST)

        if form1.is_valid():
            contact_name = form1.cleaned_data['contact_name']
            from_email = form1.cleaned_data['from_email']
            message = form1.cleaned_data['message']
            picked = form1.cleaned_data.get('picked')

            try:
                send_mail(contact_name, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "success.html")
    return render(request, "enq.html", {'form':form1})

def emailView(request):
    if request.method =='GET':
        form = ContactForm()

    else:
        form = ContactForm(request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            try:
                send_mail(contact_name, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, "success.html")
    return render(request, "email.html", {'form':form})

#def successView(request):
#    return render(request, "success.html")
