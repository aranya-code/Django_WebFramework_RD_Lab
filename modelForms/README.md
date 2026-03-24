# 📘 Django ModelForms Lab

A simple Django application demonstrating the use of **ModelForms** to create, display, and manage data using Django’s ORM and form system.

---

## 🚀 Overview

This project is part of a Django learning lab focused on:

* Creating models using Django ORM
* Building forms using `ModelForm`
* Handling user input and validation
* Rendering data in templates
* Implementing basic CRUD operations

Django is a high-level Python web framework designed for rapid development and clean, pragmatic design ([GitHub][1]).

---

## 🧩 Features

* ✅ Create records using Django ModelForms
* ✅ Display all records in a list view
* ✅ Simple form handling with validation
* ✅ Template-based UI rendering
* ✅ Lightweight and beginner-friendly structure

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML Templates
* **Database:** SQLite (default Django DB)

---

## 📂 Project Structure

```
modelForms/
│── models.py       # Database models
│── forms.py        # ModelForm definition
│── views.py        # Application views
│── urls.py         # URL routing
│── templates/
│    └── mforms/
│         ├── index.html
│         ├── products.html
│         └── addproduct.html
│── tests.py        # Unit tests
```

---

## 📌 Models

The project includes a `formCreation` model:

* `startDate` – Start date of task
* `endDate` – End date of task
* `name` – Task name
* `assignedTo` – Assigned user
* `priority` – Task priority

---

## 🧾 Forms

Uses Django **ModelForm**:

* Automatically generates form fields from the model
* Handles validation internally
* Simplifies form creation and data saving

---

## 🌐 Views

* `index` → Homepage
* `products` → Displays all records
* `addProduct` → Handles form submission and data creation

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aranya-code/Django_WebFramework_RD_Lab.git
cd Django_WebFramework_RD_Lab/modelForms
```

---

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install django
```

---

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Start server

```bash
python manage.py runserver
```

---

### 6. Open in browser

```
http://127.0.0.1:8000/
```

---

## 🧪 Running Tests

```bash
python manage.py test mforms
```



## 🔧 Future Improvements

* Add update & delete functionality
* Improve validation logic
* Add Django messages framework
* Use class-based views
* Add REST API (Django REST Framework)

---

## 📚 Learning Goals

This project helps understand:

* Django Models & ORM
* ModelForms
* Request handling (GET/POST)
* Template rendering
* Basic testing

---

## 🤝 Contributing

This is a learning project, but contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Commit changes
4. Submit a pull request

---

## 📄 License

This project is for educational purposes.

---

## 👨‍💻 Author

**Aranya Majumdar**
GitHub: https://github.com/aranya-code

