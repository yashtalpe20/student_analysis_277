# 8. Additional Templates and Documentation

# Upload template
upload_html = '''{% extends 'base.html' %}

{% block title %}Upload Data - Student Analytics{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-8 mx-auto">
        <div class="card">
            <div class="card-header">
                <h5><i class="fas fa-upload"></i> Upload Student Dataset</h5>
            </div>
            <div class="card-body">
                {% if error %}
                    <div class="alert alert-danger">{{ error }}</div>
                {% endif %}
                
                <form method="post" enctype="multipart/form-data">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="dataset" class="form-label">Select Dataset File</label>
                        <input type="file" class="form-control" id="dataset" name="dataset" accept=".csv,.xlsx" required>
                        <div class="form-text">Supported formats: CSV, Excel (.xlsx)</div>
                    </div>
                    
                    <div class="alert alert-info">
                        <h6>Expected Columns:</h6>
                        <ul class="mb-0">
                            <li>Student information (Gender, Age, Semester)</li>
                            <li>Academic data (CGPA, Attendance, Credits)</li>
                            <li>Behavioral data (Study hours, Social media usage)</li>
                            <li>Personal data (Family income, Living arrangement)</li>
                        </ul>
                    </div>
                    
                    <button type="submit" class="btn btn-primary">
                        <i class="fas fa-upload"></i> Upload & Process
                    </button>
                </form>
            </div>
        </div>
    </div>
</div>

<div class="row mt-4">
    <div class="col-md-12">
        <div class="card">
            <div class="card-header">
                <h5>Data Processing Pipeline</h5>
            </div>
            <div class="card-body">
                <div class="row">
                    <div class="col-md-3 text-center">
                        <i class="fas fa-file-import fa-3x text-primary mb-2"></i>
                        <h6>1. Data Import</h6>
                        <p class="small">Load CSV/Excel files</p>
                    </div>
                    <div class="col-md-3 text-center">
                        <i class="fas fa-broom fa-3x text-success mb-2"></i>
                        <h6>2. Data Cleaning</h6>
                        <p class="small">Handle missing values</p>
                    </div>
                    <div class="col-md-3 text-center">
                        <i class="fas fa-cogs fa-3x text-warning mb-2"></i>
                        <h6>3. Feature Engineering</h6>
                        <p class="small">Transform variables</p>
                    </div>
                    <div class="col-md-3 text-center">
                        <i class="fas fa-database fa-3x text-info mb-2"></i>
                        <h6>4. Store in DW</h6>
                        <p class="small">Save to database</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
'''

# Association Rules template
association_html = '''{% extends 'base.html' %}

{% block title %}Association Rules - Student Analytics{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-12">
        <h2><i class="fas fa-project-diagram"></i> Association Rule Mining</h2>
        <p class="text-muted">Discover interesting relationships in student performance data using Apriori algorithm</p>
    </div>
</div>

<div class="row">
    <div class="col-md-12">
        <div class="card">
            <div class="card-header">
                <h5>Discovered Association Rules</h5>
            </div>
            <div class="card-body">
                <div class="table-responsive">
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>Antecedent (If)</th>
                                <th>Consequent (Then)</th>
                                <th>Support</th>
                                <th>Confidence</th>
                                <th>Lift</th>
                                <th>Interpretation</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for rule in rules %}
                            <tr>
                                <td><span class="badge bg-primary">{{ rule.antecedent }}</span></td>
                                <td><span class="badge bg-success">{{ rule.consequent }}</span></td>
                                <td>{{ rule.support }}</td>
                                <td>{{ rule.confidence }}</td>
                                <td>
                                    {% if rule.lift > 1 %}
                                        <span class="badge bg-success">{{ rule.lift }}</span>
                                    {% else %}
                                        <span class="badge bg-warning">{{ rule.lift }}</span>
                                    {% endif %}
                                </td>
                                <td class="small">
                                    {% if rule.confidence > 0.7 %}
                                        <span class="text-success">Strong relationship</span>
                                    {% elif rule.confidence > 0.5 %}
                                        <span class="text-warning">Moderate relationship</span>
                                    {% else %}
                                        <span class="text-danger">Weak relationship</span>
                                    {% endif %}
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="row mt-4">
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h6>Key Insights</h6>
            </div>
            <div class="card-body">
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">
                        <i class="fas fa-chart-line text-success"></i>
                        Students with >80% attendance tend to achieve better grades
                    </li>
                    <li class="list-group-item">
                        <i class="fas fa-book text-primary"></i>
                        Regular study habits correlate with higher CGPA
                    </li>
                    <li class="list-group-item">
                        <i class="fas fa-users text-info"></i>
                        Co-curricular participation improves overall performance
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <div class="col-md-6">
        <div class="card">
            <div class="card-header">
                <h6>Metrics Explanation</h6>
            </div>
            <div class="card-body">
                <dl class="row">
                    <dt class="col-sm-3">Support</dt>
                    <dd class="col-sm-9">Frequency of pattern in dataset</dd>
                    
                    <dt class="col-sm-3">Confidence</dt>
                    <dd class="col-sm-9">Probability of consequent given antecedent</dd>
                    
                    <dt class="col-sm-3">Lift</dt>
                    <dd class="col-sm-9">Measure of rule strength (>1 means positive correlation)</dd>
                </dl>
            </div>
        </div>
    </div>
</div>
{% endblock %}
'''

