# Data preprocessing and feature engineering
# Create a performance category based on CGPA
def categorize_performance(cgpa):
    if cgpa >= 3.5:
        return 'Distinction'
    elif cgpa >= 3.0:
        return 'First Class'
    elif cgpa >= 2.5:
        return 'Second Class'
    else:
        return 'Pass'

# Convert CGPA to float and handle missing values
df['What is your current CGPA?'] = pd.to_numeric(df['What is your current CGPA?'], errors='coerce')
df['Performance_Category'] = df['What is your current CGPA?'].apply(categorize_performance)

# Clean and prepare data
# Rename columns for easier handling
column_mapping = {
    'University Admission year': 'admission_year',
    'Gender': 'gender',
    'Age': 'age',
    'Current Semester': 'current_semester',
    'Do you have meritorious scholarship ?': 'scholarship',
    'Do you use University transportation?': 'transportation',
    'How many hour do you study daily?': 'study_hours',
    'How many times do you seat for study in a day?': 'study_sessions',
    'What is your preferable learning mode?': 'learning_mode',
    'Do you use smart phone?': 'smartphone',
    'Do you have personal Computer?': 'personal_computer',
    'How many hour do you spent daily in social media?': 'social_media_hours',
    'Status of your English language proficiency': 'english_proficiency',
    'Average attendance on class': 'attendance',
    'Did you ever fall in probation?': 'probation',
    'Did you ever got suspension?': 'suspension',
    'Do you attend in teacher consultancy for any kind of academical problems?': 'teacher_consultancy',
    'What are the skills do you have ?': 'skills',
    'How many hour do you spent daily on your skill development?': 'skill_development_hours',
    'What is you interested area?': 'interest_area',
    'What is your relationship status?': 'relationship_status',
    'Are you engaged with any co-curriculum activities?': 'co_curricular',
    'With whom you are living with?': 'living_arrangement',
    'Do you have any health issues?': 'health_issues',
    'What was your previous SGPA?': 'previous_sgpa',
    'Do you have any physical disabilities?': 'physical_disabilities',
    'What is your current CGPA?': 'current_cgpa',
    'How many Credit did you have completed?': 'credits_completed',
    'What is your monthly family income?': 'family_income'
}

df_clean = df.rename(columns=column_mapping)

# Display cleaned data info
print("Cleaned Dataset Info:")
print(f"Shape: {df_clean.shape}")
print(f"\nPerformance Categories:")
print(df_clean['Performance_Category'].value_counts())

# Check attendance distribution
print(f"\nAttendance Statistics:")
print(df_clean['attendance'].describe())

# Save cleaned data
df_clean.to_csv('cleaned_student_data.csv', index=False)
print("\nCleaned data saved as 'cleaned_student_data.csv'")