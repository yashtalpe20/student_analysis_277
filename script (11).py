# Fix the data preprocessing issue and test again
import pandas as pd
import numpy as np

# Load the dataset and fix data issues
df = pd.read_csv('cleaned_student_data.csv')

print("Dataset shape:", df.shape)
print("\nChecking for problematic values...")

# Check attendance column for non-numeric values
print("Attendance unique values:")
print(df['attendance'].unique()[:20])

# Fix attendance column - convert ranges to averages
def clean_attendance(value):
    if isinstance(value, str):
        if '-' in str(value):
            # Handle ranges like '94-98'
            parts = str(value).split('-')
            if len(parts) == 2:
                try:
                    return (float(parts[0]) + float(parts[1])) / 2
                except:
                    return 85  # default value
    try:
        return float(value)
    except:
        return 85  # default value

df['attendance'] = df['attendance'].apply(clean_attendance)

# Ensure all numeric columns are properly converted
numeric_columns = ['age', 'current_semester', 'study_hours', 'study_sessions',
                  'social_media_hours', 'attendance', 'skill_development_hours',
                  'credits_completed', 'family_income', 'current_cgpa']

for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Fill missing values with median
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())

# Save cleaned data
df.to_csv('cleaned_student_data_fixed.csv', index=False)

print("Data cleaning completed!")
print(f"Fixed dataset shape: {df.shape}")
print(f"Missing values: {df.isnull().sum().sum()}")

# Display sample of cleaned data
print("\nSample of cleaned data:")
print(df[['attendance', 'current_cgpa', 'Performance_Category']].head())