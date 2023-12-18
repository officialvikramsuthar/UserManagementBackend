User Management Project Setup Guide Introduction Welcome to the User Management Project! This project is built using Django and Django Rest Framework, featuring Celery integration for asynchronous tasks and MongoDB for logging user actions.

Table of Contents Requirements Local Setup

Requirements: Make sure you have the following installed on your machine: PIP Python (3.x recommended) Django Django Rest Framework Celery Djongo MongoDB (for logs) Redis (for Celery) Local Setup

Clone the Repository:

git clone https://github.com/yourusername/user-management-project.git cd user-management-project Install Dependencies:

pip install -r requirements.txt Apply Migrations:

python manage.py makemigrations python manage.py migrate Create a Django Superuser:

python manage.py createsuperuser Run the Development Server:

python manage.py runserver Access the admin interface at http://127.0.0.1:8000/admin/ and the API at http://127.0.0.1:8000/api/.
