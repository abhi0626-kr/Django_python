# Django Blog Project

This is a small Django blog application built while learning Python Django.

## Purpose

I’m doing this project to learn Python Django by practicing:

- project setup
- models and migrations
- templates and static files
- views and URLs
- working with a MySQL database

## Features

- blog post listing page
- post detail page
- reusable base template
- static CSS styling
- slug support for posts

## Tech Stack

- Python
- Django
- MySQL
- HTML/CSS

## Setup

1. Activate the virtual environment:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   python -m pip install Django mysqlclient
   ```

3. Run migrations:

   ```powershell
   python manage.py migrate
   ```

4. Start the development server:

   ```powershell
   python manage.py runserver
   ```

## Notes

- Make sure MySQL is running before starting the app.
- Database settings are configured in `myapp/settings.py`.
- Static files are stored in `blog/static/blog/`.

## Project Goal

The main goal of this project is to learn Django through hands-on practice and build confidence with core web development concepts in Python.
