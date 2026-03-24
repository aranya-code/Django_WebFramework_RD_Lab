# 📝 Django ToDo App

A simple and clean ToDo application built using **Django**. This project allows users to create, view, and manage tasks with a basic completion tracking system.

---

## 🚀 Features

- ✅ Add new tasks with a name and description  
- 📋 View all tasks  
- ✔️ Mark tasks as completed  
- ❌ Mark tasks as incomplete  
- 🔔 User feedback using Django messages  

---

## 🏗️ Project Structure

```
ToDoProject/
│
├── ToDoApp/
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   └── ToDoApp/
│   │       ├── index.html
│   │       └── tasks.html
│
├── ToDoProject/
│   ├── urls.py
│
├── manage.py

```
---

## 🧠 Models

📌 This model stores:
- User name  
- Task description  
- Completion status  

---

## 🔧 Views

The application includes the following views:

- **AddTask** → Add a new task  
- **GetTasks** → Display all tasks  
- **cross** → Mark task as completed  
- **uncross** → Mark task as incomplete  

---

## 🌐 URL Routes

| Route | Description |
|------|------------|
| `/` | Add task page |
| `/task_view/` | View all tasks |
| `/cross/<id>/` | Mark task as completed |
| `/uncross/<id>/` | Mark task as incomplete |
| `/admin/` | Django admin panel |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/django-todo-app.git
cd django-todo-app
```

### 2️⃣ Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
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

## 🧪 Usage

1. Go to `http://127.0.0.1:8000/`  
2. Add a task using the form  
3. View tasks in the task list page  
4. Mark tasks as completed/incomplete  

---

## 🛠️ Technologies Used

- Python 🐍  
- Django 🌐  
- HTML (Templates)  
- SQLite (default DB)  

---

## 📌 Future Improvements

- 🔐 User authentication  
- 🗂️ Task categories  
- 📅 Due dates & reminders  
- 🎨 UI enhancements (Bootstrap/Tailwind)  
- 🧠 REST API (Django REST Framework)  
- 🌍 Deployment (Render / Railway / Docker)  

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo  
2. Create a new branch  
3. Commit your changes  
4. Push and open a Pull Request  

---

## 👨‍💻 Author

**Aranya Majumdar**  
- GitHub: https://github.com/aranya-code  

---
