# Movies App – Django Web Framework

## Overview

The Movies App is a simple Django application that demonstrates how to build a movie listing web application using the Django framework. The project showcases core Django concepts such as models, views, templates, and URL routing to display movie data.

This project is part of the Django Web Framework RD Lab and is designed to help learners understand how Django applications are structured and how data flows from the backend to the frontend.

---

## Features

- Display a list of movies
- View movie details
- Django template rendering
- URL routing with Django
- Organized Django application structure

---

## Tech Stack

Language: Python  
Framework: Django  
Frontend: HTML  
Database: SQLite (default Django database)

---

## Project Structure
```

movies/
│
├── movies/                 # Project configuration folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── moviesApp/              # Django application
│   ├── migrations/
│   │   └── __init__.py
│   │
│   ├── templates/
│   │   └── moviesApp/
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── db.sqlite3              # SQLite database
├── manage.py               # Django project manager
└── README.md
```
---


## Learning Objectives

- Understand Django project and app structure
- Create models and database migrations
- Render templates in Django
- Handle URLs and views
- Build simple web applications with Django

---

## Future Improvements

- Add movie ratings
- Add search functionality
- Add user authentication
- Improve UI with Bootstrap

---

## Author
Aranya Majumdar

GitHub:
https://github.com/aranya-code