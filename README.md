# Project Documentation:

# [Sticky Notes] Project

# Django Project

This is a modular sticky notes application built with Python.

This application, built with Django, showcases CRUD capabilities, a responsive design through Bootstrap, and a modular project structure,
and it employs unit testing following the AAA pattern.

________________________________________________________________________________
## Project Structure:
django_projects			       # Project folder dir 
│
├── myVenv
│
└── sticky_notes_project/             # This is the (UPPER) project directory—i.e. Project ROOT folder / dir.
    │
    ├── manage.py                      # Django management script allowing us to interact with the project.
    ├── README.md					   # Django project description.
    ├── .flake8
    ├── .pyproject.toml
    ├── requirements.txt
    ├── .gitignore
    ├── db.sqlite3
    │
    ├── sticky_notes_project/          # Main (CORE) project folder (Contains project settings)
    │   ├── __init__.py
    │   ├── settings.py                # Global configuration (includes installed apps, static files, etc.)
    │   ├── urls.py                    # Main URL dispatcher
    │   ├── wsgi.py
    │   └── asgi.py
    │
    │						
    │				==== # Folders for Django apps START here # ====
    │
    ├── myNotesApp/   # Our sticky notes application called 'myNotesApp'                          
    │   ├── migrations/
    │   │   └── __init__.py
    │   ├── __init__.py
    │   ├── admin.py                # Model registrations for Django admin
    │   ├── apps.py                 # App configuration
    │   ├── models.py               # Note model with title, content, and timestamps
    │   ├── forms.py                # ModelForm for Note
    │   ├── views.py                # CRUD views for the sticky notes (Performs Controller Logic)
    │   ├── urls.py                 # App-specific URL patterns
    │   ├── tests.py                # Unit tests for models and views
    │   ├── static/
    │   │   └── myNotesApp/
    │   │       ├── css/
    │   │       │   └── styles.css  # Custom CSS (with Bootstrap added via CDN in templates)
    │   │       └── js/
    │   │           └── scripts.js   # (Optional) Custom JavaScript
    │   └── templates/
    │       └── myNotesApp/
    │           ├── note_list.html    # Lists all notes
    │           ├── note_detail.html  # Displays a single note
    │           ├── note_form.html    # Form for creating / updating notes
    │           └── note_delete.html  # Note deletion confirmation
    │						
    │				==== # Folders for Django apps END here # ====
    │
    │
    │
    ├── templates/                        # Global templates folder
    │   ├── base.html                     # Base HTML template
    │   └── ...
    │
    └── static/                           # (Optional) Global static files (e.g., CSS, JavaScript, images)
        ├── css/
        ├── js/
        └── images/

________________________________________________________________________________
For .flake8:
[flake8]
max-line-length = 79
exclude = .git,__pycache__,tests,venv
ignore = E203, E266, E501, W503

For .pyproject.toml:
[tool.black]
line-length = 79

________________________________________________________________________________
## Setup Instructions:
1. Create 'django_projects' folder in file explorer.
	"C:\...\django_project" => project folder dir
2. Create a virtual environment - while in project folder dir
	Type: 'python -m venv myVenv' into vs code terminal
2.1. Activate virtual environment
	Type: 'source myVenv/Scripts/activate' into vs code terminal, then
	Type: 'pip freeze' into the vs code term.
3. Install django - still while in project folder dir
	Type: 'pip install django' into the vs code terminal, then
	Type: 'pip freeze' into the vs code term.
4. Create a new django project and application
4.1. Create a new django project:
	Type: 'django-admin startproject sticky_notes_project' into vs code term, while still in proj. folder dir
4.2. Change directory to proj ROOT dir
	Type: 'cd sticky_notes_project' into vs code term
4.3. Create a new Django application:
	Type: 'django-admin startapp myNotesApp' into vs code term
	Type: 'ls' into vs code term
5. Run initial database migrations to set up the database tables:
	Type: 'python manage.py migrate' into the vs code term
6. Create a superuser to access the Django admin interface:
	Type: 'python manage.py createsuperuser' into the vs code term, then,
	Fill in: username, email (rrrr@rrrr.com), password (1234 --this is a fictitious password)
7. Start the Django development server:
	Type: 'python manage.py runserver' into the vs code term, then follow the http://... link in term
8. Create the necessary subfolders and modules where needed within the proj folder dir or proj root dir
9. Edit and populate the different modules and subfolders
10. Install flake8:
	Type: 'pip install flake8' into the vs code term and create and populate the .flake8 file.
11. Install Black:
	Type: 'pip install black' into the vs code term
12. Perform black and flake8 PEP 8 standards. >>> Don't use prettier on HTML, CSS, JavaScript. It causes app errors
13. Run Migrations:
	Open your terminal and execute the following commands in your project’s ROOT directory:
	Type: 'python manage.py makemigrations'
	      'python manage.py migrate' into the vs code term
14. Restart Your Development Server:
	Type: 'python manage.py runserver' into the vs code term, then follow the http://... link in term
15. Use your application and check if it works.
16. Generate requirements.exe file:
	Type: 'pip freeze > requirements.txt' into vs code term, while in proj root dir.
17. Generate README.md file.
NOTE: Perform migrations to ensure that any new changes are reflected in the database, and restart the development server to test your application.


________________________________________________________________________________
Frequently used commands:

django-admin startproject sticky_notes_project


django-admin startapp myNotesApp

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

python manage.py makemigrations
python manage.py migrate

________________________________________________________________________________














