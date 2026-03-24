# 📚 Course Management System (Django CBV)

A Django-based web application to manage courses using **Class-Based Views (CBVs)**.  
This project demonstrates CRUD operations (Create, Read, Update, Delete) with clean architecture and Django best practices.

---

## 🚀 Features

- 📋 View list of courses  
- 🔍 View detailed course information  
- ➕ Create new courses  
- ✏️ Update existing courses  
- ❌ Delete courses  
- 🔗 Dynamic URL routing with `get_absolute_url()`  
- ⚡ Built using Django Class-Based Views  

---

## 🏗️ Project Structure

```
courseCbv/
│
├── courseApp/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   └── courseApp/
│   │       ├── course_list.html
│   │       ├── course_detail.html
│   │       ├── course_form.html
│   │       └── course_confirm_delete.html
│
├── courseCbv/
│   ├── urls.py
│
├── manage.py
```

---

## 🧠 Model

```python
class course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    rating = models.IntegerField()

    def get_absolute_url(self):
        return reverse('coursedetail', kwargs={'pk': self.pk})
```

📌 Automatically redirects to course detail after creation/update.

---

## 🔧 Views

Implemented using Django **Class-Based Views**:

- `courseListView` → Displays all courses  
- `courseDetailView` → Shows course details  
- `courseCreateView` → Creates a new course  
- `courseUpdateView` → Updates an existing course  
- `courseDeleteView` → Deletes a course  

---

## 🌐 URL Routes

| Route | Description |
|------|------------|
| `/` | Course list |
| `/<id>/` | Course detail |
| `/create/` | Create course |
| `/update/<id>/` | Update course |
| `/delete/<id>/` | Delete course |
| `/admin/` | Django admin |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/course-cbv-app.git
cd course-cbv-app
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install django
```

### 4️⃣ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the server

```bash
python manage.py runserver
```

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 🛠️ Technologies Used

- Python 🐍  
- Django 🌐  
- SQLite 🗃️  
- HTML Templates  

---

## 📌 Future Improvements

- 🔐 User authentication & authorization  
- ⭐ Course rating system (dynamic)  
- 🔎 Search & filter courses  
- 📊 Dashboard analytics  
- 🌍 REST API (Django REST Framework)  
- ☁️ Deployment (Render / Railway / Docker)  

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository  
2. Create a new branch  
3. Commit your changes  
4. Push and open a Pull Request  

---

## 👨‍💻 Author

**Aranya Majumdar**  
- GitHub: https://github.com/aranya-code  

---