from django.shortcuts import render
from .models import*
from . form import*
from django.core.paginator import Paginator
from .filters import*

# Create your views here.


def test(request):
    if request.method == 'post':
        form = TestForm(request.POST)
    else:
        form = TestForm()
    context = {'form':form}
    return render(request, 'test.html', context)

def category_view(request):
    page_number = request.GET.get('page')
    filter = CategoryFilter(request.GET, queryset=category.objects.all())
    categories = filter.qs
    paginator = Paginator(categories, 3)
    page = paginator.get_page(page_number)   
    
    if request.method == 'POST':
        form = categoryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = categoryForm()
    context = {'form':form, 'page':page}
    return render(request, 'category.html', context)

def unit_view(request):
    units = unit.objects.all()
    if request.method == 'POST':
        form = unitForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = unitForm()
    context = {'form':form, 'uts':units}    
    return render(request, 'unit.html', context)

def  item_view(request):
    page_number = request.GET.get('page')
    filter = ItemFilter(request.GET, queryset=item.objects.all())
    items = filter.qs
    paginator = Paginator(items, 3)
    page = paginator.get_page(page_number)
    

    if request.method == 'POST':
        form = itemForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = itemForm()
    context = {'form':form, 'page':page}
    return render (request,'item.html',context)    
        
def supplier_view(request):
    suppliers =supplier.objects.all()
    if request.method == 'POST':
        form = supplierForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = supplierForm()
    context ={'form':form, 'supplrs':suppliers}
    return render(request,'supplier.html',context)
        
def Order_view(request):
     orders =Order.objects.all()
     if request.method == 'POST':
         form = orderForm(request.POST)
         if form.is_valid():
            form.save()

     else:
         form = orderForm()    
         context = {'form':form, 'ordrs':orders}
         return render(request,'order.html',context)    

def employee_view(request):
    employees = Employee.objects.all()
    if request.method == 'POST':
     form = EmployeeForm(request.POST)
     if form.is_valid():
            form.save()

    else:
        form = EmployeeForm()
    context ={'form':form, 'employs':employees}
    return render (request,'employee.html',context)       

