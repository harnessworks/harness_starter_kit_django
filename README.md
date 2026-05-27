# Django Project

This repository contains a Django project initialized with the project package
`config` and the app package `harness_starter_kit_django`.

The app currently provides a simple public 게시판 CRUD:

- `/`: 게시글 목록
- `/posts/new/`: 게시글 작성
- `/posts/<id>/`: 게시글 상세
- `/posts/<id>/edit/`: 게시글 수정
- `/posts/<id>/delete/`: 게시글 삭제

## Setup

Create or refresh the local virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Local Commands

Run Django system checks:

```powershell
.\.venv\Scripts\python.exe manage.py check
```

Run tests:

```powershell
.\.venv\Scripts\python.exe manage.py test
```

Apply local SQLite migrations:

```powershell
.\.venv\Scripts\python.exe manage.py migrate
```

Create a superuser for admin access:

```powershell
.\.venv\Scripts\python.exe manage.py createsuperuser
```

Start the development server:

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

Run repository harness checks:

```powershell
.\.venv\Scripts\python.exe scripts\check_harness.py
```
