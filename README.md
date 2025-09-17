# Labour Attendance Management System

A comprehensive Django-based web application for managing labour attendance with role-based access control, CSV upload functionality, and Slack-inspired responsive design.

## 🚀 Features

### User Roles & Permissions
- **Master User**: Full system access, manages all companies and users
- **User1 (Company Admin)**: Company-specific management, creates supervisors and employees
- **User2 (Supervisor)**: Manages assigned employees' attendance records
- **User3 (Employee)**: Views personal attendance data and monthly summaries

### Core Functionality
- ✅ Role-based authentication and authorization
- ✅ CSV bulk upload for users and attendance data
- ✅ Responsive Slack-inspired UI design
- ✅ Real-time notifications system
- ✅ Comprehensive audit logging
- ✅ Advanced filtering and search
- ✅ Data export capabilities
- ✅ Date-wise supervisor assignments

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML5, CSS3, Bootstrap 5, Vanilla JavaScript
- **Icons**: Font Awesome 6

## 📋 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Quick Setup
1. **Clone/Download the project**
   ```bash
   cd Django_app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run setup script**
   ```bash
   python setup.py
   ```

4. **Start the development server**
   ```bash
   python manage.py runserver
   ```

5. **Access the application**
   - Open browser: `http://127.0.0.1:8000`
   - Login with: `master` / `master123`

### Manual Setup (Alternative)
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create master user
python manage.py create_master_user

# Collect static files
python manage.py collectstatic

# Start server
python manage.py runserver
```

## 📊 CSV Upload Formats

### Attendance Data Upload
```csv
EP Number,Name,Company Name,Plant,Department,Trade,Skill,Date,IN1,OUT1,IN2,OUT2,IN3,OUT3,Hours Worked,Overtime,Status
EMP001,John Doe,ABC Company,Plant 1,Production,Welder,Skilled,01-01-2024,08:00,17:00,,,,,8.0,0.0,P
```

**Format Requirements:**
- Date: DD-MM-YYYY (e.g., 09-09-2025)
- Time: HH:MM (24-hour format, e.g., 08:30, 17:45)
- Status: P (Present), A (Absent), -0.5 (Half Day), -1 (Full Deduction)

### Bulk User Upload
```csv
Role,EP Number,Name,Company Name,Username,Password,Email,Start Date,End Date,Plant,Department,Trade,Skill
user3,EMP001,John Doe,ABC Company,,,john@abc.com,2024-01-01,,Plant 1,Production,Welder,Skilled
```

**Notes:**
- If Username/Password empty, EP Number will be used for both
- Role values: master, user1, user2, user3
- Date format: YYYY-MM-DD

## 🎯 User Workflows

### Master User Workflow
1. Login to system
2. Create User1 accounts for companies
3. Upload attendance data via CSV
4. Monitor system-wide activities
5. Access audit logs and reports

### User1 (Company Admin) Workflow
1. Create User2 (Supervisor) accounts
2. Create User3 (Employee) accounts
3. Assign employees to supervisors with date ranges
4. Upload company attendance data
5. Monitor company-wide attendance

### User2 (Supervisor) Workflow
1. View assigned employees
2. Edit attendance records (times, overtime, status)
3. Add supervisor remarks
4. Filter and export assigned employee data
5. Receive notifications for attendance issues

### User3 (Employee) Workflow
1. View personal attendance history
2. Check monthly attendance summary
3. Add personal remarks to attendance records
4. Receive notifications about attendance updates

## 🔧 Configuration

### Environment Variables
Create a `.env` file for production:
```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-domain.com
DATABASE_URL=postgresql://user:pass@localhost/dbname
```

### Database Configuration
For production, update `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'labour_management',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📱 Responsive Design

The application features a Slack-inspired responsive design:

### Desktop (1200px+)
- Full sidebar navigation
- Multi-column layouts
- Detailed data tables
- Right panel for details

### Tablet (768px - 1199px)
- Collapsible sidebar
- Two-column layouts
- Compact tables with horizontal scroll

### Mobile (< 768px)
- Bottom navigation tabs
- Single column layout
- Card-based data display
- Touch-friendly interactions

## 🔐 Security Features

- Password hashing with Django's built-in system
- CSRF protection on all forms
- Role-based access control
- Session management
- Audit logging for all actions
- Input validation and sanitization

## 📈 Performance Optimization

- Database query optimization with select_related
- Pagination for large datasets
- Static file compression
- Efficient CSV processing
- Minimal JavaScript for fast loading

## 🚀 Deployment

### Production Checklist
- [ ] Set `DEBUG = False`
- [ ] Configure proper database (PostgreSQL)
- [ ] Set up environment variables
- [ ] Configure static files serving
- [ ] Set up SSL/HTTPS
- [ ] Configure backup strategy
- [ ] Set up monitoring and logging

### Deployment Options
- **Heroku**: Easy deployment with PostgreSQL addon
- **DigitalOcean**: App Platform or Droplet
- **AWS**: EC2 with RDS PostgreSQL
- **VPS**: Any Linux server with Python support

## 🤝 Support

For issues or questions:
1. Check the Django documentation
2. Review the code comments
3. Test with sample CSV files provided
4. Verify user permissions and roles

## 📄 License

This project is developed for internal use. Modify as needed for your organization.

---

**Built with ❤️ using Django and modern web technologies**