# 📚 Course Management System (Django)

A simple CRUD-based web application built with Django to manage courses.
Users can **create, view, update, and delete courses** through a web interface.

---

## 🚀 Features

* 📄 View all courses
* ➕ Add new course
* ✏️ Update existing course
* ❌ Delete course
* 🧾 Form-based input using Django ModelForms

---

## 🏗️ Project Structure

```
courseList/
│
├── models.py        # Course model
├── views.py         # CRUD logic
├── forms.py         # ModelForm for course
├── urls.py          # URL routing
├── templates/
│   └── courseList/
│       ├── index.html
│       ├── create.html
│       └── update.html
```

---

## 🌐 URL Endpoints

| URL            | Description      |
| -------------- | ---------------- |
| `/`            | View all courses |
| `/add/`        | Add a new course |
| `/update/<id>` | Update a course  |
| `/delete/<id>` | Delete a course  |

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
venv\Scripts\activate      # Windows
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

### 5. Run Server

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

---

## 🛠️ Tech Stack

* Python
* Django
* SQLite (default DB)
* HTML Templates

---

## 📌 Future Scope

* REST API with DRF
* JWT Authentication
* Frontend with Angular/React
* Deployment (Docker + Cloud)

---

## 👨‍💻 Author

Aranya Majumdar

---

