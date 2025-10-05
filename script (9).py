# 9. Complete setup and documentation files

# Requirements.txt
requirements = '''Django==4.2.7
pandas==2.1.4
scikit-learn==1.3.2
numpy==1.24.3
openpyxl==3.1.2
matplotlib==3.8.2
seaborn==0.13.0
plotly==5.17.0
pillow==10.1.0
'''

# README.md
readme = '''# Student Performance Prediction & Analytics System

A comprehensive web application implementing Data Mining and Warehouse (DMW) concepts for educational analytics.

## Features

### 🎯 Core Functionality
- **Student Performance Prediction** using Decision Tree Classification
- **Clustering Analysis** with K-means algorithm
- **Association Rule Mining** for pattern discovery
- **Interactive Dashboard** with real-time analytics
- **Data Upload & Processing** with automatic cleaning

### 📊 DMW Concepts Implemented
- **Data Preprocessing**: Cleaning, Integration, Transformation, Reduction
- **Classification**: Decision Tree for performance prediction
- **Clustering**: K-means for student grouping
- **Association Rules**: Apriori algorithm for relationship discovery
- **Data Warehouse**: Star schema with fact and dimension tables
- **OLAP Operations**: Slice, dice, roll-up, drill-down capabilities

## Technology Stack
- **Backend**: Django 4.2
- **Frontend**: Bootstrap 5, Chart.js
- **Database**: SQLite (development), MySQL (production)
- **ML Libraries**: scikit-learn, pandas, numpy
- **Visualization**: Chart.js, Plotly

## Installation

### Prerequisites
- Python 3.9+
- pip package manager

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/student-analytics.git
cd student-analytics
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser**
```bash
python manage.py createsuperuser
```

6. **Start development server**
```bash
python manage.py runserver
```

7. **Access application**
- Main application: http://127.0.0.1:8000
- Admin panel: http://127.0.0.1:8000/admin

## Usage

### 1. Data Upload
- Navigate to "Upload Data" section
- Upload student dataset (CSV/Excel format)
- System automatically cleans and processes data

### 2. Performance Prediction
- Use the dashboard prediction form
- Enter student parameters (attendance, study hours, etc.)
- Get AI-powered performance predictions

### 3. Analytics Dashboard
- View performance distribution charts
- Analyze clustering results
- Explore association rules

### 4. Reports & Insights
- Generate comprehensive reports
- Export analysis results
- Visualize data patterns

## Dataset Format

Expected columns in uploaded dataset:
- **Student Info**: Gender, Age, Semester, Admission Year
- **Academic**: CGPA, SGPA, Credits, Attendance
- **Behavioral**: Study Hours, Social Media Usage, Skills
- **Personal**: Family Income, Living Arrangement, Health

## Project Structure
```
student_analytics/
├── analytics/              # Main Django app
│   ├── models.py          # Database models
│   ├── views.py           # Application views
│   ├── urls.py            # URL routing
│   └── templates/         # HTML templates
├── static/                # Static files (CSS, JS)
├── media/                 # Uploaded files
├── ml_algorithms.py       # Machine learning implementations
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## DMW Concepts Demonstration

### 1. Data Preprocessing
- **Data Cleaning**: Handle missing values, outliers
- **Data Integration**: Combine multiple data sources
- **Data Transformation**: Normalize, encode categorical variables
- **Data Reduction**: Feature selection and dimensionality reduction

### 2. Classification (Decision Tree)
```python
# Example usage
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(max_depth=10)
classifier.fit(X_train, y_train)
predictions = classifier.predict(X_test)
```

### 3. Clustering (K-means)
```python
# Example usage
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)
```

### 4. Association Rules
- Implemented using frequency analysis
- Discovers patterns like "High Attendance → Good Performance"
- Calculates support, confidence, and lift metrics

### 5. Data Warehouse Design
- **Fact Table**: Student performance facts
- **Dimension Tables**: Student, Subject, Time, Demographics
- **Star Schema**: Optimized for OLAP queries

## API Endpoints

- `GET /` - Home page
- `GET /dashboard/` - Analytics dashboard
- `POST /upload/` - Data upload endpoint
- `POST /api/predict/` - Performance prediction API
- `GET /association-rules/` - Association rules analysis
- `GET /clustering/` - Clustering results

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Authors

- Your Name - Initial work - [YourGitHub](https://github.com/yourusername)

## Acknowledgments

- Data Mining and Warehouse course curriculum
- scikit-learn documentation
- Django framework documentation
- Bootstrap framework for responsive design
'''

# manage.py
manage_py = '''#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

if __name__ == '__main__':
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_analytics.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
'''

# Save setup files
with open('requirements.txt', 'w') as f:
    f.write(requirements)

with open('README.md', 'w') as f:
    f.write(readme)

with open('manage.py', 'w') as f:
    f.write(manage_py)

print("Setup and documentation files created successfully!"))