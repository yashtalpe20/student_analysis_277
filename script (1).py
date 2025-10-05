# Install required packages first
import subprocess
import sys

# Install mlxtend
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'mlxtend'])

# Import libraries again
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from mlxtend.frequent_patterns import apriori, association_rules
import warnings
warnings.filterwarnings('ignore')

print("All packages installed successfully!")