# 🏥 Clinical Data Management System

A Django-based web application to manage **patient records** and their **clinical data** such as height, weight, blood pressure, and heart rate.

This project demonstrates the use of **Django Class-Based Views (CBVs)**, **ModelForms**, and **relational database design**.

---

## 🚀 Features

- 👤 Create, update, delete, and view patients  
- 📊 Add clinical data for each patient  
- 🔗 One-to-many relationship (Patient → Clinical Data)  
- 🧾 Form handling using Django ModelForms  
- ⚡ Class-Based Views for clean architecture  
- 🗃️ Automatic timestamp for clinical records  

---

## 🏗️ Project Structure

```
clinicalData/
│
├── clinicalApp/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── templates/
│   │   └── clinicalApp/
│   │       ├── patient_list.html
│   │       ├── patient_form.html
│   │       ├── patient_confirm_delete.html
│   │       └── clinicaldata.html
│
├── clinicalData/
│   ├── urls.py
│
├── manage.py
```

---

## 🧠 Models

### Patient

```python
class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
```

### ClinicalData

```python
class ClinicalData(models.Model):
    COMPONENT_NAMES = [
        ('Height','Height'),
        ('Weight','Weight'),
        ('Blood Pressure','Blood Pressure'),
        ('HeartRate','Heart Rate')
    ]

    componentName = models.CharField(choices=COMPONENT_NAMES, max_length=20)
    componentValue = models.CharField(max_length=20)
    measuredDate = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
```

📌 Each patient can have multiple clinical records :contentReference[oaicite:0]{index=0}

---

## 🧾 Forms

```python
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class ClinicalDataForm(forms.ModelForm):
    class Meta:
        model = ClinicalData
        fields = '__all__'
```

Used for handling form input efficiently :contentReference[oaicite:1]{index=1}

---

## 🔧 Views

### Class-Based Views

- `PatientListView` → List all patients  
- `PatientCreateView` → Add new patient  
- `PatientUpdateView` → Update patient  
- `PatientDeleteView` → Delete patient  

### Function-Based View

- `addData` → Add clinical data for a specific patient  

Built using Django CBVs for scalability :contentReference[oaicite:2]{index=2}

---

## 🌐 URL Routes

| Route | Description |
|------|------------|
| `/` | List patients |
| `/create/` | Create patient |
| `/update/<id>/` | Update patient |
| `/delete/<id>/` | Delete patient |
| `/clinicaldata/<id>/` | Add clinical data |
| `/admin/` | Admin panel |

Defined in `urls.py` :contentReference[oaicite:3]{index=3}

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/clinical-data-app.git
cd clinical-data-app
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

- 🔐 Authentication (login/register)  
- 📊 Dashboard with charts  
- 🔎 Search & filter patients  
- 📅 Historical data visualization  
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