# Clustering template
clustering_html = '''{% extends 'base.html' %}

{% block title %}Clustering Analysis - Student Analytics{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-12">
        <h2><i class="fas fa-project-diagram"></i> K-Means Clustering Analysis</h2>
        <p class="text-muted">Student grouping based on performance patterns and characteristics</p>
    </div>
</div>

<div class="row">
    {% for cluster in clusters %}
    <div class="col-md-4">
        <div class="card">
            <div class="card-header bg-primary text-white">
                <h5><i class="fas fa-users"></i> {{ cluster.name }}</h5>
            </div>
            <div class="card-body">
                <h2 class="text-primary">{{ cluster.count }} <small class="text-muted">students</small></h2>
                <p><strong>Average CGPA:</strong> {{ cluster.avg_cgpa }}</p>
                
                <div class="progress mb-2">
                    <div class="progress-bar" role="progressbar" style="width: {{ cluster.avg_cgpa|mul:25 }}%">
                        {{ cluster.avg_cgpa }}
                    </div>
                </div>
                
                <ul class="list-unstyled">
                    {% if cluster.id == 1 %}
                        <li><i class="fas fa-check text-success"></i> High attendance (>90%)</li>
                        <li><i class="fas fa-check text-success"></i> Regular study habits</li>
                        <li><i class="fas fa-check text-success"></i> Active in co-curricular</li>
                    {% elif cluster.id == 2 %}
                        <li><i class="fas fa-check text-warning"></i> Moderate attendance (70-90%)</li>
                        <li><i class="fas fa-check text-warning"></i> Average study time</li>
                        <li><i class="fas fa-check text-warning"></i> Some co-curricular involvement</li>
                    {% else %}
                        <li><i class="fas fa-times text-danger"></i> Low attendance (<70%)</li>
                        <li><i class="fas fa-times text-danger"></i> Irregular study patterns</li>
                        <li><i class="fas fa-times text-danger"></i> Limited involvement</li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </div>
    {% endfor %}
</div>

<div class="row mt-4">
    <div class="col-md-8">
        <div class="card">
            <div class="card-header">
                <h5>Cluster Visualization</h5>
            </div>
            <div class="card-body">
                <canvas id="clusterScatter"></canvas>
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="card">
            <div class="card-header">
                <h5>Cluster Recommendations</h5>
            </div>
            <div class="card-body">
                <div class="alert alert-success">
                    <h6>High Performers</h6>
                    <p class="small">Continue mentoring programs</p>
                </div>
                <div class="alert alert-warning">
                    <h6>Average Performers</h6>
                    <p class="small">Implement targeted interventions</p>
                </div>
                <div class="alert alert-danger">
                    <h6>Low Performers</h6>
                    <p class="small">Require immediate attention</p>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
// Cluster scatter plot
const ctx = document.getElementById('clusterScatter').getContext('2d');
new Chart(ctx, {
    type: 'scatter',
    data: {
        datasets: [{
            label: 'High Performers',
            data: [{x: 3.8, y: 95}, {x: 3.7, y: 92}, {x: 3.9, y: 98}],
            backgroundColor: 'rgba(40, 167, 69, 0.6)'
        }, {
            label: 'Average Performers', 
            data: [{x: 3.2, y: 80}, {x: 3.1, y: 82}, {x: 3.3, y: 78}],
            backgroundColor: 'rgba(255, 193, 7, 0.6)'
        }, {
            label: 'Low Performers',
            data: [{x: 2.8, y: 65}, {x: 2.7, y: 60}, {x: 2.9, y: 68}],
            backgroundColor: 'rgba(220, 53, 69, 0.6)'
        }]
    },
    options: {
        responsive: true,
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'CGPA'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Attendance %'
                }
            }
        }
    }
});
</script>
{% endblock %}
'''

# Save additional templates
with open('upload.html', 'w') as f:
    f.write(upload_html)

with open('association_rules.html', 'w') as f:
    f.write(association_html)

with open('clustering.html', 'w') as f:
    f.write(clustering_html)

print("Additional templates created successfully!")