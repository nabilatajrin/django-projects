# Import full sources from the original repositories

This monorepo already includes:

- Root `README.md` and `.gitignore`
- Folder structure for all five projects
- Core files (`manage.py`, models, some views)

The original apps still live in separate repos. To **copy the remaining source** into this repo (excluding virtualenvs), run locally:

```bash
git clone https://github.com/nabilatajrin/django-projects.git
cd django-projects

# Blog
git clone --depth 1 https://github.com/nabilatajrin/django-blog-application.git /tmp/d-blog
rsync -a --exclude='.git' --exclude='.idea' --exclude='__pycache__' /tmp/d-blog/src/ 02-blog-application/

# Notes
git clone --depth 1 https://github.com/nabilatajrin/django-note-taking-app.git /tmp/d-notes
rsync -a --exclude='.git' --exclude='.idea' --exclude='venv' --exclude='lib' --exclude='bin' --exclude='include' \
  /tmp/d-notes/django_app /tmp/d-notes/mysite /tmp/d-notes/Pipfile* 03-note-taking-app/

# Profiles
git clone --depth 1 https://github.com/nabilatajrin/django-profiles-rest-api.git /tmp/d-prof
rsync -a --exclude='.git' --exclude='.idea' --exclude='venv' --exclude='.vagrant' \
  /tmp/d-prof/profiles_api /tmp/d-prof/profiles_project /tmp/d-prof/manage.py /tmp/d-prof/requirements.txt \
  04-profiles-rest-api/

# Weight
git clone --depth 1 https://github.com/nabilatajrin/django-rest-api-for-weight.git /tmp/d-weight
rsync -a --exclude='.git' --exclude='.idea' --exclude='myvenv' --exclude='env' \
  /tmp/d-weight/django_rest_api/ 05-weight-rest-api/

# Basics (TryDjango)
git clone --depth 1 https://github.com/nabilatajrin/django.git /tmp/d-basic
rsync -a --exclude='.git' --exclude='.idea' --exclude='lib' --exclude='bin' --exclude='include' --exclude='share' \
  /tmp/d-basic/Dev/trydjango/src/ 01-basics-trydjango/

git add .
git commit -m "Import full sources from original Django repos (no venvs)"
git push
```

After verifying, archive or delete the five old repositories in GitHub Settings so your profile only shows **django-projects**.
