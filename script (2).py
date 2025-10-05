# Let's work with available libraries and create a complete project structure
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import warnings
warnings.filterwarnings('ignore')

# Read the dataset
df = pd.read_excel('Students_Performance_data_set.xlsx')

# Display basic info about the dataset
print("Dataset Shape:", df.shape)
print("\nColumn Names:")
cols = df.columns.tolist()
for i, col in enumerate(cols, 1):
    print(f"{i}. {col}")

# Check for missing values
print(f"\nMissing Values:\n{df.isnull().sum()}")

# Basic statistics
print(f"\nData Types:\n{df.dtypes}")

# Display first 5 rows
print(f"\nFirst 5 rows:")
df.head()