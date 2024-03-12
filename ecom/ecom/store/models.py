from django.db import models
import datetime

# จังหวัดทั้งหมด ของ โรงแรม
# Categories of Products
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    #@daverobb2011
    class Meta:
        verbose_name_plural = 'categories'

# Customers
class Customer(models.Model):
    first_name = models.CharField(max_length=50, default='', blank=True, null=True)
    last_name = models.CharField(max_length=50, default='', blank=True, null=True)
    phone = models.CharField(max_length=10, default='', blank=True, null=True)
    email = models.EmailField(max_length=100, default='', blank=True, null=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# โรงแรมทั้งหมด
# All of our Products
class Product(models.Model):
    # ชื่อฐานข้อมูล myhotels
    place_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, default='', blank=True, null=True)
    phone_number = models.CharField(max_length=12, default='', blank=True, null=True)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    first_photo_url = models.CharField(max_length=800, default='', blank=True, null=True)
    # Province
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    map_url = models.CharField(max_length=800, default='', blank=True, null=True)
    website = models.CharField(max_length=800, default='', blank=True, null=True)
    uploadDate = models.DateField(auto_now_add=True)
    '''
    ค่าเริ่มต้น = 0
    ทศนิยม 2 ตำแหน่ง = 0.99 
    ค่าตัวเลขสูงสุด = 9999.99
    ถ้าต้องการ ค่าตัวเลข = 19999.99 ต้องเป็น max_digits=7
    '''
    # price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    # description = models.CharField(max_length=250, default='', blank=True, null=True)
    # image = models.ImageField(upload_to='uploads/product/')
    # Add Sale Stuff
    # is_sale = models.BooleanField(default=False)
    # sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name

# Customer Orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product

