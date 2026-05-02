# Modern Blog

A Django-based blog application with user authentication, rich text editing, AI-powered chatbot, and media management.

## 📋 Table of Contents

- [Project Architecture](#project-architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Local Setup](#local-setup)
- [Running the Application](#running-the-application)
- [Features](#features)

## 🏗️ Project Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Frontend Layer                    │
│         (HTML Templates, CSS, JavaScript)            │
└────────────────┬────────────────────────────────────┘
                 │
┌────────────────▼────────────────────────────────────┐
│                   Django Framework                   │
│  ┌──────────────────────────────────────────────┐   │
│  │            URL Router (urls.py)               │   │
│  └──────────────────────────────────────────────┘   │
└────────────────┬────────────────────────────────────┘
                 │
    ┌────────────┼────────────┬──────────────┐
    │            │            │              │
┌───▼────┐  ┌───▼────┐  ┌───▼────┐  ┌────▼────┐
│Accounts│  │  Blog  │  │Chatbot │  │  Admin  │
│  App   │  │  App   │  │  App   │  │ Panel   │
└────────┘  └────────┘  └────────┘  └─────────┘
    │            │            │
┌───▼────────────▼────────────▼──────────────┐
│         Models & ORM (Database)             │
│  ┌──────────────────────────────────────┐  │
│  │     SQLite (db.sqlite3)              │  │
│  └──────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

### Applications Overview

#### 1. **Accounts App** (`accounts/`)
- **Purpose**: User authentication and profile management
- **Models**: User profiles, OTP verification
- **Views**: Registration, login, profile management, OTP verification
- **Features**:
  - User registration with email verification
  - OTP-based authentication
  - User profile management
  - Password management

#### 2. **Blog App** (`blog/`)
- **Purpose**: Blog post management and publishing
- **Models**: Blog posts, categories, tags
- **Views**: Post list, post detail, post creation, post update, post deletion
- **Features**:
  - Create, read, update, delete (CRUD) blog posts
  - Rich text editing with TinyMCE
  - Media upload support (images, files)
  - Post categorization and filtering

#### 3. **Chatbot App** (`chatbot/`)
- **Purpose**: AI-powered chatbot functionality
- **Integration**: Google Generative AI API
- **Features**:
  - Real-time chat interactions
  - AI-powered responses using Google's Generative AI
  - Conversation history

#### 4. **Core Project** (`modern_blog/`)
- **Purpose**: Main Django project settings and configuration
- **Files**:
  - `settings.py`: Django configuration
  - `urls.py`: Main URL router
  - `wsgi.py`: WSGI application for production
  - `asgi.py`: ASGI application for async support

## 💻 Tech Stack

| Component | Version | Purpose |
|-----------|---------|---------|
| **Django** | 6.0.4 | Web framework |
| **Python** | 3.13 | Programming language |
| **SQLite** | Latest | Database (development) |
| **TinyMCE** | 5.0.0 | Rich text editor |
| **Google Generative AI** | 0.8.6 | AI chatbot integration |
| **Pillow** | 12.2.0 | Image processing |
| **Gunicorn** | 25.3.0 | WSGI HTTP server |
| **Whitenoise** | 6.12.0 | Static file serving |
| **python-dotenv** | 1.2.2 | Environment variables |

## 📁 Project Structure

```
modern_blog/
├── README.md                      # Project documentation
├── manage.py                      # Django management script
├── db.sqlite3                     # SQLite database
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore rules
│
├── modern_blog/                   # Project configuration
│   ├── __init__.py
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Main URL configuration
│   ├── wsgi.py                   # WSGI configuration
│   └── asgi.py                   # ASGI configuration
│
├── accounts/                      # User authentication app
│   ├── migrations/               # Database migrations
│   ├── models.py                 # User models
│   ├── views.py                  # Authentication views
│   ├── forms.py                  # User forms
│   ├── urls.py                   # Account URLs
│   ├── admin.py                  # Admin interface
│   ├── apps.py                   # App configuration
│   ├── signals.py                # Django signals
│   └── tests.py                  # Unit tests
│
├── blog/                          # Blog posting app
│   ├── migrations/               # Database migrations
│   ├── models.py                 # Post, Category models
│   ├── views.py                  # Blog views
│   ├── forms.py                  # Post forms
│   ├── urls.py                   # Blog URLs
│   ├── admin.py                  # Admin interface
│   ├── apps.py                   # App configuration
│   └── tests.py                  # Unit tests
│
├── chatbot/                       # AI chatbot app
│   ├── migrations/               # Database migrations
│   ├── models.py                 # Chat models
│   ├── views.py                  # Chatbot views
│   ├── urls.py                   # Chatbot URLs
│   ├── admin.py                  # Admin interface
│   ├── apps.py                   # App configuration
│   └── tests.py                  # Unit tests
│
├── templates/                     # HTML templates
│   ├── base.html                 # Base template
│   ├── landing.html              # Landing page
│   ├── accounts/                 # Account templates
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── profile.html
│   │   └── verify_otp.html
│   └── blog/                     # Blog templates
│       ├── post_list.html
│       ├── post_detail.html
│       ├── post_form.html
│       └── post_confirm_delete.html
│
├── static/                        # Static files
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── media/                         # User uploaded files
│   ├── posts/
│   └── profiles/
│
└── env-blog/                      # Virtual environment
    ├── Scripts/                  # Executable scripts
    ├── Lib/                      # Python packages
    └── pyvenv.cfg               # Virtual env config
```

## 🚀 Local Setup

### Prerequisites

- Python 3.13+
- pip (Python package manager)
- Git

### Installation Steps

#### 1. Clone the Repository
```bash
git clone <repository-url>
cd modern_blog
```

#### 2. Create Virtual Environment
```bash
# On Windows PowerShell
python -m venv env-blog

# Activate virtual environment
.\env-blog\Scripts\Activate.ps1

# On macOS/Linux
python3 -m venv env-blog
source env-blog/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Environment Variables
Create a `.env` file in the project root:
```env
# Django
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Google Generative AI
GOOGLE_API_KEY=your-google-api-key-here

# Database (optional)
# DATABASE_URL=sqlite:///db.sqlite3

# Email Configuration (optional)
# EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
# EMAIL_HOST=smtp.gmail.com
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER=your-email@gmail.com
# EMAIL_HOST_PASSWORD=your-app-password
```

#### 5. Database Setup
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser for admin panel
python manage.py createsuperuser
```

#### 6. Create Necessary Directories
```bash
# Create media directories if they don't exist
mkdir -p media/posts
mkdir -p media/profiles
```

#### 7. Collect Static Files (for production)
```bash
python manage.py collectstatic --noinput
```

## ▶️ Running the Application

### Development Server

```bash
# Make sure virtual environment is activated
python manage.py runserver

# Server will be available at: http://127.0.0.1:8000/
```

### Access Admin Panel
1. Navigate to: `http://127.0.0.1:8000/admin/`
2. Login with superuser credentials created during setup

### Production with Gunicorn

```bash
gunicorn modern_blog.wsgi:application --bind 0.0.0.0:8000
```

## ✨ Features

### User Authentication
- ✅ User registration with email verification
- ✅ Secure login/logout
- ✅ OTP-based authentication
- ✅ User profile management
- ✅ Password reset

### Blog Management
- ✅ Create, edit, delete blog posts
- ✅ Rich text editing with TinyMCE
- ✅ Image and file uploads
- ✅ Post categorization
- ✅ Post search and filtering

### Chatbot
- ✅ AI-powered responses using Google Generative AI
- ✅ Real-time chat interface
- ✅ Conversation history

### Admin Panel
- ✅ Manage users
- ✅ Manage blog posts
- ✅ Manage chatbot conversations

## 🔧 Common Commands

```bash
# Run development server
python manage.py runserver

# Create new app
python manage.py startapp app_name

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Django shell
python manage.py shell

# Collect static files
python manage.py collectstatic
```

## 📝 Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `DEBUG` | Enable/disable debug mode | `True` or `False` |
| `SECRET_KEY` | Django secret key | `your-secret-key` |
| `ALLOWED_HOSTS` | Allowed hosts | `localhost,127.0.0.1` |
| `GOOGLE_API_KEY` | Google Generative AI API key | `your-api-key` |
| `DATABASE_URL` | Database connection string | `sqlite:///db.sqlite3` |

## 🐛 Troubleshooting

### Virtual Environment Issues
```bash
# If activation fails on Windows PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Deactivate and reactivate
deactivate
.\env-blog\Scripts\Activate.ps1
```

### Database Issues
```bash
# Reset database (WARNING: This deletes all data)
rm db.sqlite3
python manage.py migrate
```

### Missing Dependencies
```bash
# Reinstall all dependencies
pip install -r requirements.txt --upgrade
```

## 📞 Support

For issues and questions, please create an issue in the repository.

## 📄 License

This project is licensed under the MIT License.

---

**Last Updated**: May 2, 2026
**Django Version**: 6.0.4
**Python Version**: 3.13+
