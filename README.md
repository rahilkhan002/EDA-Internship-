**🦠 COVID-19 Exploratory Data Analysis (EDA)**


📘 Project Overview

This project performs Exploratory Data Analysis (EDA) on a cleaned and structured COVID-19 dataset (synthetic_cleaned_covid_data.csv).
The goal is to explore trends, correlations, and insights related to cases, deaths, vaccinations, and government stringency measures across countries and over time.

All analysis and visualizations are performed in Python using pandas, matplotlib, and seaborn, with results displayed interactively (plt.show()), without saving external files.

🚀 Key Objectives

Understand global and country-level COVID-19 trends

Identify the top affected countries by total cases and deaths

Analyze the relationship between total cases and deaths

Explore vaccination progress and government stringency index trends

Provide data-driven insights through clear and interpretable visualizations

🧩 Dataset

File: synthetic_cleaned_covid_data.csv
The dataset contains cleaned COVID-19 data derived from Our World in Data (OWID).
Typical columns include:

location — Country name

iso_code — Country code

date — Date of record

total_cases, new_cases — Reported case counts

total_deaths, new_deaths — Reported deaths

total_vaccinations, people_vaccinated, people_fully_vaccinated — Vaccination progress

stringency_index — Government response intensity

population — Country population

📊 Analysis & Visualizations
🔹 1. Data Overview

Displayed basic info, data types, and missing values

Summarized dataset statistics using describe()

🔹 2. Distribution Analysis

Histogram of total COVID-19 cases across all countries

Highlights data skew and global variation in case numbers

🔹 3. Correlation Analysis

Heatmap of key numerical variables

Helps identify strong relationships (e.g., between cases and deaths, or cases and vaccinations)

🔹 4. Top 10 Countries by Total Cases

Bar chart showing countries most affected by total case counts

🔹 5. Total Deaths vs Total Cases

Scatter plot (log-log scale) showing how deaths scale with total cases per country

🔹 6. Time-Series Analysis (India Example)

Line plot of total cases and total deaths over time for India

Shows the pandemic’s evolution and trend patterns

🔹 7. Vaccination Progress

Line plot of total vaccinations in India over time

Visualizes how vaccine rollout progressed

🔹 8. Government Stringency Index

Line chart of stringency index for India

Shows how government restrictions changed over time

🛠️ Technologies Used
Tool / Library	Purpose
Python 3	Programming language
pandas	Data manipulation and cleaning
NumPy	Numerical computations
matplotlib	Core plotting library
seaborn	Advanced statistical visualizations
Pathlib	Clean and efficient file path handling
🧠 Insights

Countries with larger populations tend to have higher total cases but varying fatality ratios.

Vaccination rollouts and lower stringency indexes correlate with declining case/death trends.

The correlation heatmap revealed strong relationships between total_cases and total_deaths.

📦 How to Run

Clone the repository:

git clone https://github.com/<your-username>/covid19-eda.git
cd covid19-eda


Install dependencies:

pip install pandas numpy matplotlib seaborn


Run the EDA script:

python covid_eda_analysis.py


All visualizations will appear as pop-up plots using plt.show().

📈 Example Output Visuals

(Add images or screenshots of your plots here once you run the script.)

Distribution of total cases

Top 10 countries by total cases

Correlation heatmap

COVID-19 time series (India)

Vaccination trend

🧾 Author

Rahil Khan
📍 Data Science & Analytics Enthusiast
🔗 LinkedIn

⭐ Future Improvements

Add interactive dashboards (Plotly or Power BI)

Automate country selection for analysis

Integrate predictive modeling for case forecasting
