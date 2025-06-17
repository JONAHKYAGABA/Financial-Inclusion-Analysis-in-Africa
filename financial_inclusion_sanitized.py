# Financial Inclusion Analysis Script (Sanitized Full Version)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Suppress warnings for cleaner output
import warnings
warnings.filterwarnings('ignore')

# Load dataset (no credentials required)
file_path = 'Train.csv'  # Ensure this file is present in your working directory
if not os.path.exists(file_path):
    raise FileNotFoundError("Train.csv not found. Please ensure it's in the same folder as this script.")

# Read dataset
train = pd.read_csv(file_path)

# --- Basic Exploration ---
print("First 5 rows:")
print(train.head())

print("\nSummary Statistics:")
print(train.describe(include='all'))

print("\nData Types:")
print(train.dtypes)

print("\nNull Value Counts:")
print(train.isnull().sum())

# --- Visual Analysis ---

# 1. Bank Account Ownership Distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=train, x='bank_account', palette='Set2')
plt.title('Bank Account Ownership')
plt.tight_layout()
plt.show()

# 2. Gender vs Bank Account Ownership
plt.figure(figsize=(6, 4))
sns.countplot(data=train, x='gender_of_respondent', hue='bank_account', palette='Set1')
plt.title('Gender vs Bank Account Ownership')
plt.tight_layout()
plt.show()

# 3. Age Distribution
plt.figure(figsize=(8, 4))
sns.histplot(data=train, x='age_of_respondent', hue='bank_account', bins=30, kde=True, palette='husl')
plt.title('Age Distribution by Bank Account Ownership')
plt.tight_layout()
plt.show()

# 4. Education Level vs Bank Account Ownership
plt.figure(figsize=(10, 5))
sns.countplot(data=train, y='education_level', hue='bank_account', palette='coolwarm')
plt.title('Education Level vs Bank Account Ownership')
plt.tight_layout()
plt.show()

# 5. Marital Status vs Bank Account Ownership
plt.figure(figsize=(8, 4))
sns.countplot(data=train, x='marital_status', hue='bank_account', palette='Set3')
plt.title('Marital Status vs Bank Account Ownership')
plt.tight_layout()
plt.show()

# 6. Household Size Distribution
plt.figure(figsize=(8, 4))
sns.histplot(data=train, x='household_size', bins=20, hue='bank_account', kde=False, palette='viridis')
plt.title('Household Size Distribution by Bank Account Ownership')
plt.tight_layout()
plt.show()

# 7. Job Type vs Bank Account Ownership
plt.figure(figsize=(12, 6))
sns.countplot(data=train, y='job_type', hue='bank_account', palette='magma')
plt.title('Job Type vs Bank Account Ownership')
plt.tight_layout()
plt.show()

# 8. Region vs Bank Account Ownership
plt.figure(figsize=(12, 6))
sns.countplot(data=train, y='region', hue='bank_account', palette='plasma')
plt.title('Region vs Bank Account Ownership')
plt.tight_layout()
plt.show()

print("\n✅ Financial inclusion analysis completed successfully.")
