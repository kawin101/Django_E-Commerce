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
# หากคุณต้องการให้ค้นหาข้อมูลโรงแรมด้วยเงื่อนไข "name" หรือ "address" ใน Django ORM คุณสามารถใช้ Q objects ร่วมกับ | (pipe) operator เพื่อรวมเงื่อนไขที่ต้องการ
from django.db.models import Q

# ผู้ใช้งานต้อง เข้าสู่ระบบก่อนใช้งานเว็บไซต์
@login_required(login_url='login') 
def searchWriter(request, writer):
    # ดึงข้อมูลผู้ใช้งานมาแสดงหน้าหลัก
    username = request.user.username

    # ดึงข้อมูลผู้ใช้งานปัจจุบัน
    products = Product.objects.filter(writer=writer)

    # ดึงข้อมูลหมวดหมู่ทั้งหมด
    categories = Category.objects.all()
    productCount = products.count()

    return render(request, "frontend/searchWriter.html", {
        'products': products,
        'categories': categories,
        'writer': writer,
        'productCount': productCount,
        'username': username,
    })

# ผู้ใช้งานต้อง เข้าสู่ระบบก่อนใช้งานเว็บไซต์
@login_required(login_url='login')  
# ฟังก์ชันค้นหาด้วย ชื่อโรงแรม หรือ ที่อยู่ เช่น ตำบล อำเภอ จังหวัด
def searchAddress(request):
    # ดึงข้อมูลผู้ใช้งานมาแสดงหน้าหลัก
    username = request.user.username

    categories = Category.objects.all()
    products = None  # กำหนดค่าเริ่มต้นให้เป็น None

    if request.method == "POST":
        searchAddress = request.POST.get('searchAddress', '')

        # ถ้าไม่มี if ค่อยตรวจสอบ ผลลัพธ์การค้นหาจะเป็น "จำนวนข้อมูลโรงแรมทั้งหมด"
        # ตรวจสอบว่า ผู้ใช้งาน ไม่ได้พิมพ์ข้อมูลในช่องค้นหา ให้แสดง ผลลัพธ์การค้นหาเป็น "0"
        if searchAddress:
            products = Product.objects.filter(Q(name__contains=searchAddress) | Q(address__contains=searchAddress))
            productsCount = products.count()
        else:
            productsCount = 0

        return render(request, "frontend/searchAddress.html", {
            'searchAddress': searchAddress,
            'products': products,
            'categories': categories,
            'productsCount': productsCount,
            'username': username,
        })
    else:
        return render(request, "frontend/searchAddress.html", {'categories': categories})

'''
    ฟังก์ชันค้นหาด้วย ชื่อโรงแรม หรือ ที่อยู่ เช่น ตำบล อำเภอ จังหวัด (ต้นฉบับ)
'''
# def searchAddress(request):
#     categories = Category.objects.all()

#     if request.method == "POST":
#         searchAddress = request.POST.get('searchAddress', '')
        
#         # ค้นหาข้อมูล ด้วย ชื่อโรงแรม 
#         # products = Product.objects.filter(name__contains=searchAddress)

#         # ค้นหาข้อมูล ด้วย ชื่อโรงแรม หรือ ที่อยู่
#         products = Product.objects.filter(Q(name__contains=searchAddress) | Q(address__contains=searchAddress))
#         # นับจำนวนผลลัพธ์การค้นหา
#         productsCount = products.count()

#         return render(request, "frontend/searchAddress.html", { 
#             'searchAddress': searchAddress,
#             'products': products,
#             'categories': categories,
#             'productsCount': productsCount,
#         })
#     else:
#         return render(request, "frontend/searchAddress.html", {'categories': categories})

# ผู้ใช้งานต้อง เข้าสู่ระบบก่อนใช้งานเว็บไซต์
@login_required(login_url='login')  
def searchCategory(request, cat_id):
    # ดึงข้อมูลผู้ใช้งานมาแสดงหน้าหลัก
    username = request.user.username
    # ดึงข้อมูลไอดีแต่ละจังหวัดที่อยู่ในตางรางข้อมูลโรงแรม
    products = Product.objects.filter(category_id = cat_id)
    # ดึงชื่อจังหวัดมาแสดงผล
    categoryName = Category.objects.get(id=cat_id)
    # ดึงข้อมูลของจังหวัดทั้งหมด
    categories = Category.objects.all()
    # นับจำนวนโรงแรมตาม category_id
    productCount = Product.objects.filter(category_id=cat_id).count()

    return render(request, "frontend/category.html", {
        'products': products,
        'categories': categories,
        'categoryName': categoryName,
        'productCount': productCount,
        'username': username,
    })

