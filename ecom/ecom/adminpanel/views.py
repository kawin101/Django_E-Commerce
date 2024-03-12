from django.shortcuts import render, redirect
from store.models import Product
'''
นำเข้าคลาส User จากโมดูล การจัดการข้อมูลของผู้ใช้งานในระบบ 
ใช้คลาส User เพื่อดึงข้อมูลผู้ใช้งาน เพิ่ม ลบ และแก้ไขข้อมูลผู้ใช้งานในระบบ Django 
'''
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='login') 
def panel(request):
    if request.user.is_superuser:
        current_user = request.user
        products = Product.objects.all()
        productCount = Product.objects.count()
        return render(request, 'backend/index.html', {
            "products": products,
            "productCount": productCount,
            "current_user": current_user,
        })
    else:
        messages.error(request, ("ท่านไม่ได้รับอนุญาต เฉพาะผู้ดูแลระบบเท่านั้น!"))
        return redirect('login')

# def panel(request):

#     # ดึงข้อมูลผู้ใช้ปัจจุบันที่ล็อกอินอยู่
#     current_user = request.user

#     products = Product.objects.all()
#     productCount = Product.objects.count()
#     return render(request, 'backend/index.html', {
#         "products": products,
#         "productCount": productCount,
#         "current_user": current_user,
#     })
