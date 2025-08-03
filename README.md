# student-management# Study Management System

A comprehensive Django-based web application for managing study records and academic activities, built with modern web technologies and deployed on Vercel.

## 🚀 Features

- **Study Record Management**: Add, view, edit, and delete study records
- **Academic Activity Tracking**: Monitor study progress and activities
- **Search & Filter**: Find study records quickly with search functionality
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Admin Panel**: Django admin interface for advanced management
- **Secure**: Production-ready security configurations

## 🛠️ Tech Stack

- **Backend**: Django 4.x
- **Database**: SQLite (development & production)
- **Frontend**: HTML, CSS, JavaScript
- **Static Files**: WhiteNoise for static file serving
- **Deployment**: Vercel
- **Python**: 3.9+

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.9 or higher
- pip (Python package installer)
- Git
- Vercel CLI (for deployment)

## 🔧 Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd student-management-main
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the root directory:
```env
DEBUG=True
SECRET_KEY=your-development-secret-key-here
```

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 8. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the application.

## 🌐 Deployment

### Deploy to Vercel

1. **Install Vercel CLI**:
```bash
npm i -g vercel
```

2. **Login to Vercel**:
```bash
vercel login
```

3. **Configure Environment Variables**:
Set these in your Vercel dashboard:
- `DEBUG=False`
- `SECRET_KEY=your-production-secret-key`

4. **Deploy**:
```bash
vercel --prod
```

### Vercel Configuration
The project includes a `vercel.json` file with optimized settings for Django deployment.

## 📁 Project Structure

```
student-management-main/
├── studyManagement/          # Main Django project
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL configuration
│   └── wsgi.py              # WSGI application
├── studies/                 # Main app
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   ├── static/              # CSS, JS, images
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   └── urls.py              # App URLs
├── static/                  # Global static files
├── staticfiles/             # Collected static files
├── requirements.txt         # Python dependencies
├── vercel.json              # Vercel configuration
├── manage.py                # Django management script
└── README.md                # This file
```

## 🔐 Security Features

- Environment-based configuration
- Secure secret key management
- HTTPS enforcement in production
- CSRF protection
- XSS protection
- Content type sniffing protection
- Secure cookies in production

## 📚 Usage

### Adding Study Records
1. Navigate to the main page
2. Click "Add Study Record" button
3. Fill in the study details
4. Submit the form

### Managing Study Records
1. View all study records on the main dashboard
2. Use search functionality to find specific records
3. Click "Edit" to modify study information
4. Click "Delete" to remove study records

### Admin Panel
Access the Django admin at `/admin/` with superuser credentials for advanced study record management.

## 🐛 Troubleshooting

### Common Issues

**Static files not loading:**
```bash
python manage.py collectstatic --noinput
```

**Database issues:**
```bash
python manage.py makemigrations
python manage.py migrate
```

**Deployment checks:**
```bash
python manage.py check --deploy
```

### Environment Variables
Make sure these are set in production:
- `DEBUG=False`
- `SECRET_KEY=your-secure-secret-key`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/Ajaykumar-dev-07)
- Email: your.ajaydemowork@gmail.com

## 🙏 Acknowledgments

- Django Documentation
- Vercel for hosting
- WhiteNoise for static file serving
- Bootstrap for responsive design

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Ajaykumar-dev-07/study-management-system/issues) page
2. Create a new issue with detailed description
3. Contact the maintainer

---

⭐ **Star this repository if you find it helpful!**