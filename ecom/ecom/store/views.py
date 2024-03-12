from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
from .forms import SearchForm
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# เป็นคำสั่งใน Python ที่ใช้ในโปรเจกต์ Django เพื่อให้กลายเป็น decorator (ตกแต่งฟังก์ชัน) ที่ต้องการผู้ใช้เข้าสู่ระบบก่อนที่จะทำงานในหน้า view นั้น ๆ
from django.contrib.auth.decorators import login_required


# ค้นหาจังหวัดด้วยชื่อ ต้องกรอก ชื่อเมื่อค้นหาทุกจังหวัด เสียเวลา วนลูป id จังหวัดรวดเร็วกว่า
# def category(request, foo):
#     # Replace Hyphens with Spaces
#     foo = foo.replace('-', ' ')
#     # Grab the category from the url
#     try:
#         # Look Up The Category
#         category = Category.objects.get(name=foo)
#         products = Product.objects.filter(category=category)
#         return render(request, 'category.html', {'products':products, 'category':category})
#     except:
#         messages.success(request, ("That Category Doesn't Exist..."))
#         return redirect('home')

# 'login' คือชื่อของ URL pattern สำหรับหน้า login ของคุณ
@login_required(login_url='login')  
# ค้นหาด้วยชื่อโรงแรมและแสดงการค้นหาล่าสุด 1 โรงแรม
def search_view(request):
    recent_searches = []  # Implement logic to retrieve recent searches from a database
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            products = Product.objects.filter(name__icontains=search_query)
            # Implement logic to store recent searches in the database
            recent_searches.append(search_query)
    else:
        form = SearchForm()
        products = []

    return render(request, 'search.html', {'form': form, 'products': products, 'recent_searches': recent_searches})

# 'login' คือชื่อของ URL pattern สำหรับหน้า login ของคุณ
@login_required(login_url='login')  
# ฟังก์ชันค้นหาโรงแรมด้วยชื่อ เช่น "ก" จะแสดงชื่อโรงแรมทั้งหมดที่มีตัวอักษรด้วย "ก"
def searchAddress(request):
    categories = Category.objects.all()

    if request.method == "POST":
        searchAddress = request.POST.get('searchAddress', '')
        # ค้นหาข้อมูล ด้วย ชื่อโรงแรม 
        products = Product.objects.filter(name__contains=searchAddress)

        return render(request, "searchAddress.html", { 
            'searchAddress': searchAddress,
            'products': products,
            'categories': categories,
        })
    else:
        return render(request, "searchAddress.html", {'categories': categories})

# 'login' คือชื่อของ URL pattern สำหรับหน้า login ของคุณ
@login_required(login_url='login')  
def searchCategory(request, cat_id):
    products = Product.objects.filter(category_id = cat_id)

    categoryName = Category.objects.get(id=cat_id)
    categories = Category.objects.all()

    return render(request, "category.html", {
        'products': products,
        'categories': categories,
        'categoryName': categoryName,
    })

# 'login' คือชื่อของ URL pattern สำหรับหน้า login ของคุณ
@login_required(login_url='login')  
def product(request, pk):
    product = Product.objects.get(id=pk)

    categories = Category.objects.all()
    return render(request, 'product.html', {
        'product': product,
        'categories': categories,
        })

# 'login' คือชื่อของ URL pattern สำหรับหน้า login ของคุณ
@login_required(login_url='login')  
def home(request):
    # เรียงลำดับตามคีย์หลักตามลำดับจากมากไปน้อย
    products = Product.objects.all().order_by('-pk')
    categories = Category.objects.all()

    # if .order_by('pk') = 1,2,3,4
    # '-pk' = 4,3,2,1
    # [:2] แสดง 2 บทความล่าสุด
    latest = products[:6]  # ดึงข้อมูล 10 บล็อกล่าสุด

    # Pagination | จำนวนโรงแรมที่แสดงแต่ละหน้า เช่น หน้าละ 6 โรงแรม
    paginator = Paginator(products, 12)

    '''
    โค้ดด้านบนมีไวยากรณ์การจัดการหน้าเว็บแบบ pagination ใน Django:
    1. `page = int(request.GET.get('page', '1'))`: รับค่า `page` จาก URL 
    และแปลงเป็นจำนวนเต็ม, ถ้าไม่ระบุจะเป็น 1.
    2. `product = paginator.page(page)`: พยายามดึงข้อมูลหน้าเว็บที่ `page` จาก paginator.
    3. ถ้าหน้าที่กำหนดมีข้อมูล, `product` ถูกกำหนดเป็นหน้าที่กำหนดมา.
    4. ถ้าหน้าที่กำหนดไม่มีข้อมูลหรือไม่ถูกต้อง, `product_per_page` ถูกกำหนดเป็นหน้าสุดท้ายของ paginator.
    5. การใช้โค้ดนี้ช่วยจัดการการแสดงข้อมูลหน้าเว็บที่แบ่งหน้า (pagination) ใน Django 
    และป้องกันการเกิดข้อผิดพลาดเมื่อรับค่า `page` ที่ไม่ถูกต้องหรือหน้าที่ไม่มีข้อมูล.
    '''
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        product_per_page = paginator.get_page(page)
    except (EmptyPage, InvalidPage):
        product_per_page = paginator.get_page(paginator.num_pages)

    return render(request, 'home.html', {
        'products':product_per_page,
        'categories': categories,
        'latest': latest,
        })

# 'login' คือชื่อของ URL pattern สำหรับหน้า login ของคุณ
@login_required(login_url='login')  
def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    # แสดงข้อมูลจังหวัดทั้งหมด เมื่ออยู่หน้า เข้าสู่ระบบ
    categories = Category.objects.all()

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("ยินดีต้อนรับ ท่านได้เข้าสู่ระบบแล้วเรียบร้อย!"))
            return redirect('home')
        else:
            messages.success(request, ("เกิดข้อผิดพลาดกรุณาลองอีกครั้ง..."))
            return redirect('login')

    else:
        return render(request, 'login.html', {
            'categories': categories,
        })
 
def logout_user(request):
    logout(request)
    messages.success(request, ("ท่านได้ออกจากระบบแล้วเรียบร้อย...ขอบคุณที่ใช้งานเว็บไซต์ครับ..."))
    return redirect('home')

def register_user(request):
    # แสดงข้อมูลจังหวัดทั้งหมด เมื่ออยู่หน้า สมัครสมาชิก
    categories = Category.objects.all()

    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("ท่านได้สมัครสมาชิกเสร็จแล้วเรียบร้อย! ยินดีต้อนรับครับ!"))
            return redirect('home')
        else:
            messages.success(request, ("เกิดข้อผิดพลาด! เกิดปัญหาในการสมัครสมาชิก กรุณาลองใหม่อีกครั้ง......"))
            return redirect('register')
    else:
        return render(request, 'register.html', {
            'form':form,
            'categories': categories,
        })


