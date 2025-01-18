# Django_E-Commerce Docs | How to install this project

## English

### Download Python Version: 3.11.2 | 64 bit for Windows 10
- [Download Python](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

### Create database on phpMyAdmin
- Open XAMPP and click 'Admin' button in the MySQL row
- Database name: `myhotels`
- Collation: `utf8_general_ci`

### Make a new directory
Navigate to your desired directory and create a new one for the project.

### Create a virtual environment
```sh
python -m venv virt
```

### Clone the repository
```sh
git clone https://github.com/kawin101/Django_E-Commerce.git
cd Django_E-Commerce/ecom
```

### Activate the virtual environment
```sh
source ../virt/Scripts/activate
```

### Install dependencies
```sh
pip install -r requirements.txt
```

### Setup the database
```sh
python manage.py makemigrations
python manage.py migrate
```

### Create a superuser
```sh
python manage.py createsuperuser
```
- Username: `admin`
- Password: `password`
- Leave other fields empty

### Run the server
```sh
python manage.py runserver
```
Open [https://localhost:8000](https://localhost:8000)

### Reset the database
```sh
rm -r myapp/migrations
python manage.py flush
python manage.py makemigrations myapp
python manage.py migrate
```

... DONE, WELCOME TO MY SENIOR PROJECT OF EDUCATION AT KKU THAILAND 2023 - 2024.

## ภาษาไทย

### ดาวน์โหลด Python เวอร์ชัน 3.11.2 | 64 บิต สำหรับ Windows 10
- [ดาวน์โหลด Python](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

### สร้างฐานข้อมูลใน phpMyAdmin
- เปิด XAMPP แล้วคลิกปุ่ม 'Admin' ในแถว MySQL
- ชื่อฐานข้อมูล: `myhotels`
- การเข้ารหัส: `utf8_general_ci`

### สร้างไดเรกทอรีใหม่
ไปที่ไดเรกทอรีที่ต้องการและสร้างไดเรกทอรีใหม่สำหรับโปรเจกต์

### สร้างตัวจำลองสภาพแวดล้อมของ Python
```sh
python -m venv virt
```

### โคลน repository
```sh
git clone <repository_url> Django_E-Commerce
cd Django_E-Commerce/ecom
```

### เปิดใช้งานตัวจำลองสภาพแวดล้อม
```sh
source ../virt/Scripts/activate
```

### ติดตั้ง dependencies
```sh
pip install -r requirements.txt
```

### ตั้งค่าฐานข้อมูล
```sh
python manage.py makemigrations
python manage.py migrate
```

### สร้าง superuser
```sh
python manage.py createsuperuser
```
- ชื่อผู้ใช้: `admin`
- รหัสผ่าน: `password`
- เว้นช่องอื่นๆ ว่างไว้

### รันเซิร์ฟเวอร์
```sh
python manage.py runserver
```
เปิด [https://localhost:8000](https://localhost:8000)

### รีเซ็ตฐานข้อมูล
```sh
rm -r myapp/migrations
python manage.py flush
python manage.py makemigrations myapp
python manage.py migrate
```

... เสร็จสิ้น ยินดีต้อนรับสู่โปรเจกต์จบการศึกษาของฉันที่ KKU ประเทศไทย 2023 - 2024.

---

## The following section is originally written by a human:

** Download Python Version: 3.11.2 | 64 bit for Windows 10
- https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe

## Create database on phpMyAdmin
- Open your XAMPP and then click 'Admin' button rows of MySQL 
- Database name: myhotels 
- type: utf8_general_ci 

## Make a new dir
cd to dir 

### # สร้างตัวจำลองสภาพแวดล้อมของภาษา Python
pip install -m venv virt | python -m venv virt \
mkdir floder to keep your file \
clone repository to new directory 

/c/Django_E-Commerce/ 
- ecom 
- virt \
and cd ecom/ \
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

python manage.py runserver \
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
