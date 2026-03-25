# 🎓 Student Management System (Django CBV)

A Django-based web application to manage student records using **Class-Based Views (CBVs)**.  
This project demonstrates full CRUD operations along with clean architecture and Django best practices.

---

## 🚀 Features

- 📋 View list of students  
- 🔍 View detailed student information  
- ➕ Add new student records  
- ✏️ Update student details  
- ❌ Delete student records  
- 🔗 Automatic redirection using `get_absolute_url()`  
- ⚡ Built using Django Class-Based Views  

---

## 🏗️ Project Structure

```
CBVproject/
│
├── CBVApp/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   └── CBVApp/
│   │       ├── studentinfo_list.html
│   │       ├── studentinfo_detail.html
│   │       ├── studentinfo_form.html
│   │       └── studentinfo_confirm_delete.html
│
├── CBVproject/
│   ├── urls.py
│
├── manage.py
```

---

## 🧠 Model

```python
class studentInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    score = models.FloatField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
```

📌 Each student has a unique ID, name, and score.

---

## 🔧 Views

Implemented using Django **Class-Based Views (CBVs)**:

- `studentInfoView` → Displays all students  
- `studentDetailsView` → Shows student details  
- `studentCreateView` → Creates a new student  
- `studentUpdateView` → Updates student data  
- `studentDeleteView` → Deletes a student  

---

## 🌐 URL Routes

| Route | Description |
|------|------------|
| `/` | Student list |
| `/<id>/` | Student detail |
| `/create/` | Create student |
| `/update/<id>/` | Update student |
| `/delete/<id>/` | Delete student |
| `/admin/` | Django admin panel |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/student-cbv-app.git
cd student-cbv-app
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
- MySQL

---

## 📌 Future Improvements

- 🔐 Authentication (login/logout)  
- 📊 Student performance analytics  
- 🔎 Search & filter students  
- 📈 Graphical dashboard  
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

