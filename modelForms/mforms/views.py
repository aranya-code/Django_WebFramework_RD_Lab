from django.shortcuts import render
from mforms.forms import modelFormCreation
from mforms.models import formCreation

def index(request):
    return render(request, 'mforms/index.html')

def proucts(request):
    productsList=formCreation.objects.all()
    return render(request, 'mforms/products.html', {'productsListView':productsList})

def addProduct(request):
    form = modelFormCreation()
    if request.method == 'POST':
        form = modelFormCreation(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request, 'mforms/addproduct.html',{'form':form})
