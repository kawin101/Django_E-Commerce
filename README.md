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