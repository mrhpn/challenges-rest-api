# Django CSV to JSON API

This is a Django project that reads data from a CSV file and exposes it as a
JSON API.

## Demo (Screenshot)

![screenshot](/demo/screenshot-1.png)

## Prerequisites

- Python 3.x
- pip

## Folder Structure

```
myproject/
├── challenges/               # Django app for the API
│   ├── migrations/           # Database migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── myproject/                # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── data/                     # Folder for CSV files
│   └── challenges.csv
├── .gitignore                # Files and folders to ignore
├── manage.py                 # Django management script
├── README.md                 # Project documentation
└── requirements.txt          # Project dependencies
```

## Setup Instructions

1. Clone the repo

```
git clone --url--
```

2. Create a virtual environment

```
python3 -m venv myenv
```

3. Activate the virtual environment:

```
source myenv/bin/activate
```

4. Install dependencies:

```
pip install -r requirements.txt
```

5. Run server:

```
python manage.py runserver
```

6. Test the API

```
http://127.0.0.1:8000/api/challenges
```
