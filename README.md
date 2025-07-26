# SimorghCMS

<div align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
</div>

<div align="center">
  <h3>A Modern and Powerful Content Management System</h3>
  <p>Built with FastAPI and Pure HTML/CSS/JS</p>
</div>

## 📋 Project Overview

SimorghCMS is a modern, fast, and user-friendly Content Management System inspired by WordPress. This CMS is built using modern technologies like FastAPI and provides advanced features such as user management, articles, categories, and comments management.

## 🚀 Features

### Backend (FastAPI)
- ✅ JWT Authentication System
- ✅ User Management with Different Roles (Admin, Editor, Author, Subscriber)
- ✅ Create, Edit, and Delete Articles
- ✅ Article Categorization and Tagging
- ✅ Comment System with Status Management
- ✅ Media File Upload and Management
- ✅ Documented API with Swagger and ReDoc
- ✅ Asynchronous Database with SQLAlchemy
- ✅ High Security and Data Validation

### Frontend (Pure HTML/CSS/JS)
- ✅ Responsive and Modern Design
- ✅ Advanced User Dashboard
- ✅ Article and Comment Management
- ✅ User Profile Management
- ✅ Multi-language Support (Persian/English)
- ✅ High Performance and Speed
- ✅ No Heavy Framework Dependencies
- ✅ Clean and Intuitive User Interface

## 🛠️ Technologies

### Backend
- **FastAPI** - High-performance Python web framework
- **SQLAlchemy** - Python ORM for database operations
- **SQLite** - Lightweight and portable database
- **JWT** - Secure tokens for authentication
- **Alembic** - Database migration tool
- **Pydantic** - Data validation and settings management

### Frontend
- **HTML5** - Markup language for web pages
- **CSS3** - Styling and responsive design
- **JavaScript (ES6+)** - Client-side scripting
- **Fetch API** - Modern HTTP client for API calls
- **No Framework Dependencies** - Pure vanilla JavaScript

## 📦 Installation and Setup

### Prerequisites
- Python 3.8+
- pip
- Git

### Backend Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/SimorghCMS.git
cd SimorghCMS

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create database
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### Running the Backend

```bash
# Run development server
uvicorn app.main:app --reload

# Server will be available at http://localhost:8000
```

### Frontend Setup

```bash
# Create static directory for frontend files
mkdir -p static/frontend

# Copy frontend files to static directory
cp -r frontend/* static/frontend/
```

### Running the Frontend (for development)

```bash
# From the project root directory
python -m http.server 3000

# Frontend will be available at http://localhost:3000
```

## 📚 API Documentation

After starting the server, you can access the API documentation:

- **Swagger UI**: `http://localhost:8000/api/docs`
- **ReDoc**: `http://localhost:8000/api/redoc`

## 🗂️ Project Structure

```
SimorghCMS/
├── app/
│   ├── api/          # API endpoints
│   ├── core/         # Core configurations and security
│   ├── crud/         # Database operations
│   ├── database/     # Database configuration
│   ├── models/       # Database models
│   ├── schemas/      # Pydantic schemas
│   └── main.py       # Main application file
├── frontend/         # Frontend files (lightweight version)
├── static/           # Static files
├── alembic/          # Migration files
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## 🔧 Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=sqlite+aiosqlite:///./cms.db
SECRET_KEY=your-super-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 🐳 Docker Deployment

```bash
# Build and run with Docker
docker-compose up --build
```

## 🚀 Production Deployment

### With Nginx

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /api/ {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

## 📖 Usage Guide

### First Admin User

After first run, create an admin user:

1. Visit `http://localhost:8000`
2. Click on "Register"
3. Enter your user information
4. Change the user role to "admin" in the database

### Creating Articles

1. Log in to your account
2. Go to the dashboard
3. Click on "Create New Article"
4. Enter article information and publish

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the GNU License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the excellent framework
- [Python](https://www.python.org/) community
- Open source community

## 📞 Contact

SimorghCMS Project - [@shythonx](https://t.me/shythonx) - shayanheidari01@gmail.com

Project Link: [SimorghCMS](https://github.com/shayanheidari01/SimorghCMS)

---

<div align="center">
  <p>Made with ❤️ and Python</p>
  <p>© 2023 SimorghCMS. All rights reserved.</p>
</div>
