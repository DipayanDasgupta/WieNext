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
Further Steps for Project Realization
This section outlines the next steps to complete the project and provides guidance on how to distribute the work effectively among 5 team members, including those with limited Python knowledge.

Further Steps
Enhance the AI Onboarding Process

Add more questions to the onboarding process to gauge the user's level more accurately.
Implement machine learning or rule-based logic for better user level predictions.
Store user responses in the database for analytics.
Build a Dynamic Roadmap System

Expand the roadmap database with more categories (e.g., Web Development, Data Science).
Add a dashboard to allow administrators to add/edit/delete roadmaps dynamically.
Incorporate filters in the UI so users can browse roadmaps by skill level or topic.
Video Recommendation System

Integrate a third-party API (e.g., YouTube Data API) to fetch and recommend videos dynamically.
Build a recommendation engine using the user's level and preferences.
Improve UI/UX

Design an engaging and modern front-end for onboarding and roadmap pages.
Use libraries like Bootstrap or Tailwind CSS for a responsive layout.
Add JavaScript for interactivity (e.g., roadmap flowcharts or collapsible sections).
Testing and Deployment

Write test cases for models, views, and templates using Django’s test framework.
Use Docker for containerization and ensure the app runs seamlessly in any environment.
Deploy the project using a cloud platform like Heroku, AWS, or Google Cloud.
Work Distribution
Here’s how to divide the tasks among the 5 team members:

Person 1: Python/Django Expert
Responsible for overall project architecture and backend implementation.
Tasks:
Set up the Django project structure.
Implement user authentication and onboarding logic.
Build models, forms, and views for roadmaps and AI onboarding.
Person 2: Intermediate Python Learner
Responsible for integrating video recommendations and the dynamic roadmap system.
Tasks:
Write the logic for fetching videos from the YouTube Data API.
Implement the roadmap CRUD (Create, Read, Update, Delete) functionality.
Connect the frontend with the backend.
Person 3: Front-End Specialist (Little Python Knowledge)
Focus on designing the UI and improving user experience.
Tasks:
Create HTML templates for onboarding, dashboards, and roadmaps.
Design the CSS and JavaScript for dynamic roadmap flowcharts.
Ensure responsiveness and accessibility.
Person 4: Beginner with Python
Work on adding content and testing the application.
Tasks:
Populate the database with roadmap data.
Test features using Django’s admin panel and report bugs.
Write beginner-friendly documentation for team use.
Person 5: Beginner with Python
Focus on deployment and learning basic Django concepts.
Tasks:
Set up the project in a local environment and test its functionality.
Assist with deployment (e.g., setting up Docker and cloud deployment).
Learn Django by working on small tasks like adding routes or writing simple views.
Collaboration Tips
Version Control: Use GitHub or GitLab for version control. Create branches for each feature and conduct code reviews before merging.
Task Management: Use a project management tool like Trello or Asana to assign and track tasks.
Learning Resources: Share resources for Django, Python, and front-end design to help beginners get up to speed.
For Python: Python Beginner Tutorial
For Django: Official Django Documentation
For CSS/HTML: W3Schools HTML/CSS
Weekly Meetings: Conduct weekly meetings to discuss progress, blockers, and next steps.
By dividing the tasks based on expertise and providing learning opportunities, this project can be completed effectively while ensuring everyone contributes meaningfully! Let me know if you need further clarification or resources.







