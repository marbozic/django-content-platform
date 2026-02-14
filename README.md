# Django Platform Starter

Production-minded Django starter focused on scalable, server-rendered architectures with admin governance and SEO-safe publishing workflows.

## Highlights
- Admin-controlled CMS patterns
- Publish gates & validation
- Redirect system (DB-backed)
- Canonical + robots handling
- Sitemap support
- Caching example
- Test coverage
- Management command for page generation

## Stack
- Django 4.x
- PostgreSQL-ready (SQLite for demo)
- Redis-compatible caching
- Docker-ready structure

## Run locally

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `/admin` to explore the CMS patterns.

## Why this repo exists
This is a public-safe reference project demonstrating how I typically structure Django applications when building scalable, content-driven platforms. It intentionally avoids client-specific logic while reflecting real production patterns.
