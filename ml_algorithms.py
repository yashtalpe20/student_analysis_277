import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle
import warnings
warnings.filterwarnings('ignore')

class StudentPerformanceAnalyzer:
    def __init__(self):
        self.dt_classifier = None
        self.kmeans_model = None
        self.label_encoders = {}
        self.scaler = StandardScaler()

    def load_and_preprocess_data(self, file_path):
        """Load and preprocess the student dataset"""
        df = pd.read_csv(file_path)

        # Handle missing values
        df = df.fillna(df.mode().iloc[0])

        # Encode categorical variables
        categorical_columns = ['gender', 'scholarship', 'transportation', 'learning_mode', 
                             'smartphone', 'personal_computer', 'english_proficiency',
                             'probation', 'suspension', 'teacher_consultancy', 'skills',
                             'interest_area', 'relationship_status', 'co_curricular',
                             'living_arrangement', 'health_issues', 'physical_disabilities']

        for col in categorical_columns:
            if col in df.columns:
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col].astype(str))
                self.label_encoders[col] = le

        return df

    def train_classification_model(self, df):
        """Train Decision Tree for performance classification"""
        # Select features for classification
        feature_columns = ['age', 'current_semester', 'study_hours', 'study_sessions',
                          'social_media_hours', 'attendance', 'skill_development_hours',
                          'credits_completed', 'family_income']

        X = df[feature_columns]
        y = df['Performance_Category']

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train Decision Tree
        self.dt_classifier = DecisionTreeClassifier(random_state=42, max_depth=10)
        self.dt_classifier.fit(X_train, y_train)

        # Predictions and evaluation
        y_pred = self.dt_classifier.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        print(f"Classification Accuracy: {accuracy:.2f}")
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))

        return accuracy

    def perform_clustering(self, df):
        """Perform K-means clustering"""
        # Select numerical features for clustering
        cluster_features = ['current_cgpa', 'attendance', 'study_hours', 'credits_completed']
        X_cluster = df[cluster_features].fillna(df[cluster_features].mean())

        # Scale features
        X_scaled = self.scaler.fit_transform(X_cluster)

        # Perform K-means clustering
        self.kmeans_model = KMeans(n_clusters=3, random_state=42)
        cluster_labels = self.kmeans_model.fit_predict(X_scaled)

        # Add cluster labels to dataframe
        df['Cluster'] = cluster_labels

        # Analyze clusters
        cluster_analysis = df.groupby('Cluster')[cluster_features].mean()
        print("\nCluster Analysis:")
        print(cluster_analysis)

        return cluster_labels

    def generate_association_rules(self, df):
        """Generate association rules (simplified implementation)"""
        # Create binary features for association rule mining
        rules = []

        # Rule 1: High attendance -> Good performance
        high_attendance = df['attendance'] >= 85
        good_performance = df['Performance_Category'].isin(['Distinction', 'First Class'])

        support_ha = high_attendance.sum() / len(df)
        support_gp = good_performance.sum() / len(df)
        support_both = (high_attendance & good_performance).sum() / len(df)

        if support_ha > 0:
            confidence_ha_gp = support_both / support_ha
            rules.append({
                'antecedent': 'High Attendance (>=85%)',
                'consequent': 'Good Performance',
                'support': round(support_both, 3),
                'confidence': round(confidence_ha_gp, 3),
                'lift': round(confidence_ha_gp / support_gp, 3)
            })

        # Rule 2: High study hours -> High CGPA
        high_study = df['study_hours'] >= 4
        high_cgpa = df['current_cgpa'] >= 3.5

        support_hs = high_study.sum() / len(df)
        support_hc = high_cgpa.sum() / len(df)
        support_both_2 = (high_study & high_cgpa).sum() / len(df)

        if support_hs > 0:
            confidence_hs_hc = support_both_2 / support_hs
            rules.append({
                'antecedent': 'High Study Hours (>=4)',
                'consequent': 'High CGPA (>=3.5)',
                'support': round(support_both_2, 3),
                'confidence': round(confidence_hs_hc, 3),
                'lift': round(confidence_hs_hc / support_hc, 3) if support_hc > 0 else 0
            })

        print("\nAssociation Rules:")
        for rule in rules:
            print(f"Rule: {rule['antecedent']} -> {rule['consequent']}")
            print(f"Support: {rule['support']}, Confidence: {rule['confidence']}, Lift: {rule['lift']}")
            print()

        return rules

    def save_models(self):
        """Save trained models"""
        if self.dt_classifier:
            with open('decision_tree_model.pkl', 'wb') as f:
                pickle.dump(self.dt_classifier, f)

        if self.kmeans_model:
            with open('kmeans_model.pkl', 'wb') as f:
                pickle.dump(self.kmeans_model, f)

        with open('scaler.pkl', 'wb') as f:
            pickle.dump(self.scaler, f)

        with open('label_encoders.pkl', 'wb') as f:
            pickle.dump(self.label_encoders, f)

        print("Models saved successfully!")

    def predict_performance(self, student_data):
        """Predict performance for new student data"""
        if self.dt_classifier:
            prediction = self.dt_classifier.predict([student_data])
            probability = self.dt_classifier.predict_proba([student_data])
            return prediction[0], max(probability[0])
        return None, None

# Usage example
if __name__ == "__main__":
    analyzer = StudentPerformanceAnalyzer()

    # Load and preprocess data
    df = analyzer.load_and_preprocess_data('cleaned_student_data.csv')

    # Train classification model
    accuracy = analyzer.train_classification_model(df)

    # Perform clustering
    clusters = analyzer.perform_clustering(df)

    # Generate association rules
    rules = analyzer.generate_association_rules(df)

    # Save models
    analyzer.save_models()
