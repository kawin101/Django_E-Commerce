# Django_E-Commerce Docs | How to install this project.

** Download Python Version: 3.11.2 | 64 bit for Windows 10
- https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe

## Create database on phpMyAdmin
- Open your XAMPP and then click 'Admin' button rows of MySQL
- Database name: myhotels
- type: utf8_general_ci

## Make a new dir
cd to dir 
### # สร้างตัวจำลองสภาพแวดล้อมของภาษา Python
pip install -m venv virt | python -m venv virt
mkdir floder to keep your file
clone repository to new directory

/c/Django_E-Commerce/
- ecom
- virt
and cd ecom/
/c/Django_E-Commerce/ecom

## Setup

python -m venv virt

### # เปิดใช้งานตัวจำลองสภาพแวดล้อมของ Django Python
source virt/Scripts/activate

### # ตรวจสอบเครื่องมือ
pip freeze | pip list

### # ติดตั้งเครื่องมือ ไฟล์ requirements อยู่ในโฟลเดอร์เดียวกับ manage.py
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

### # Create Super User before run project | Please, Open Git base on VS CODE Terminal for easy way.
python manage.py createsuperuser
- username: admin
- password: password
anythings else is empty.

python manage.py runserver
run https://localhost:8000

... DONE, YOUR WELCOME TO MY SENOIR PROJECT OF EDUCATION AT KKU THALAND 2023 - 2024.

## Reset New Database
### # ลบชุดฐานข้อมูลเดิม | for example `rm -r store/migrations`
rm -r myapp/migrations 

python manage.py flush
### # สร้างฐานข้อมูลใหม่อ้างอิงตาม models.py | for example `python manage.py makemigrations store`
python manage.py makemigrations myapp 

### # สร้างชุดข้อมูลทั้งหมด
python manage.py migrate 
