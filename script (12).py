# Now run the complete ML analysis with fixed data
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import warnings
warnings.filterwarnings('ignore')

# Load the fixed dataset
df = pd.read_csv('cleaned_student_data_fixed.csv')

print("="*50)
print("STUDENT PERFORMANCE ANALYTICS RESULTS")
print("="*50)

# 1. CLASSIFICATION ANALYSIS
print("\n1. CLASSIFICATION ANALYSIS (Decision Tree)")
print("-" * 40)

# Select features for classification
feature_columns = ['age', 'current_semester', 'study_hours', 'study_sessions',
                  'social_media_hours', 'attendance', 'skill_development_hours',
                  'credits_completed', 'family_income']

# Ensure we have the required columns and clean data
available_features = [col for col in feature_columns if col in df.columns]
X = df[available_features].fillna(df[available_features].median())
y = df['Performance_Category']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Decision Tree
dt_classifier = DecisionTreeClassifier(random_state=42, max_depth=10)
dt_classifier.fit(X_train, y_train)

# Make predictions
y_pred = dt_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Classification Accuracy: {accuracy:.3f}")
print(f"Number of features used: {len(available_features)}")
print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

# Feature importance
feature_importance = pd.DataFrame({
    'feature': available_features,
    'importance': dt_classifier.feature_importances_
}).sort_values('importance', ascending=False)

print(f"\nTop 5 Most Important Features:")
for i, row in feature_importance.head().iterrows():
    print(f"  {row['feature']}: {row['importance']:.3f}")

# 2. CLUSTERING ANALYSIS
print(f"\n2. CLUSTERING ANALYSIS (K-Means)")
print("-" * 40)

# Select numerical features for clustering
cluster_features = ['current_cgpa', 'attendance', 'study_hours', 'credits_completed']
available_cluster_features = [col for col in cluster_features if col in df.columns]
X_cluster = df[available_cluster_features].fillna(df[available_cluster_features].median())

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_cluster)

# Perform K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
cluster_labels = kmeans.fit_predict(X_scaled)

# Add cluster labels to dataframe
df['Cluster'] = cluster_labels

# Analyze clusters
cluster_analysis = df.groupby('Cluster')[available_cluster_features].mean()
cluster_counts = df['Cluster'].value_counts().sort_index()

print(f"Cluster Analysis:")
for cluster_id in range(3):
    count = cluster_counts[cluster_id]
    avg_cgpa = cluster_analysis.loc[cluster_id, 'current_cgpa']
    avg_attendance = cluster_analysis.loc[cluster_id, 'attendance']
    print(f"  Cluster {cluster_id}: {count} students (Avg CGPA: {avg_cgpa:.2f}, Avg Attendance: {avg_attendance:.1f}%)")

# 3. ASSOCIATION RULES ANALYSIS
print(f"\n3. ASSOCIATION RULES ANALYSIS")
print("-" * 40)

# Create binary features for association rule mining
high_attendance = df['attendance'] >= 85
good_performance = df['Performance_Category'].isin(['Distinction', 'First Class'])
high_study = df['study_hours'] >= 4
high_cgpa = df['current_cgpa'] >= 3.5

# Calculate association rules
rules = []

# Rule 1: High attendance -> Good performance
support_ha = high_attendance.sum() / len(df)
support_gp = good_performance.sum() / len(df)
support_both_1 = (high_attendance & good_performance).sum() / len(df)
confidence_ha_gp = support_both_1 / support_ha if support_ha > 0 else 0

rules.append({
    'rule': 'High Attendance (>=85%) → Good Performance',
    'support': support_both_1,
    'confidence': confidence_ha_gp,
    'lift': confidence_ha_gp / support_gp if support_gp > 0 else 0
})

# Rule 2: High study hours -> High CGPA
support_hs = high_study.sum() / len(df)
support_hc = high_cgpa.sum() / len(df)
support_both_2 = (high_study & high_cgpa).sum() / len(df)
confidence_hs_hc = support_both_2 / support_hs if support_hs > 0 else 0

rules.append({
    'rule': 'High Study Hours (>=4) → High CGPA (>=3.5)',
    'support': support_both_2,
    'confidence': confidence_hs_hc,
    'lift': confidence_hs_hc / support_hc if support_hc > 0 else 0
})

print("Discovered Association Rules:")
for rule in rules:
    print(f"  {rule['rule']}")
    print(f"    Support: {rule['support']:.3f}, Confidence: {rule['confidence']:.3f}, Lift: {rule['lift']:.3f}")

# 4. PERFORMANCE DISTRIBUTION
print(f"\n4. PERFORMANCE DISTRIBUTION")
print("-" * 40)

performance_dist = df['Performance_Category'].value_counts()
print("Performance Category Distribution:")
for category, count in performance_dist.items():
    percentage = (count / len(df)) * 100
    print(f"  {category}: {count} students ({percentage:.1f}%)")

print(f"\nDataset Summary:")
print(f"Total Students: {len(df)}")
print(f"Average CGPA: {df['current_cgpa'].mean():.2f}")
print(f"Average Attendance: {df['attendance'].mean():.1f}%")
print(f"Classification Model Accuracy: {accuracy:.1%}")

print("\n" + "="*50)
print("ANALYSIS COMPLETED SUCCESSFULLY!")
print("="*50)