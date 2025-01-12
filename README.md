Wienext Project
Wienext is a personalized skill-learning platform that leverages AI-driven recommendations, providing users with tailored learning roadmaps, video recommendations, and an intuitive onboarding experience. The platform integrates advanced machine learning models, YouTube video recommendations, and user-friendly interfaces.

Directory Structure
plaintext
Copy code
wienext/
├── roadmaps/
│   ├── static/
│   │   ├── css/
│   │   │   └── roadmap.css          # CSS for roadmap pages
│   │   └── js/
│   │       └── roadmap.js           # JavaScript for roadmap interactivity
│   ├── templates/
│   │   ├── roadmap_detail.html      # Template for detailed roadmap view
│   │   └── roadmap_list.html        # Template for listing available roadmaps
│   ├── __init__.py                  # Package initialization
│   ├── models.py                    # Database models for roadmaps
│   ├── urls.py                      # URL routing for roadmap views
│   └── views.py                     # Views for handling roadmap requests
├── skill_learning/
│   ├── api/
│   │   ├── urls.py                  # API endpoint definitions
│   │   └── views.py                 # API views for handling requests
│   ├── models/
│   │   ├── ncf_recommendation.py    # Neural Collaborative Filtering model
│   │   └── tfidf_recommendation.py  # TF-IDF recommendation model
│   ├── utils/
│   │   ├── data_preprocessing.py    # Functions for cleaning and preparing data
│   │   └── model_helpers.py         # Helper functions for model training and evaluation
│   ├── youtube_recommendation.py    # YouTube video recommendation logic
│   └── video_recommendation.py      # Generic video recommendation handling
├── users/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css            # CSS for user dashboard and onboarding
│   │   └── js/
│   │       └── script.js            # JavaScript for user interactions
│   ├── templates/
│   │   ├── dashboard.html           # User dashboard template
│   │   ├── onboarding.html          # Onboarding process template
│   │   └── roadmap_list.html        # Roadmap listing template for users
│   ├── __init__.py                  # Package initialization
│   ├── ai_onboarding.py             # AI logic for onboarding personalization
│   ├── forms.py                     # Django forms for user input
│   ├── models.py                    # User-related database models
│   ├── urls.py                      # URL routing for user views
│   └── views.py                     # Views for handling user requests
├── templates/
│   ├── base.html                    # Base template for common layout
│   └── common_layout.html           # Common layout template for the site
├── db.sqlite3                       # SQLite database file
├── Dockerfile                       # Docker configuration for containerization
├── manage.py                        # Django's command-line utility
├── README.md                        # Project documentation
├── requirements.txt                 # Python dependencies for the project
└── tests.py                         # Test cases for the application
Code Description
roadmaps/
Static Files: Contains CSS and JS specific to the roadmap features.
Templates: HTML files for displaying roadmaps and details.
Models: Defines the structure of the roadmap data.
Views: Handles requests related to roadmaps, such as viewing and listing roadmaps.
skill_learning/
API: Defines RESTful endpoints for interacting with the recommendation system.
Models: Contains the recommendation models (NCF and TF-IDF) used for suggesting skills and resources.
Utils: Functions for data preprocessing and model assistance.
YouTube Recommendation: Logic to fetch and recommend YouTube videos based on user preferences.
Video Recommendation: General logic for handling video recommendations.
users/
Static Files: CSS and JS for user-facing pages like the dashboard and onboarding.
Templates: HTML files for user interactions, including onboarding and dashboards.
AI Onboarding: Implements AI-driven personalization for new users.
Forms: Handles user input forms.
Models: Defines user-related data structures.
Views: Manages user requests and interactions.
templates/
Base Templates: Common layout files to maintain consistency across the site.
db.sqlite3
SQLite database storing application data.
Dockerfile
Configuration for containerizing the application using Docker.
manage.py
Django’s command-line utility for project management.
requirements.txt
Lists all Python dependencies required for the project.
tests.py
Contains unit tests to ensure the integrity of the application.
Setup Instructions
Clone the Repository:

bash
Copy code
git clone https://github.com/your-repo/wienext.git
cd wienext
Install Dependencies: Ensure Python 3.8+ and pip are installed. Then run:

bash
Copy code
pip install -r requirements.txt
Database Setup: Run migrations to set up the database schema:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the Server: Start the Django development server:

bash
Copy code
python manage.py runserver
Access the Application: Open a browser and navigate to http://localhost:8000.

Team Member Deliverables
Backend Developers
Enhance API Functionality: Implement additional endpoints in skill_learning/api/views.py.
Model Optimization: Improve performance of the NCF and TF-IDF models in skill_learning/models/.
AI Onboarding: Refine the onboarding logic in users/ai_onboarding.py to better personalize user experiences.
Frontend Developers
UI Enhancements: Update users/templates/dashboard.html and onboarding.html for a more intuitive interface.
Interactive Features: Enhance user interactivity through users/static/js/script.js.
Data Scientists
Model Development: Explore additional recommendation models and integrate them into skill_learning/models/.
Data Preprocessing: Enhance skill_learning/utils/data_preprocessing.py for more robust data handling.
Project Managers
Documentation: Ensure all code is well-documented, and maintain an updated README.md.
Testing: Oversee the creation and execution of test cases in tests.py.
Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License.

