# Django Projects

A single portfolio repository that combines five Django learning projects previously kept as separate repos.

**Author:** [Nabila Tajrin](https://github.com/nabilatajrin)

---

## Projects included

| Folder | Original repo | Description |
|--------|---------------|-------------|
| [`01-basics-trydjango`](01-basics-trydjango/) | `django` | Early Django practice (pages, products, templates) |
| [`02-blog-application`](02-blog-application/) | `django-blog-application` | Simple blog: create, edit, delete posts |
| [`03-note-taking-app`](03-note-taking-app/) | `django-note-taking-app` | Todo / note-taking Django app |
| [`04-profiles-rest-api`](04-profiles-rest-api/) | `django-profiles-rest-api` | User profiles REST API |
| [`05-weight-rest-api`](05-weight-rest-api/) | `django-rest-api-for-weight` | Weight tracking REST API |

Virtual environments (`venv`, `myvenv`, etc.) and IDE folders were **not** copied. Use a fresh virtualenv per project.

---

## Requirements

- Python 3.6+ (projects were written around older Django; newer Python may need dependency bumps)
- `pip` / virtualenv (or Pipenv where a `Pipfile` is present)

---

## How to run a project

Example for the blog app:

```bash
cd 02-blog-application
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install django         # or: pipenv install
python manage.py migrate
python manage.py runserver
```

For projects with `requirements.txt`:

```bash
pip install -r requirements.txt
```

For projects with `Pipfile`:

```bash
pip install pipenv
pipenv install
pipenv run python manage.py runserver
```

---

## Project notes

### 01 – Basics (TryDjango)
Introductory project with `pages` and `products` apps and basic templates (`home`, `about`, `contact`).

### 02 – Blog application
Blog with post CRUD. Uses Pipenv. Templates under `templates/`.

### 03 – Note-taking app
Contains `django_app` (todo) and `mysite` layouts from the original practice structure.

### 04 – Profiles REST API
Django REST Framework style profiles API (`profiles_api` + `profiles_project`). See `requirements.txt`.

### 05 – Weight REST API
REST API around a weight-related `MyApp` model.

---

## Why this repo exists

These apps were split across five repositories (`django`, `django-blog-application`, `django-note-taking-app`, `django-profiles-rest-api`, `django-rest-api-for-weight`). Merging them:

- Reduces clutter on the GitHub profile
- Avoids the generic name `django` (clashes with the official Django org)
- Keeps each app isolated in its own folder
- Drops committed virtualenvs from this new repo

The original repositories can be **archived or deleted** after you verify everything here.

---

## Original repositories (before merge)

- https://github.com/nabilatajrin/django
- https://github.com/nabilatajrin/django-blog-application
- https://github.com/nabilatajrin/django-note-taking-app
- https://github.com/nabilatajrin/django-profiles-rest-api
- https://github.com/nabilatajrin/django-rest-api-for-weight

---

## License

Learning / portfolio code. Use and adapt freely.
