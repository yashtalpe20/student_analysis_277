# Create Django project structure files

# 1. Django Models (models.py)
models_py = '''from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    gender_choices = [('Male', 'Male'), ('Female', 'Female')]
    gender = models.CharField(max_length=10, choices=gender_choices)
    age = models.IntegerField()
    admission_year = models.IntegerField()
    current_semester = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.roll_no} - {self.name}"

class AcademicRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    current_cgpa = models.FloatField()
    previous_sgpa = models.FloatField()
    credits_completed = models.IntegerField()
    attendance = models.IntegerField()  # percentage
    scholarship = models.BooleanField(default=False)
    probation = models.BooleanField(default=False)
    suspension = models.BooleanField(default=False)
    performance_category = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.student.roll_no} - CGPA: {self.current_cgpa}"

class StudentBehavior(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    study_hours = models.IntegerField()
    study_sessions = models.IntegerField()
    learning_mode = models.CharField(max_length=20)
    social_media_hours = models.IntegerField()
    skill_development_hours = models.IntegerField()
    skills = models.TextField()
    interest_area = models.CharField(max_length=100)
    co_curricular = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.student.roll_no} - Behavior Data"

class Prediction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    predicted_performance = models.CharField(max_length=50)
    confidence_score = models.FloatField()
    cluster_group = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student.roll_no} - {self.predicted_performance}"
'''

# Save models.py
with open('models.py', 'w') as f:
    f.write(models_py)

print("Django models.py created successfully!")

# 2. Django Views (views.py)
views_py = '''from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from .models import Student, AcademicRecord, StudentBehavior, Prediction
import json

def home(request):
    """Home page with dashboard overview"""
    context = {
        'total_students': Student.objects.count(),
        'total_predictions': Prediction.objects.count(),
    }
    return render(request, 'analytics/home.html', context)

@login_required
def upload_data(request):
    """Upload student data from CSV/Excel"""
    if request.method == 'POST' and request.FILES.get('dataset'):
        file = request.FILES['dataset']
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith('.xlsx'):
            df = pd.read_excel(file)
        else:
            return render(request, 'analytics/upload.html', {'error': 'Invalid file format'})
        
        # Process and save data to database
        process_uploaded_data(df)
        return redirect('dashboard')
    
    return render(request, 'analytics/upload.html')

def process_uploaded_data(df):
    """Process uploaded data and save to database"""
    # Clean and process data similar to our preprocessing
    for index, row in df.iterrows():
        # Create or update student record
        student, created = Student.objects.get_or_create(
            roll_no=f"STU{index+1:04d}",
            defaults={
                'name': f"Student {index+1}",
                'gender': row.get('gender', 'Male'),
                'age': int(row.get('age', 20)),
                'admission_year': int(row.get('admission_year', 2021)),
                'current_semester': int(row.get('current_semester', 1))
            }
        )

@login_required
def dashboard(request):
    """Main analytics dashboard"""
    # Get summary statistics
    students = Student.objects.all()
    predictions = Prediction.objects.all()
    
    context = {
        'students': students,
        'predictions': predictions,
        'performance_distribution': get_performance_distribution(),
        'cluster_analysis': get_cluster_analysis(),
    }
    return render(request, 'analytics/dashboard.html', context)

def get_performance_distribution():
    """Get performance category distribution"""
    records = AcademicRecord.objects.all()
    distribution = {}
    for record in records:
        cat = record.performance_category
        distribution[cat] = distribution.get(cat, 0) + 1
    return distribution

def get_cluster_analysis():
    """Perform cluster analysis"""
    # Implement clustering logic
    return {'cluster_1': 25, 'cluster_2': 30, 'cluster_3': 45}

@csrf_exempt
def predict_performance(request):
    """API endpoint for performance prediction"""
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # Implement prediction logic using trained model
        prediction_result = {
            'predicted_category': 'First Class',
            'confidence': 0.85,
            'cluster': 2
        }
        
        return JsonResponse(prediction_result)
    
    return JsonResponse({'error': 'Invalid request method'})

def association_rules(request):
    """Display association rules analysis"""
    # Implement Apriori algorithm results
    rules = [
        {'antecedent': 'High Attendance', 'consequent': 'Good Performance', 'support': 0.6, 'confidence': 0.8},
        {'antecedent': 'Regular Study', 'consequent': 'High CGPA', 'support': 0.5, 'confidence': 0.75},
    ]
    
    context = {'rules': rules}
    return render(request, 'analytics/association_rules.html', context)

def clustering_results(request):
    """Display clustering analysis results"""
    context = {
        'clusters': [
            {'id': 1, 'name': 'High Performers', 'count': 150, 'avg_cgpa': 3.8},
            {'id': 2, 'name': 'Average Performers', 'count': 200, 'avg_cgpa': 3.2},
            {'id': 3, 'name': 'Low Performers', 'count': 100, 'avg_cgpa': 2.8},
        ]
    }
    return render(request, 'analytics/clustering.html', context)
'''

with open('views.py', 'w') as f:
    f.write(views_py)

print("Django views.py created successfully!")