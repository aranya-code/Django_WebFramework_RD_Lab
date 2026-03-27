# 🎓 Student Management System (Django)

A simple CRUD-based web application built with Django to manage student records.
The system supports **authentication, authorization, and role-based deletion permissions**.

---

## 🚀 Features

* 🔐 User authentication (login/logout)
* 📄 View all students (login required)
* ➕ Create new student records
* ✏️ Update student details
* ❌ Delete students (permission-based)
* 🧾 Form handling using Django ModelForms

---

## 🏗️ Project Structure

```
fvbAPP/
│
├── models.py        # Student model
├── views.py         # CRUD logic with authentication
├── forms.py         # ModelForm for student
├── tests.py         # Unit test cases
├── templates/
│   └── fvbAPP/
│       ├── index.html
│       ├── create.html
│       ├── update.html
│       └── logout.html
```

---

## 🌐 URL Endpoints

| URL                | Description                          |
| ------------------ | ------------------------------------ |
| `/`                | View all students (login required)   |
| `/create/`         | Create a new student                 |
| `/update/<id>`     | Update student                       |
| `/delete/<id>`     | Delete student (requires permission) |
| `/accounts/login/` | Login                                |
| `/logout/`         | Logout                               |

---

## 🔐 Authentication & Permissions

* Uses Django built-in authentication system
* All views require login (`@login_required`)
* Delete operation requires permission:

```
fvbAPP.delete_studentinfo
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <project-folder>
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate   # Windows
```

---

### 3. Install Dependencies

```bash
pip install django
```

---

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

---

### 6. Run Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

## 🧪 Running Tests

```bash
python manage.py test
```

## 🔧 Suggested Improvements


## 🛠️ Tech Stack

* Python
* Django
* SQLite (default database)
* HTML Templates

---

## 📌 Future Enhancements

* REST API with Django REST Framework
* JWT Authentication
* Frontend integration (Angular/React)
* Docker-based deployment
* CI/CD pipeline

---

## 👨‍💻 Author

Aranya Majumdar

---


