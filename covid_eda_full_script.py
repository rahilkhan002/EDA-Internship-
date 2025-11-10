"""
EDA on synthetic_cleaned_covid_data.csv
Visualizes trends, distributions, and relationships in COVID-19 data.
Displays all plots using plt.show() — nothing is saved to disk.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# -------------------------------------
# Load dataset
# -------------------------------------
DATA_PATH = Path("synthetic_cleaned_covid_data.csv")
df = pd.read_csv(DATA_PATH)
print("✅ Data loaded successfully!")
print(f"Shape: {df.shape}")
print("\nColumns:", list(df.columns))
print("\nPreview:\n", df.head())

# -------------------------------------
# Basic Info
# -------------------------------------
print("\nMissing values per column:\n", df.isna().sum())
print("\nData types:\n", df.dtypes)

# Convert date column to datetime (if exists)
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

# -------------------------------------
# Statistical Summary
# -------------------------------------
print("\nStatistical Summary:\n", df.describe())

# -------------------------------------
# 1️⃣ Distribution of total cases
# -------------------------------------
if 'total_cases' in df.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(df['total_cases'].dropna(), bins=40, kde=True)
    plt.title("Distribution of Total COVID-19 Cases")
    plt.xlabel("Total Cases")
    plt.ylabel("Frequency")
    plt.show()

# -------------------------------------
# 2️⃣ Correlation heatmap (numeric columns)
# -------------------------------------
plt.figure(figsize=(8,6))
corr = df.select_dtypes('number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap of Numeric Features")
plt.show()

# -------------------------------------
# 3️⃣ Top 10 countries by total cases
# -------------------------------------
if 'location' in df.columns and 'total_cases' in df.columns:
    latest = df.sort_values('date').groupby('location', as_index=False).last()
    top_cases = latest.nlargest(10, 'total_cases')

    plt.figure(figsize=(10,6))
    sns.barplot(x='total_cases', y='location', data=top_cases, palette='viridis')
    plt.title("Top 10 Countries by Total Cases")
    plt.xlabel("Total Cases")
    plt.ylabel("Country")
    plt.show()

# -------------------------------------
# 4️⃣ Total deaths vs total cases (scatter)
# -------------------------------------
if {'total_deaths', 'total_cases'}.issubset(df.columns):
    plt.figure(figsize=(8,6))
    sns.scatterplot(x='total_cases', y='total_deaths', hue='location', data=latest, legend=False)
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Total Deaths vs Total Cases (log scale)")
    plt.xlabel("Total Cases")
    plt.ylabel("Total Deaths")
    plt.show()

# -------------------------------------
# 5️⃣ Time series trend for India (example)
# -------------------------------------
if 'location' in df.columns and 'India' in df['location'].unique():
    india = df[df['location'] == 'India'].sort_values('date')
    plt.figure(figsize=(10,6))
    plt.plot(india['date'], india['total_cases'].ffill(), label='Total Cases')
    plt.plot(india['date'], india['total_deaths'].ffill(), label='Total Deaths')
    plt.title("COVID-19 Trend in India")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.legend()
    plt.show()

# -------------------------------------
# 6️⃣ Vaccination progress (if data available)
# -------------------------------------
if {'total_vaccinations', 'date', 'location'}.issubset(df.columns):
    india_vax = df[df['location'] == 'India']
    plt.figure(figsize=(10,6))
    plt.plot(india_vax['date'], india_vax['total_vaccinations'].ffill(), color='green', label='Total Vaccinations')
    plt.title("Vaccination Progress in India")
    plt.xlabel("Date")
    plt.ylabel("Total Vaccinations")
    plt.legend()
    plt.show()

# -------------------------------------
# 7️⃣ Stringency index over time (for India)
# -------------------------------------
if {'stringency_index', 'date', 'location'}.issubset(df.columns):
    india_str = df[df['location'] == 'India']
    plt.figure(figsize=(10,5))
    plt.plot(india_str['date'], india_str['stringency_index'].ffill(), color='orange')
    plt.title("Stringency Index Over Time (India)")
    plt.xlabel("Date")
    plt.ylabel("Stringency Index")
    plt.show()

print("\n🎯 EDA completed successfully! All plots have been displayed.")
