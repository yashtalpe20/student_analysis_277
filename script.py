# Let's analyze the dataset structure and create a complete Student Performance Prediction system
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from mlxtend.frequent_patterns import apriori, association_rules
import warnings
warnings.filterwarnings('ignore')

# Read the dataset
df = pd.read_excel('Students_Performance_data_set.xlsx')

# Display dataset info
print("Dataset Shape:", df.shape)
print("\nColumn Names:")
for i, col in enumerate(df.columns, 1):
    print(f"{i}. {col}")

print("\nFirst few rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())