# ผู้ใช้งานต้อง เข้าสู่ระบบก่อนใช้งานเว็บไซต์
@login_required(login_url='login')
def product(request, pk):
    # ดึงข้อมูลผู้ใช้งานมาแสดงหน้าหลัก
    username = request.user.username
    product = Product.objects.get(id=pk)

    categories = Category.objects.all()
    return render(request, 'frontend/product.html', {
        'product': product,
        'categories': categories,
        'username': username,
        })

# ผู้ใช้งานต้อง เข้าสู่ระบบก่อนใช้งานเว็บไซต์
@login_required(login_url='login') 
def home(request):
    # ดึงข้อมูลผู้ใช้งานมาแสดงหน้าหลัก
    username = request.user.username
    # เรียงลำดับตามคีย์หลักตามลำดับจากมากไปน้อย หรือ ข้อมูลใหม่ ไป ข้อมูลเก่า
    products = Product.objects.all().order_by('-pk')
    
    # ดึงข้อมูลของจังหวัดทั้งหมด
    categories = Category.objects.all()
    # ดึงชื่อจังหวัดมาแสดงผล
    categoryName = Category.objects.all()

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
    # try:
    #     page = int(request.GET.get('page', '1'))
    # except ValueError:
    #     page = 1

    # try:
    #     product_per_page = paginator.get_page(page)
    # except (EmptyPage, InvalidPage):
    #     product_per_page = paginator.get_page(paginator.num_pages)

    try:
        page = request.GET.get('page', 1)
        product_per_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        product_per_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        product_per_page = paginator.page(paginator.num_pages)

    return render(request, 'frontend/home.html', {
        'products':product_per_page,
        'categories': categories,
        'categoryName': categoryName,
        'latest': latest,
        'username': username,
        })

# ผู้ใช้งานต้อง เข้าสู่ระบบก่อนใช้งานเว็บไซต์
@login_required(login_url='login')  
def about(request):
    return render(request, 'frontend/about.html', {})

'''
ระบบป้องกันผู้ใช้งานไม่ให้สามารถเข้าสู่ระบบแอดมินหลังบ้านมาแก้ไขข้อมูลได้โดยตรง
'''
def login_user(request):
    categories = Category.objects.all()
    
    # ตรวจสอบว่าผู้ใช้เคยเข้าสู่ระบบแล้วหรือไม่
    if request.user.is_authenticated:
        messages.error(request, ("ท่านเข้าสู่ระบบอยู่แล้ว...กรุณาออกจากระบบก่อนครับ!"))
        return redirect('home')

    #
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_superuser:  # ตรวจสอบว่าผู้ใช้เป็น admin หรือไม่
                return redirect('panel')  # ถ้าเป็น admin ให้เปลี่ยนเส้นทางไปหน้า panel
            else:
                messages.success(request, f"ยินดีต้อนรับท่าน {username} ท่านได้เข้าสู่ระบบแล้วเรียบร้อย!")
                return redirect('home')  # ถ้าไม่ใช่ admin ให้เปลี่ยนเส้นทางไปหน้าหลัก
        else:
            messages.error(request, ("เกิดข้อผิดพลาดกรุณาลองอีกครั้ง..."))
            return redirect('login')
    else:
        return render(request, 'frontend/login.html', {
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
            messages.success(request, f"ท่านได้สมัครสมาชิกเสร็จแล้วเรียบร้อย! {username} ยินดีต้อนรับครับ!")

            return redirect('home')
        else:
            messages.error(request, ("เกิดข้อผิดพลาด! เกิดปัญหาในการสมัครสมาชิก กรุณาลองใหม่อีกครั้ง......"))
            return redirect('register')
    else:
        return render(request, 'frontend/register.html', {
            'form':form,
            'categories': categories,
        })

'''
    ฟังก์ชันการเข้าสู่ระบบ (ต้นฉบับ)
'''

# def login_user(request):
#     # แสดงข้อมูลจังหวัดทั้งหมด เมื่ออยู่หน้า เข้าสู่ระบบ
#     categories = Category.objects.all()

#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, ("ยินดีต้อนรับ ท่านได้เข้าสู่ระบบแล้วเรียบร้อย!"))
#             return redirect('home')
#         else:
#             messages.success(request, ("เกิดข้อผิดพลาดกรุณาลองอีกครั้ง..."))
#             return redirect('login')

#     else:
#         return render(request, 'login.html', {
#             'categories': categories,
#         })

'''
ฟังก์ชันค้นหา จังหวัด สำรอง อยู่ในช่วงทดสอบ
ความต้องการ ให้แสดงข้อมูลการค้นหาล่าสุด ทั้งหมดของผู้ใช้งาน
**ทำอะไรได้บ้างแล้วตอนนี้? แสดงข้อมูลการค้นหาล่าสุด 1 สถานที่
'''
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
