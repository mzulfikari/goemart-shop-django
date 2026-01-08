##  🛒 Goemart Shop – Django E-Commerce (Dockerized)

<img src="/docs/db.Diagram.png">



---


<div dir="rtl">
Goemart  یک فروشگاه اینترنتی مبتنی بر Django است که با معماری ماژولار طراحی شده و به‌صورت کامل از طریق Docker و Docker Compose قابل اجرا، توسعه و استقرار می‌باشد. این پروژه با هدف ایجاد یک ساختار استاندارد، مقیاس‌پذیر و مناسب برای محیط‌های توسعه، تست و Production طراحی شده است.
</div>



---
## 🚀 Features

- 👤 سیستم حساب کاربری (ثبت‌نام، ورود، پروفایل)
- 🛍️ مدیریت محصولات
- 🛒 سبد خرید
- 📦 ثبت و مدیریت سفارش‌ها
- 🎨 قالب‌های HTML فروشگاهی
- 🔐 اعتبارسنجی فرم‌ها
- 🧱 معماری ماژولار Django
- 🐳 اجرای کامل با Docker
- ⚙️ مدیریت تنظیمات محیطی با env

---

## ⚙️ Environment Variables

```
envs/dev.env
```
 ### **نمونه:**

```
DEBUG=1
SECRET_KEY=django-insecure-secret-key
ALLOWED_HOSTS=*
```
---
## ▶️ Run Project with Docker (Recommended)

```
docker-compose exec web python manage.py migrate
```

---
## 2️⃣ Apply 

```
docker-compose exec web python manage.py migrate
```

---
## 3️⃣ Create superuser

```
docker-compose exec web python manage.py createsuperuser
```
---
## 4️⃣ Access project


🌐 **Website: http://localhost:8000**

🔐 **Admin panel: http://localhost:8000/admin**

---

## 🛠 Useful Docker Commands

 ### **Stop containers:**
```
docker-compose down
```
 ### **Rebuild only:**
 ```
docker-compose build
```
 ### **View logs:**
 ```
docker-compose logs -f
```
---
## 🧪 Run Project without Docker (Optional)
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
---
## 🧑‍💻 Tech Stack
• **Backend:** Django<br> • **Frontend:** HTML, CSS, JavaScript<br> • **Database:** SQLite (dev)<br> • **Containerization:** Docker & Docker Compose<br>
---

## 📌 Roadmap
• <span style="font-size:14px;">**Backend:** Django</span> • <span style="font-size:14px;">**Frontend:** HTML, CSS, JavaScript</span> • <span style="font-size:14px;">**Database:** SQLite (Development)</span> • <span style="font-size:14px;">**Containerization:** Docker & Docker Compose</span> • <span style="font-size:14px;">**Template Engine:** Django</span>

---
