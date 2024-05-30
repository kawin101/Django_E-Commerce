from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseForbidden
# เป็นคำสั่งใน Python ที่ใช้ในโปรเจกต์ Django เพื่อให้กลายเป็น decorator (ตกแต่งฟังก์ชัน) ที่ต้องการผู้ใช้เข้าสู่ระบบก่อนที่จะทำงานในหน้า view นั้น ๆ
from django.contrib.auth.decorators import login_required


# ผู้ใช้งานต้อง เข้าสู่ระบบก่อนใช้งานเว็บไซต์
@login_required(login_url='login') 
def cart_summary(request):
    # ดึงข้อมูลผู้ใช้งานมาแสดงหน้าหลัก
    username = request.user.username

    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods()

    navigate_message = ""
    google_maps_url = ""

    if request.method == 'POST':
        if 'navigate' in request.POST:
            # รับค่าสถานที่ 1 และสถานที่ 2 จาก request.POST
            location1 = request.POST.get('location1', '')
            location2 = request.POST.get('location2', '')

            # นำทางผู้ใช้ไปยังสถานที่ปลายทาง (ตัวอย่างเช่นการแสดงผลในที่นี้เป็นการสร้างลิงก์ URL)
            # navigate_message = f"กำลังนำทางจาก {location1} ไปยัง {location2}"
            navigate_message = f"กำลังนำทางจาก <strong>{location1}</strong> ไปยัง <strong>{location2}</strong>"
            google_maps_url = f"https://www.google.com/maps/dir/{location1}/{location2}"

        else:
            return HttpResponseForbidden("Invalid request")

    return render(request, "cart_summary.html", {
        "cart_products": cart_products,
        "username": username,
        "navigate_message": navigate_message,
        "google_maps_url": google_maps_url,
    })

'''
    ฟังก์ชันนับจำนวนโรงแรมโดนใจทั้งหมด (ทำงานได้ แต่ต้องปรับปรุง)
'''
# def cart_summary(request):
#     # ดึงข้อมูลผู้ใช้งานมาแสดงหน้าหลัก
#     username = request.user.username

#     # Get the cart
#     cart = Cart(request)
#     cart_products = cart.get_prods()

#     navigate_message = ""
#     google_maps_url = ""

#     if request.method == 'POST':

#         # รับค่าสถานที่ 1 และสถานที่ 2 จาก request.POST
#         location1 = request.POST.get('location1', '')
#         location2 = request.POST.get('location2', '')

#         # นำทางผู้ใช้ไปยังสถานที่ปลายทาง (ตัวอย่างเช่นการแสดงผลในที่นี้เป็นการสร้างลิงก์ URL)
#         navigate_message = f"กำลังนำทางจาก {location1} ไปยัง {location2}"
#         google_maps_url = f"https://www.google.com/maps/dir/{location1}/{location2}"
            
#     return render(request, "cart_summary.html", {
#         "cart_products": cart_products,
#         "username": username,
#         "navigate_message": navigate_message,
#         "google_maps_url": google_maps_url,
#     })


'''
    ฟังก์ชันนับจำนวนโรงแรมโดนใจทั้งหมด (ต้นฉบับ)
'''
# def cart_summary(request):
#     # ดึงข้อมูลผู้ใช้งานมาแสดงหน้าหลัก
#     username = request.user.username

#     # Get the cart
#     cart = Cart(request)
#     cart_products = cart.get_prods

#     return render(request, "cart_summary.html", {
#         "cart_products": cart_products,
#         "username": username,
#     })

# ผู้ใช้งานต้อง เข้าสู่ระบบก่อนใช้งานเว็บไซต์
@login_required(login_url='login') 
def cart_add(request):
    # Get the cart
    cart = Cart(request)
    # test for POST
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        
        # lookup product in DB
        product = get_object_or_404(Product, id=product_id)

        # Save to session
        cart.add(product=product)

        # Get Cart Quantity
        cart_quantity = cart.__len__()

        # Return resonse
        # response = JsonResponse({'ชื่อโรงแรม: ': product.name})
        # จำนวนโรงแรมโดนใจ
        response = JsonResponse({'qty': cart_quantity})

        return response

# ผู้ใช้งานต้อง เข้าสู่ระบบก่อนใช้งานเว็บไซต์
@login_required(login_url='login') 
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        # Get stuff
        product_id = int(request.POST.get('product_id'))
        # Call delete Function in Cart
        cart.delete(product=product_id)

        response = JsonResponse({'product':product_id})
        # return redirect('cart_summary')
        return response

def cart_update(request):
    pass
