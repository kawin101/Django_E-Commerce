# การแสดงผลหน้าเว็บ html และ การนำทางไป urls.py ต่างๆ ในโปรเจ็ค
from django.shortcuts import render, redirect
# นำเข้าข้อมูลใน Product และ Category มาใช้งาน
from store.models import Product, Category
'''
นำเข้าคลาส User จากโมดูล การจัดการข้อมูลของผู้ใช้งานในระบบ 
ใช้คลาส User เพื่อดึงข้อมูลผู้ใช้งาน เพิ่ม ลบ และแก้ไขข้อมูลผู้ใช้งานในระบบ Django 
'''
from django.contrib.auth.models import User
# ตรวจสอบให้เข้าสู่ะระบบก่อน เข้าใช้งานเว็บไซต์
from django.contrib.auth.decorators import login_required
# ส่งข้อความแจ้งเตือน กลับไปหน้าแสดงผล
from django.contrib import messages
# ตรวจสอบชนิดไฟล์ข้อมูลที่อัพโลหลด
from django.core.files.storage import FileSystemStorage
# ตรวจสอบผู้เข้าใช้งานระบบ
from django.contrib.auth.models import auth

def insertData(request):
    # ตรวจสอบคำขอว่าเป็นการเพิ่มข้อมูลไปยังเซิฟเวอร์และตัวแปรไฟล์รูปภาพ
    if request.method == "POST" and request.FILES["image"]:
        # สร้างตัวแปร เก็บข้อมูลรูปภาพ
        datafile = request.FILES["image"]

        '''
            รับข้อมูลจากหน้าเพิ่มข้อมูลโรงแรม
        '''
        # รหัสตำแหน่งโรงแรม
        place_id = request.POST["place_id"]
        # ชื่อโรงแรม
        name = request.POST["name"]
        # ที่อยู่
        address = request.POST["address"]
        # เบอร์โทร
        phone_number = request.POST["phone_number"]
        # ละติจูด
        latitude = request.POST["latitude"]
        # ลองติจูด
        longitude = request.POST["longitude"]
        # รูปภาพโรงแรมแบบ URL
        first_photo_url = request.POST["first_photo_url"]
        # จังหวัด
        category = request.POST["category"]
        # ตำแหน่งบนแผนที่
        map_url = request.POST["map_url"]
        # เว็บไซต์โรงแรม
        website = request.POST["website"]
        # ดึงข้อมูลชื่อ username ปัจจุบันที่ใช้งานมาแสดง
        writer = auth.get_user(request)

        # ตรวจสอบว่าข้อมูลที่ส่งเข้ามาเป็นประเภทรูปภาพ
        if str(datafile.content_type).startswith("image"):
            # อัพโหลด
            fs = FileSystemStorage()
            # ส่งรูปภาพที่อัพโหลดมา ไปเก็บที่โฟลเดอร์ที่กำหนดไว้
            img_url = "uploads/product/"+datafile.name
            # บันทึกรูปภาพลงเครื่อง
            filename = fs.save(img_url, datafile)

            '''
                บันทึกข้อมูลโรงแรม
            '''
            
            product = Product(
                place_id = place_id,
                name = name,
                address = address,
                phone_number = phone_number,
                latitude = latitude,
                longitude = longitude,
                first_photo_url = first_photo_url,
                category_id = category,
                map_url = map_url,
                website = website,
                image = img_url,
                writer = writer,
            )

            product.save()

            # แสดงข้อมูลแจ้งเตือนกลับไปหาผู้ดูแลระบบ
            messages.success(request, "บันทึกข้อมูลเสร็จเรียบร้อยแล้วครับ")

            # ทำงานเสร็จ กลับไปหน้าเพิ่มข้อมูลโรงแรม
            return redirect("displayForm")
        else:
            # แสดงข้อมูลแจ้งเตือนกลับไปหาผู้ดูแลระบบ
            messages.error(request, "ประเภทไฟล์ที่อัพโหลดไม่รองรับ กรุณาอัพโหลดเป็นไฟล์รูปภาพใหม่อีกครั้งครับ")
            # ทำงานเสร็จ กลับไปหน้าเพิ่มข้อมูลโรงแรม
            return redirect("displayForm")

'''
    ฟังก์ชันแสดงหน้าเพิ่มข้อมูลโรงแรม
'''
# ผู้ดูแลระบบต้อง เข้าสู่ระบบก่อนใช้งานเว็บไซต์
@login_required(login_url='login') 
def displayForm(request):
    # ดึงข้อมูลชื่อ username ปัจจุบันที่ใช้งานมาแสดง
    # current_user = request.user
    writer = auth.get_user(request)

    # ข้อมูลโรงแรมทั้งหมดมาแสดง
    products = Product.objects.all()
    # นับจำนวนโรงทั้งหมดที่มีในฐานข้อมูล
    productCount = Product.objects.count()
    # ข้อมูลจังหวัดทั้งหมดมาแสดง
    categories = Category.objects.all()

    return render(request, 'backend/productForm.html', {
        "products": products,
        "productCount": productCount,
        "categories": categories,
        "writer": writer,
        # "current_user": current_user,
    })

'''
    ฟังก์ชันแสดงหน้าแผงควบคุม
'''
# ผู้ดูแลระบบต้อง เข้าสู่ระบบก่อนใช้งานเว็บไซต์
@login_required(login_url='login') 
def panel(request):
    # ตรวจสอบว่าเป็นผู้ดูแลระบบหรือไม่? ถ้าใช้ให้ทำงานต่อไป
    if request.user.is_superuser:
        # ดึงข้อมูล username ปัจจุบันมาแสดง
        # current_user = request.user
        writer = auth.get_user(request)

        # ข้อมูลจังหวัดทั้งหมดมาแสดง
        products = Product.objects.all()
        # นับจำนวนโรงทั้งหมดที่มีในฐานข้อมูล
        productCount = Product.objects.count()
        return render(request, 'backend/home.html', {
            "products": products,
            "productCount": productCount,
            "writer": writer,
            # "current_user": current_user,
        })
    else:
        # แจ้งเตือนกลับไปยังหน้าหลัก ว่า username ที่คุณใช้ไม่ใช้ผู้ดูแลระบบ
        messages.error(request, ("ท่านไม่ได้รับอนุญาต เฉพาะผู้ดูแลระบบเท่านั้น!"))
        # นำทางกลับไปยังหน้าเข้าสู่ระบบ
        return redirect('login')

'''
    ฟังก์ชันแสดงหน้าแผงควบคุม ต้นฉบับ
'''
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
