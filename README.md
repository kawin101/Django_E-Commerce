# Django_E-Commerce Docs | How to install this project

Please select your language / กรุณาเลือกภาษาของคุณ / Por favor seleccione su idioma / Veuillez sélectionner votre langue / 请选择你的语言 / कृपया अपनी भाषा चुनें / Пожалуйста, выберите ваш язык / Bitte wählen Sie Ihre Sprache / 请选择您的语言 / 请选择您的语言 / 请选择您的语言:
- [English](#english)
- [ภาษาไทย](#ภาษาไทย)
- [Español](#español)
- [Français](#français)
- [中文 (简体)](#中文-简体)
- [हिन्दी](#हिन्दी)
- [العربية](#العربية)
- [Português](#português)
- [Русский](#русский)
- [Deutsch](#deutsch)
- [Add your language here](#)

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
git clone https://github.com/kawin101/Django_E-Commerce.git
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

## Español

### Descargar Python Versión 3.11.2 | 64 bits para Windows 10
- [Descargar Python](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

// ...existing code...

... HECHO, BIENVENIDO A MI PROYECTO DE FIN DE CARRERA EN KKU TAILANDIA 2023 - 2024.

## Français

### Télécharger Python Version 3.11.2 | 64 bits pour Windows 10
- [Télécharger Python](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

// ...existing code...

... TERMINÉ, BIENVENUE À MON PROJET DE FIN D'ÉTUDES À KKU THAÏLANDE 2023 - 2024.

## 中文 (简体)

### 下载 Python 版本 3.11.2 | 适用于 Windows 10 的 64 位
- [下载 Python](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

// ...existing code...

... 完成，欢迎来到我在泰国 KKU 的 2023 - 2024 年毕业项目。

## हिन्दी

### विंडोज़ 10 के लिए 64 बिट संस्करण 3.11.2 डाउनलोड करें
- [Python डाउनलोड करें](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

// ...existing code...

... हो गया, KKU थाईलैंड 2023 - 2024 में मेरी स्नातक परियोजना में आपका स्वागत है।

## العربية

### تحميل إصدار Python 3.11.2 | 64 بت لنظام Windows 10
- [تحميل Python](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

// ...existing code...

... تم، مرحبًا بكم في مشروع التخرج الخاص بي في KKU تايلاند 2023 - 2024.

## Português

### Baixar Python Versão 3.11.2 | 64 bits para Windows 10
- [Baixar Python](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

// ...existing code...

... FEITO, BEM-VINDO AO MEU PROJETO DE CONCLUSÃO DE CURSO NA KKU TAILÂNDIA 2023 - 2024.

## Русский

### Скачать Python версии 3.11.2 | 64 бит для Windows 10
- [Скачать Python](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

// ...existing code...

... ГОТОВО, ДОБРО ПОЖАЛОВАТЬ В МОЙ ВЫПУСКНОЙ ПРОЕКТ В KKU ТАИЛАНД 2023 - 2024.

## Deutsch

### Python Version 3.11.2 | 64 Bit für Windows 10 herunterladen
- [Python herunterladen](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

// ...existing code...

... FERTIG, WILLKOMMEN ZU MEINEM ABSCHLUSSPROJEKT AN DER KKU THAILAND 2023 - 2024.

---