# Skill Learning Website with Customizable Roadmaps

This project is a customizable skill-learning website that generates roadmap flowcharts for learning skills, similar to [roadmap.sh](https://roadmap.sh). It includes an AI onboarding process to gauge the user's level using questions and recommends tailored video tutorials based on the user's proficiency level. The website is built using Python frameworks such as Django for the backend and Flask for the AI onboarding.

## **Directory Structure**

```plaintext
skill_learning/
├── manage.py               # Django's management script
├── skill_learning/         # Django project settings and configurations
│   ├── __init__.py
│   ├── settings.py         # Django settings
│   ├── urls.py             # Root URL configuration
│   ├── wsgi.py             # WSGI entry point for deployment
│   ├── asgi.py             # ASGI entry point for async applications
├── users/                  # User app for registration and AI onboarding
│   ├── __init__.py
│   ├── models.py           # User model customization
│   ├── views.py            # Views for user management
│   ├── urls.py             # User app URL configuration
│   ├── forms.py            # Forms for AI onboarding
│   ├── ai_onboarding.py    # AI onboarding logic
│   ├── templates/          # HTML templates for the user app
│   │   ├── onboarding.html # Onboarding form
│   │   ├── dashboard.html  # Dashboard for logged-in users
│   ├── static/             # Static files for the user app
│   │   ├── css/
│   │   │   └── style.css   # CSS for the user app
│   │   ├── js/
│   │       └── script.js   # JavaScript for the user app
├── roadmaps/               # Roadmap app for skill roadmaps
│   ├── __init__.py
│   ├── models.py           # Roadmap model
│   ├── views.py            # Views for roadmaps
│   ├── urls.py             # Roadmap app URL configuration
│   ├── templates/          # HTML templates for the roadmap app
│   │   ├── roadmap_list.html
│   │   ├── roadmap_detail.html
│   ├── static/             # Static files for the roadmap app
│   │   ├── css/
│   │   │   └── roadmap.css
│   │   ├── js/
│   │       └── roadmap.js
├── db.sqlite3              # SQLite database file
└── requirements.txt        # Project dependencies
```

---

## **Setup Instructions**

Follow these steps to set up and run the project on your local machine.

### **1. Clone the Repository**

```bash
git clone https://github.com/your-repo/skill-learning.git
cd skill-learning
```

### **2. Set Up a Virtual Environment**

Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### **3. Install Dependencies**

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### **4. Run Migrations**

Apply database migrations:

```bash
python manage.py migrate
```

### **5. Run the Development Server**

Start the Django development server:

```bash
python manage.py runserver
```

Access the website at `http://127.0.0.1:8000/`.

---

## **Code Overview**

### **1. Django Backend**

#### **settings.py**

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'roadmaps',
]
STATIC_URL = '/static/'
TEMPLATES_DIR = BASE_DIR / "templates"
```

#### **urls.py**

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('roadmaps/', include('roadmaps.urls')),
]
```

### **2. Users App**

#### **models.py**

```python
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    level = models.CharField(max_length=50, default="Beginner")
```

#### **forms.py**

```python
from django import forms
from .models import CustomUser

class OnboardingForm(forms.Form):
    question_1 = forms.CharField(label="Do you have prior experience in coding?")
    question_2 = forms.IntegerField(label="Rate your proficiency in Python (1-10):")
```

#### **ai_onboarding.py**

```python
def evaluate_user_level(responses):
    if responses['question_2'] > 7:
        return "Advanced"
    elif responses['question_2'] > 4:
        return "Intermediate"
    return "Beginner"
```

#### **views.py**

```python
from django.shortcuts import render, redirect
from .forms import OnboardingForm
from .ai_onboarding import evaluate_user_level

def onboarding_view(request):
    if request.method == "POST":
        form = OnboardingForm(request.POST)
        if form.is_valid():
            user_level = evaluate_user_level(form.cleaned_data)
            request.user.level = user_level
            request.user.save()
            return redirect('dashboard')
    else:
        form = OnboardingForm()
    return render(request, 'onboarding.html', {'form': form})
```

#### **templates/onboarding.html**

```html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Submit</button>
</form>
```

---

### **3. Roadmaps App**

#### **models.py**

```python
from django.db import models

class Roadmap(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tutorial_link = models.URLField()
    level = models.CharField(max_length=50)
```

#### **views.py**

```python
from django.shortcuts import render
from .models import Roadmap

def roadmap_list(request):
    roadmaps = Roadmap.objects.filter(level=request.user.level)
    return render(request, 'roadmap_list.html', {'roadmaps': roadmaps})
```

#### **templates/roadmap_list.html**

```html
<h1>Roadmaps</h1>
<ul>
  {% for roadmap in roadmaps %}
    <li>
      <a href="{{ roadmap.tutorial_link }}">{{ roadmap.title }}</a>
      <p>{{ roadmap.description }}</p>
    </li>
  {% endfor %}
</ul>
```

---

### **4. Frontend Customization**

#### **static/css/style.css**

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f8f9fa;
    margin: 0;
    padding: 0;
}
```

#### **static/js/script.js**

```javascript
console.log("Frontend JS loaded successfully.");
```

---

### **Dependencies**

Add these dependencies to `requirements.txt`:

```plaintext
Django==4.0
```

---

### **Deployment**

For production, consider deploying using services like Heroku, AWS, or Azure. Use `gunicorn` as the application server and a PostgreSQL database.

If you need more details, let me know!
