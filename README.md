# Django_E-Commerce Docs | How to install this project

Please select your language / กรุณาเลือกภาษาของคุณ:
- [English](#english)
- [ภาษาไทย](#ภาษาไทย)
- [中文](#中文)
- [हिन्दी](#हिन्दी)
- [Español](#español)
- [Français](#français)
- [العربية](#العربية)
- [বাংলা](#বাংলা)
- [Русский](#русский)
- [Português](#português)
- [اردو](#اردو)

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

## 中文

### 下载 Python 版本: 3.11.2 | 64 位 Windows 10
- [下载 Python](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

### 在 phpMyAdmin 中创建数据库
- 打开 XAMPP 并点击 MySQL 行中的 'Admin' 按钮
- 数据库名称: `myhotels`
- 校对: `utf8_general_ci`

### 创建新目录
导航到您想要的目录并为项目创建一个新目录。

### 创建虚拟环境
```sh
python -m venv virt
```

### 克隆仓库
```sh
git clone https://github.com/kawin101/Django_E-Commerce.git
cd Django_E-Commerce/ecom
```

### 激活虚拟环境
```sh
source ../virt/Scripts/activate
```

### 安装依赖
```sh
pip install -r requirements.txt
```

### 设置数据库
```sh
python manage.py makemigrations
python manage.py migrate
```

### 创建超级用户
```sh
python manage.py createsuperuser
```
- 用户名: `admin`
- 密码: `password`
- 其他字段留空

### 运行服务器
```sh
python manage.py runserver
```
打开 [https://localhost:8000](https://localhost:8000)

### 重置数据库
```sh
rm -r myapp/migrations
python manage.py flush
python manage.py makemigrations myapp
python manage.py migrate
```

... 完成，欢迎来到我在泰国 KKU 的 2023 - 2024 毕业项目。

## हिन्दी

### Python संस्करण 3.11.2 | 64 बिट Windows 10 के लिए डाउनलोड करें
- [Python डाउनलोड करें](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

### phpMyAdmin में डेटाबेस बनाएं
- XAMPP खोलें और MySQL पंक्ति में 'Admin' बटन पर क्लिक करें
- डेटाबेस का नाम: `myhotels`
- कोलेशन: `utf8_general_ci`

### एक नई निर्देशिका बनाएं
अपनी इच्छित निर्देशिका पर जाएं और परियोजना के लिए एक नई निर्देशिका बनाएं।

### एक वर्चुअल वातावरण बनाएं
```sh
python -m venv virt
```

### रिपॉजिटरी क्लोन करें
```sh
git clone https://github.com/kawin101/Django_E-Commerce.git
cd Django_E-Commerce/ecom
```

### वर्चुअल वातावरण सक्रिय करें
```sh
source ../virt/Scripts/activate
```

### निर्भरता स्थापित करें
```sh
pip install -r requirements.txt
```

### डेटाबेस सेटअप करें
```sh
python manage.py makemigrations
python manage.py migrate
```

### एक सुपरयूजर बनाएं
```sh
python manage.py createsuperuser
```
- उपयोगकर्ता नाम: `admin`
- पासवर्ड: `password`
- अन्य फ़ील्ड खाली छोड़ दें

### सर्वर चलाएं
```sh
python manage.py runserver
```
[https://localhost:8000](https://localhost:8000) खोलें

### डेटाबेस रीसेट करें
```sh
rm -r myapp/migrations
python manage.py flush
python manage.py makemigrations myapp
python manage.py migrate
```

... समाप्त, 2023 - 2024 में थाईलैंड के KKU में मेरी स्नातक परियोजना में आपका स्वागत है।

## Español

### Descargar Python Versión: 3.11.2 | 64 bits para Windows 10
- [Descargar Python](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

### Crear base de datos en phpMyAdmin
- Abra XAMPP y haga clic en el botón 'Admin' en la fila de MySQL
- Nombre de la base de datos: `myhotels`
- Intercalación: `utf8_general_ci`

### Crear un nuevo directorio
Navegue a su directorio deseado y cree uno nuevo para el proyecto.

### Crear un entorno virtual
```sh
python -m venv virt
```

### Clonar el repositorio
```sh
git clone https://github.com/kawin101/Django_E-Commerce.git
cd Django_E-Commerce/ecom
```

### Activar el entorno virtual
```sh
source ../virt/Scripts/activate
```

### Instalar dependencias
```sh
pip install -r requirements.txt
```

### Configurar la base de datos
```sh
python manage.py makemigrations
python manage.py migrate
```

### Crear un superusuario
```sh
python manage.py createsuperuser
```
- Nombre de usuario: `admin`
- Contraseña: `password`
- Deje otros campos vacíos

### Ejecutar el servidor
```sh
python manage.py runserver
```
Abra [https://localhost:8000](https://localhost:8000)

### Restablecer la base de datos
```sh
rm -r myapp/migrations
python manage.py flush
python manage.py makemigrations myapp
python manage.py migrate
```

... HECHO, BIENVENIDO A MI PROYECTO DE GRADUACIÓN EN KKU TAILANDIA 2023 - 2024.

## Français

### Télécharger la version Python: 3.11.2 | 64 bits pour Windows 10
- [Télécharger Python](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

### Créer une base de données sur phpMyAdmin
- Ouvrez XAMPP et cliquez sur le bouton 'Admin' dans la ligne MySQL
- Nom de la base de données: `myhotels`
- Interclassement: `utf8_general_ci`

### Créer un nouveau répertoire
Naviguez vers votre répertoire souhaité et créez-en un nouveau pour le projet.

### Créer un environnement virtuel
```sh
python -m venv virt
```

### Cloner le dépôt
```sh
git clone https://github.com/kawin101/Django_E-Commerce.git
cd Django_E-Commerce/ecom
```

### Activer l'environnement virtuel
```sh
source ../virt/Scripts/activate
```

### Installer les dépendances
```sh
pip install -r requirements.txt
```

### Configurer la base de données
```sh
python manage.py makemigrations
python manage.py migrate
```

### Créer un superutilisateur
```sh
python manage.py createsuperuser
```
- Nom d'utilisateur: `admin`
- Mot de passe: `password`
- Laissez les autres champs vides

### Exécuter le serveur
```sh
python manage.py runserver
```
Ouvrez [https://localhost:8000](https://localhost:8000)

### Réinitialiser la base de données
```sh
rm -r myapp/migrations
python manage.py flush
python manage.py makemigrations myapp
python manage.py migrate
```

... TERMINÉ, BIENVENUE DANS MON PROJET DE FIN D'ÉTUDES À KKU THAÏLANDE 2023 - 2024.

## العربية

### تحميل إصدار Python: 3.11.2 | 64 بت لنظام Windows 10
- [تحميل Python](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

### إنشاء قاعدة بيانات في phpMyAdmin
- افتح XAMPP وانقر على زر 'Admin' في صف MySQL
- اسم قاعدة البيانات: `myhotels`
- الترتيب: `utf8_general_ci`

### إنشاء دليل جديد
انتقل إلى الدليل المطلوب وأنشئ واحدًا جديدًا للمشروع.

### إنشاء بيئة افتراضية
```sh
python -m venv virt
```

### استنساخ المستودع
```sh
git clone https://github.com/kawin101/Django_E-Commerce.git
cd Django_E-Commerce/ecom
```

### تفعيل البيئة الافتراضية
```sh
source ../virt/Scripts/activate
```

### تثبيت التبعيات
```sh
pip install -r requirements.txt
```

### إعداد قاعدة البيانات
```sh
python manage.py makemigrations
python manage.py migrate
```

### إنشاء مستخدم فائق
```sh
python manage.py createsuperuser
```
- اسم المستخدم: `admin`
- كلمة المرور: `password`
- اترك الحقول الأخرى فارغة

### تشغيل الخادم
```sh
python manage.py runserver
```
افتح [https://localhost:8000](https://localhost:8000)

### إعادة تعيين قاعدة البيانات
```sh
rm -r myapp/migrations
python manage.py flush
python manage.py makemigrations myapp
python manage.py migrate
```

... تم، مرحبًا بك في مشروع تخرجي في KKU تايلاند 2023 - 2024.

## বাংলা

### Python সংস্করণ 3.11.2 | 64 বিট Windows 10 এর জন্য ডাউনলোড করুন
- [Python ডাউনলোড করুন](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

### phpMyAdmin এ ডাটাবেস তৈরি করুন
- XAMPP খুলুন এবং MySQL সারির 'Admin' বোতামে ক্লিক করুন
- ডাটাবেসের নাম: `myhotels`
- কোলেশন: `utf8_general_ci`

### একটি নতুন ডিরেক্টরি তৈরি করুন
আপনার পছন্দের ডিরেক্টরিতে যান এবং প্রকল্পের জন্য একটি নতুন ডিরেক্টরি তৈরি করুন।

### একটি ভার্চুয়াল পরিবেশ তৈরি করুন
```sh
python -m venv virt
```

### রিপোজিটরি ক্লোন করুন
```sh
git clone https://github.com/kawin101/Django_E-Commerce.git
cd Django_E-Commerce/ecom
```

### ভার্চুয়াল পরিবেশ সক্রিয় করুন
```sh
source ../virt/Scripts/activate
```

### নির্ভরতা ইনস্টল করুন
```sh
pip install -r requirements.txt
```

### ডাটাবেস সেটআপ করুন
```sh
python manage.py makemigrations
python manage.py migrate
```

### একটি সুপারইউজার তৈরি করুন
```sh
python manage.py createsuperuser
```
- ব্যবহারকারীর নাম: `admin`
- পাসওয়ার্ড: `password`
- অন্যান্য ক্ষেত্রগুলি খালি রাখুন

### সার্ভার চালান
```sh
python manage.py runserver
```
[https://localhost:8000](https://localhost:8000) খুলুন

### ডাটাবেস রিসেট করুন
```sh
rm -r myapp/migrations
python manage.py flush
python manage.py makemigrations myapp
python manage.py migrate
```

... সম্পন্ন, 2023 - 2024 সালে থাইল্যান্ডের KKU-তে আমার স্নাতক প্রকল্পে স্বাগতম।

## Русский

### Скачать версию Python: 3.11.2 | 64 бит для Windows 10
- [Скачать Python](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

### Создать базу данных в phpMyAdmin
- Откройте XAMPP и нажмите кнопку 'Admin' в строке MySQL
- Имя базы данных: `myhotels`
- Сопоставление: `utf8_general_ci`

### Создать новый каталог
Перейдите в нужный каталог и создайте новый для проекта.

### Создать виртуальную среду
```sh
python -m venv virt
```

### Клонировать репозиторий
```sh
git clone https://github.com/kawin101/Django_E-Commerce.git
cd Django_E-Commerce/ecom
```

### Активировать виртуальную среду
```sh
source ../virt/Scripts/activate
```

### Установить зависимости
```sh
pip install -r requirements.txt
```

### Настроить базу данных
```sh
python manage.py makemigrations
python manage.py migrate
```

### Создать суперпользователя
```sh
python manage.py createsuperuser
```
- Имя пользователя: `admin`
- Пароль: `password`
- Остальные поля оставьте пустыми

### Запустить сервер
```sh
python manage.py runserver
```
Откройте [https://localhost:8000](https://localhost:8000)

### Сбросить базу данных
```sh
rm -r myapp/migrations
python manage.py flush
python manage.py makemigrations myapp
python manage.py migrate
```

... ГОТОВО, ДОБРО ПОЖАЛОВАТЬ В МОЙ ВЫПУСКНОЙ ПРОЕКТ В KKU ТАИЛАНД 2023 - 2024.

## Português

### Baixar a versão do Python: 3.11.2 | 64 bits para Windows 10
- [Baixar Python](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

### Criar banco de dados no phpMyAdmin
- Abra o XAMPP e clique no botão 'Admin' na linha do MySQL
- Nome do banco de dados: `myhotels`
- Colação: `utf8_general_ci`

### Criar um novo diretório
Navegue até o diretório desejado e crie um novo para o projeto.

### Criar um ambiente virtual
```sh
python -m venv virt
```

### Clonar o repositório
```sh
git clone https://github.com/kawin101/Django_E-Commerce.git
cd Django_E-Commerce/ecom
```

### Ativar o ambiente virtual
```sh
source ../virt/Scripts/activate
```

### Instalar dependências
```sh
pip install -r requirements.txt
```

### Configurar o banco de dados
```sh
python manage.py makemigrations
python manage.py migrate
```

### Criar um superusuário
```sh
python manage.py createsuperuser
```
- Nome de usuário: `admin`
- Senha: `password`
- Deixe os outros campos em branco

### Executar o servidor
```sh
python manage.py runserver
```
Abra [https://localhost:8000](https://localhost:8000)

### Redefinir o banco de dados
```sh
rm -r myapp/migrations
python manage.py flush
python manage.py makemigrations myapp
python manage.py migrate
```

... FEITO, BEM-VINDO AO MEU PROJETO DE GRADUAÇÃO NA KKU TAILÂNDIA 2023 - 2024.

## اردو

### Python ورژن 3.11.2 | 64 بٹ Windows 10 کے لیے ڈاؤن لوڈ کریں
- [Python ڈاؤن لوڈ کریں](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)

### phpMyAdmin میں ڈیٹا بیس بنائیں
- XAMPP کھولیں اور MySQL کی قطار میں 'Admin' بٹن پر کلک کریں
- ڈیٹا بیس کا نام: `myhotels`
- کولیشن: `utf8_general_ci`

### ایک نیا ڈائریکٹری بنائیں
اپنی مطلوبہ ڈائریکٹری پر جائیں اور پروجیکٹ کے لیے ایک نیا ڈائریکٹری بنائیں۔

### ایک ورچوئل ماحول بنائیں
```sh
python -m venv virt
```

### ریپوزٹری کلون کریں
```sh
git clone https://github.com/kawin101/Django_E-Commerce.git
cd Django_E-Commerce/ecom
```

### ورچوئل ماحول کو فعال کریں
```sh
source ../virt/Scripts/activate
```

### انحصار انسٹال کریں
```sh
pip install -r requirements.txt
```

### ڈیٹا بیس سیٹ اپ کریں
```sh
python manage.py makemigrations
python manage.py migrate
```

### ایک سپر یوزر بنائیں
```sh
python manage.py createsuperuser
```
- صارف نام: `admin`
- پاس ورڈ: `password`
- دیگر فیلڈز کو خالی چھوڑ دیں

### سرور چلائیں
```sh
python manage.py runserver
```
[https://localhost:8000](https://localhost:8000) کھولیں

### ڈیٹا بیس ری سیٹ کریں
```sh
rm -r myapp/migrations
python manage.py flush
python manage.py makemigrations myapp
python manage.py migrate
```

... مکمل، 2023 - 2024 میں تھائی لینڈ کے KKU میں میرے گریجویشن پروجیکٹ میں خوش آمدید۔