# Django Projects

A single portfolio repository that combines **five** Django learning projects previously kept as separate repos.

**Author:** [Nabila Tajrin](https://github.com/nabilatajrin)  
**Repo:** https://github.com/nabilatajrin/django-projects

---

## Projects included

| Folder | Original repo | Description |
|--------|---------------|-------------|
| [`01-basics-trydjango`](01-basics-trydjango/) | `django` | Early Django practice (pages, products, templates) |
| [`02-blog-application`](02-blog-application/) | `django-blog-application` | Simple blog: create, edit, delete posts |
| [`03-note-taking-app`](03-note-taking-app/) | `django-note-taking-app` | Todo / note-taking Django app |
| [`04-profiles-rest-api`](04-profiles-rest-api/) | `django-profiles-rest-api` | User profiles REST API |
| [`05-weight-rest-api`](05-weight-rest-api/) | `django-rest-api-for-weight` | Weight tracking REST API |

Virtual environments and IDE metadata are **not** part of this repo. Use a fresh `venv` per project.

See [IMPORT_SOURCES.md](IMPORT_SOURCES.md) if you need to pull any remaining files from the original repos.

---

## Requirements

- Python 3.6+ (these projects used older Django; bump packages if needed on newer Python)
- `pip` + virtualenv, or Pipenv where a `Pipfile` exists

---

## How to run a project

```bash
cd 02-blog-application   # or any other project folder
python3 -m venv venv
source venv/bin/activate
pip install django       # or: pip install -r requirements.txt / pipenv install
python manage.py migrate
python manage.py runserver
```

---

## Why merge?

| Before | After |
|--------|--------|
| 5 separate Django repos | 1 clear **django-projects** repo |
| Generic name `django` (clashes with official Django) | Meaningful portfolio name |
| Virtualenvs committed in some repos | Clean tree, no `venv` |

After you are happy with this repo, archive or delete:

- https://github.com/nabilatajrin/django
- https://github.com/nabilatajrin/django-blog-application
- https://github.com/nabilatajrin/django-note-taking-app
- https://github.com/nabilatajrin/django-profiles-rest-api
- https://github.com/nabilatajrin/django-rest-api-for-weight

That reduces your total public repo count by **4** (5 removed, 1 added).

---

## License

Learning / portfolio code. Use and adapt freely.
