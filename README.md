##  🛒 Goemart Shop – Django E-Commerce (Dockerized)

<img src="/docs/db.Diagram.png">
<img src="/docs/home.png">
<img src="/docs/product.png">
<img src="/docs/managment order.png">
<img src="/docs/managmet product.png">
<img src="/docs/add product.png">
<img src="/docs/mangment message.png

---


<div dir="rtl">
Goemart is an online store built on Django, designed with a modular architecture, and fully runnable, developable, and deployable through Docker and Docker Compose. This project aims to provide a standardized, scalable structure suitable for development, testing, and production environments.
</div>



---
## 🚀 Features

• <span style="font-size:14px;">**User authentication system (signup, login, profile)**</span><br> • <span style="font-size:14px;">**Product management**</span><br> • <span style="font-size:14px;">**Shopping cart**</span><br> • <span style="font-size:14px;">**Order creation and management**</span><br> • <span style="font-size:14px;">**HTML-based store templates**</span><br> • <span style="font-size:14px;">**Form validation**</span><br> • <span style="font-size:14px;">**Modular Django architecture**</span><br> • <span style="font-size:14px;">**Full Docker support**</span><br> • <span style="font-size:14px;">**Environment-based configuration (env files)**</span><br>env

---

## ⚙️ Environment Variables

```
envs/dev.env
```
 ### **Example:**

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

• <span style="font-size:14px;">**Backend:** Django</span><br> • <span style="font-size:14px;">**Frontend:** HTML, CSS, JavaScript</span><br> • <span style="font-size:14px;">**Database:** SQLite (dev)</span><br> • <span style="font-size:14px;">**Containerization:** Docker & Docker Compose</span><br>

---

## 📌 Roadmap
• <span style="font-size:14px;">**PostgreSQL service**</span><br> • <span style="font-size:14px;">**Payment gateway**</span><br> • <span style="font-size:14px;">**REST API**</span><br> • <span style="font-size:14px;">**Production Docker setup**</span><br> • <span style="font-size:14px;">**CI/CD**</span><br>

---
## 📄 License

• <span style="font-size:14px;">**MIT License**</span><br> • <span style="font-size:14px;">**Developed by Morteza ❤️**</span><br>
