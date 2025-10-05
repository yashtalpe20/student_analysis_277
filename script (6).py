# 6. HTML Templates

# Base template
base_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Student Performance Analytics{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{% url 'analytics:home' %}">
                <i class="fas fa-graduation-cap"></i> Student Analytics
            </a>
            <div class="navbar-nav ms-auto">
                <a class="nav-link" href="{% url 'analytics:home' %}">Home</a>
                <a class="nav-link" href="{% url 'analytics:dashboard' %}">Dashboard</a>
                <a class="nav-link" href="{% url 'analytics:upload_data' %}">Upload Data</a>
                <a class="nav-link" href="{% url 'analytics:association_rules' %}">Association Rules</a>
                <a class="nav-link" href="{% url 'analytics:clustering_results' %}">Clustering</a>
            </div>
        </div>
    </nav>

    <main class="container mt-4">
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            {% endfor %}
        {% endif %}

        {% block content %}
        {% endblock %}
    </main>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''

# Home page template
home_html = '''{% extends 'base.html' %}

{% block title %}Home - Student Performance Analytics{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-12">
        <div class="jumbotron bg-primary text-white p-5 rounded">
            <h1 class="display-4">Student Performance Prediction & Analytics System</h1>
            <p class="lead">Advanced Data Mining and Warehouse concepts applied to educational analytics</p>
            <hr class="my-4">
            <p>Upload student data, analyze performance patterns, and predict outcomes using machine learning.</p>
            <a class="btn btn-light btn-lg" href="{% url 'analytics:dashboard' %}" role="button">
                <i class="fas fa-chart-bar"></i> View Dashboard
            </a>
        </div>
    </div>
</div>

<div class="row mt-4">
    <div class="col-md-3">
        <div class="card text-center">
            <div class="card-body">
                <i class="fas fa-users fa-3x text-primary mb-3"></i>
                <h5 class="card-title">Total Students</h5>
                <h2 class="text-primary">{{ total_students }}</h2>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card text-center">
            <div class="card-body">
                <i class="fas fa-brain fa-3x text-success mb-3"></i>
                <h5 class="card-title">Predictions Made</h5>
                <h2 class="text-success">{{ total_predictions }}</h2>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card text-center">
            <div class="card-body">
                <i class="fas fa-chart-line fa-3x text-warning mb-3"></i>
                <h5 class="card-title">Classification</h5>
                <p>Decision Tree Algorithm</p>
            </div>
        </div>
    </div>
    <div class="col-md-3">
        <div class="card text-center">
            <div class="card-body">
                <i class="fas fa-project-diagram fa-3x text-info mb-3"></i>
                <h5 class="card-title">Clustering</h5>
                <p>K-means Algorithm</p>
            </div>
        </div>
    </div>
</div>

<div class="row mt-4">
    <div class="col-md-12">
        <h3>DMW Concepts Implemented</h3>
        <div class="row">
            <div class="col-md-6">
                <ul class="list-group">
                    <li class="list-group-item"><i class="fas fa-check text-success"></i> Data Preprocessing</li>
                    <li class="list-group-item"><i class="fas fa-check text-success"></i> Classification (Decision Tree)</li>
                    <li class="list-group-item"><i class="fas fa-check text-success"></i> Clustering (K-means)</li>
                    <li class="list-group-item"><i class="fas fa-check text-success"></i> Association Rule Mining</li>
                </ul>
            </div>
            <div class="col-md-6">
                <ul class="list-group">
                    <li class="list-group-item"><i class="fas fa-check text-success"></i> Data Warehouse Design</li>
                    <li class="list-group-item"><i class="fas fa-check text-success"></i> OLAP Operations</li>
                    <li class="list-group-item"><i class="fas fa-check text-success"></i> Distance Measures</li>
                    <li class="list-group-item"><i class="fas fa-check text-success"></i> Data Visualization</li>
                </ul>
            </div>
        </div>
    </div>
</div>
{% endblock %}
'''

# Dashboard template
dashboard_html = '''{% extends 'base.html' %}

{% block title %}Dashboard - Student Analytics{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-12">
        <h2><i class="fas fa-chart-bar"></i> Analytics Dashboard</h2>
        <p class="text-muted">Comprehensive analysis of student performance data</p>
    </div>
</div>

<div class="row">
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h5><i class="fas fa-chart-pie"></i> Performance Distribution</h5>
            </div>
            <div class="card-body">
                <canvas id="performanceChart"></canvas>
            </div>
        </div>
    </div>
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h5><i class="fas fa-project-diagram"></i> Cluster Analysis</h5>
            </div>
            <div class="card-body">
                <canvas id="clusterChart"></canvas>
            </div>
        </div>
    </div>
</div>

<div class="row mt-4">
    <div class="col-md-12">
        <div class="card">
            <div class="card-header">
                <h5><i class="fas fa-users"></i> Student Performance Prediction</h5>
            </div>
            <div class="card-body">
                <form id="predictionForm">
                    <div class="row">
                        <div class="col-md-3">
                            <label for="attendance">Attendance (%)</label>
                            <input type="number" class="form-control" id="attendance" min="0" max="100">
                        </div>
                        <div class="col-md-3">
                            <label for="studyHours">Study Hours</label>
                            <input type="number" class="form-control" id="studyHours" min="1" max="24">
                        </div>
                        <div class="col-md-3">
                            <label for="previousSGPA">Previous SGPA</label>
                            <input type="number" step="0.01" class="form-control" id="previousSGPA" min="0" max="4">
                        </div>
                        <div class="col-md-3">
                            <button type="submit" class="btn btn-primary mt-4">
                                <i class="fas fa-brain"></i> Predict Performance
                            </button>
                        </div>
                    </div>
                </form>
                <div id="predictionResult" class="mt-3"></div>
            </div>
        </div>
    </div>
</div>

<script>
// Performance Distribution Chart
const performanceCtx = document.getElementById('performanceChart').getContext('2d');
new Chart(performanceCtx, {
    type: 'doughnut',
    data: {
        labels: ['Distinction', 'First Class', 'Second Class', 'Pass'],
        datasets: [{
            data: [438, 406, 259, 91],
            backgroundColor: ['#28a745', '#17a2b8', '#ffc107', '#dc3545']
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});

// Cluster Analysis Chart
const clusterCtx = document.getElementById('clusterChart').getContext('2d');
new Chart(clusterCtx, {
    type: 'bar',
    data: {
        labels: ['High Performers', 'Average Performers', 'Low Performers'],
        datasets: [{
            label: 'Number of Students',
            data: [150, 200, 100],
            backgroundColor: ['#28a745', '#ffc107', '#dc3545']
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});

// Prediction Form Handler
document.getElementById('predictionForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = {
        attendance: document.getElementById('attendance').value,
        studyHours: document.getElementById('studyHours').value,
        previousSGPA: document.getElementById('previousSGPA').value
    };
    
    try {
        const response = await fetch('/api/predict/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(formData)
        });
        
        const result = await response.json();
        
        document.getElementById('predictionResult').innerHTML = `
            <div class="alert alert-success">
                <h6>Prediction Results:</h6>
                <p><strong>Predicted Performance:</strong> ${result.predicted_category}</p>
                <p><strong>Confidence:</strong> ${(result.confidence * 100).toFixed(1)}%</p>
                <p><strong>Cluster Group:</strong> ${result.cluster}</p>
            </div>
        `;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('predictionResult').innerHTML = 
            '<div class="alert alert-danger">Error making prediction. Please try again.</div>';
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
</script>
{% endblock %}
'''

# Save HTML templates
with open('base.html', 'w') as f:
    f.write(base_html)

with open('home.html', 'w') as f:
    f.write(home_html)

with open('dashboard.html', 'w') as f:
    f.write(dashboard_html)

print("HTML templates created successfully!")