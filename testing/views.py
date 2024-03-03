# from django.shortcuts import render
# from django.http import HttpResponse
# from testing.models import addData

# # Create your views here.

# def addQ(request):
#     if request.method == 'POST':
#         name= request.POST.get('name')
#         country= request.POST.get('country')
#         price= request.POST.get('price')
#         enter = addData(name=name, country=country,price=price)
#         enter.save()
#     return render(request, "about.html")

from django.shortcuts import render,redirect,get_object_or_404
from django.db import IntegrityError
from .models import addData,Product
from django.conf import settings
from .forms import updateProduct


def addQ(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        country = request.POST.get('country')
        price = request.POST.get('price')

        # Check if an object with the same name already exists
        existing_object = addData.objects.filter(name=name).first()

        if existing_object:
            # Duplicate found, handle accordingly (e.g., display an error message)
            return render(request, 'demo.html', {'message': 'Entry with this name already exists.'})

        try:
            # No duplicate found, save the new object
            new_entry = addData(name=name, country=country, price=price)
            new_entry.save()
            return render(request, 'about.html', {'message': 'Entry added successfully.'})

        except IntegrityError as e:
            # Handle other integrity errors as needed
            return render(request, 'demo.html', {'message': 'An error occurred: {}'.format(str(e))})

    else:
        # Handle GET requests or render the form
        return render(request, 'about.html')


def demo(request):
    return render(request, "editproduct.html")

def trial(request):
    return render(request, "adminview.html")


def edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'edit.html', {'product': product})


def product_list(request):
    # Retrieve all products from the database
    products = Product.objects.all()

    # Pass the products to the template
    return render(request, 'adminview.html', {'products': products})

def product_list_shop(request):
    # Retrieve all products from the database
    products = Product.objects.all()

    # Pass the products to the template
    return render(request, 'shop.html', {'products': products})



def addProduct(request):
    n=''
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        catagory = request.POST.get('catagory')
        brand = request.POST.get('brand')
        country = request.POST.get('country')
        quantity = request.POST.get('quantity')
        rating = request.POST.get('rating')
        picture = request.FILES.get('picture')
        description = request.POST.get('description')

        # Save the data to the database
        Product.objects.create(
            name=name,
            price=price,
            catagory=catagory,
            brand=brand,
            country=country,
            quantity=quantity,
            rating = rating,
            img=picture,
            description=description
        )
        
        n="Added"
        return redirect('product') 
        # return render(request, 'editproduct.html',{'n':n})
        # return redirect('success_page')  # Redirect to a success page or another view
    
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('product') 
   




# def update_product(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
    
#     if request.method == 'POST':
#         form = updateProduct(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             # Redirect or do something else upon successful update
#     else:
#         form = updateProduct(instance=product)

#     return render(request, 'adminview.html', {'form': form, 'product': product})



def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        name = request.POST.get('name',product.name)
        price = request.POST.get('price',product.price)
        catagory = request.POST.get('catagory',product.catagory)
        brand = request.POST.get('brand',product.brand)
        country = request.POST.get('country',product.country)
        quantity = request.POST.get('quantity',product.quantity)
        picture = request.FILES.get('picture',product.img)
        description = request.POST.get('description',product.description)

        # if picture:
        #     picture_url = f"{settings.MEDIA_URL}{picture.name}"
        # else:
        #     picture_url = product.img.url

        Product.objects.filter(id=product_id).update(
            name=name,
            price=price,
            catagory=catagory,
            brand=brand,
            country=country,
            quantity = quantity,
            img=f"{settings.MEDIA_URL}{picture}",
            description=description
        )
    
        
            
        return redirect('product')
    # else:
    #     form = ProductForm(instance=product)

    # return render(request, 'update_price.html', {'form': form, 'product_id': product_id})



    





