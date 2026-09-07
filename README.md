# Introduction  

This is my attempt submitted for homework 1 of AI devtools zoomcamp  

https://github.com/DataTalksClub/ai-dev-tools-zoomcamp  

# Chore Management Tool

A web-based application for managing shared household chores across multiple users and devices. Track one-time and recurring tasks, assign them to team members, and monitor completion status.

## Tech Stack

- **Backend**: Django 5.2 + HTMX - Server-side templating with HTMX for interactive UI
- **Database**: SQLite (file-based, easy setup)
- **Package Management**: uv - Fast Python package installer
- **Testing**: pytest suite
- **Frontend**: HTMX + vanilla HTML/CSS/JS (no heavy frameworks)

## Features

- Multi-user authentication (email/password)
- Shared real-time dashboard
- One-time and recurring chore tracking
- Per-period manual assignment for recurring tasks
- Completion state management (not started → in progress → completed)
- No automatic reminders - manual workflow only

## Getting Started

1. **Install dependencies:**
   ```bash
   uv sync
   ```

2. **Run development server:**
   ```bash
   uv run python manage.py runserver
   ```

3. **Run tests:**
   ```bash
   uv run pytest -v
   ```

4. **Access the app:** http://localhost:8000

## Project Structure

```
src/
├── chore_management/    # Django app initialization
├── config/              # Settings, URLs, and templates
└── manage.py           # CLI entry point
static/                  # Static files
templates/               # Django/HTMX templates
tests/                   # Pytest test suite
_db.sqlite3             # SQLite database (created on first run)
```

## Requirements

- Python 3.13+
- pipx >= 1.0 or uv package manager

## License

MIT
