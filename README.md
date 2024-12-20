# django-contact-book
A web-based contact management system built with Django and MySQL. Features include adding, editing, soft-deleting, and searching contacts with fast performance. Contacts are displayed with pagination, sorted by Full Name. Scalable to 1 million contacts with a clean UI and unit tests.

# Introduction
The Contact Manager project is a web-based application built using the Django framework. It allows users to manage contacts efficiently, with features for adding, editing, viewing, and deleting contacts. The project is structured using Django’s standard project and app architecture, which separates concerns for better maintainability and scalability.

Project Folder: The contact_manager/ directory contains essential project configurations such as settings.py, URL routing in urls.py, and WSGI settings in wsgi.py for deployment.

App Folder: The contacts/ directory is the core application, which handles the contact management functionalities. It includes:

Models (models.py) for defining the Contact model.
Views (views.py) to handle business logic for each operation (CRUD).
Templates for the front-end structure, including pages for creating, updating, deleting, and listing contacts.
Admin Configuration (admin.py) to register models for the Django admin interface.
Tests (tests.py) to ensure that the application runs correctly.
Migrations: The migrations/ folder stores the database schema changes, ensuring the app's models are synced with the database.


  
