# Nails Salon Business Data Analysis

## Project Overview

This project analyzes real-world booking data from a small nail salon to uncover business insights and support data-driven decision-making. The goal is to better understand customer booking patterns, service demand, staff performance, and revenue trends while identifying opportunities to improve overall business operations.

## Objectives

- Analyze booking patterns and identify peak business hours, days and months.
- Identify popular services and customer preferences.
- Evaluate staff performance and service distribution.
- Examine revenue trends and appointment cancellations.
- Provide actionable recommendations for business improvement.

## Dataset

The project uses historical booking records from 2024, 2025, and 2026.

Key attributes include booking dates, appointment status, customer information, service names, staff assignments, service prices, and appointment times.

**Privacy:** Original customer data is kept private. Customer information is anonymized, and only synthetic sample data is shared in this repository.

## Project Workflow

1. **Data Cleaning:** 
- Combine booking files (3 files for three years: 2024, 2025, 2026)
- Address data quality issues (spelling errors, data types conversion, missing values)
- Anonymize customer information (using SHA-256)
- Engineer relevant features.
2. **Exploratory Data Analysis:** Explore booking trends (), service demand, staff performance, revenue, and cancellations.
3. **Business Insights:** Interpret findings and develop actionable recommendations for business improvement.

## Tools & Technologies

- Python
- Pandas & NumPy
- Matplotlib & Seaborn
- Jupyter Notebook
- Git & GitHub

## Project Structure

```text
Nails_Salon_DataAnalysis/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
│
├── notebooks/
│   ├── cleaning.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   └── 03_business_insights.ipynb
│
├── src/
│   └── anonymize.py
│
├── owner/
│   └── docs/
│       └── data_dictionary.md
│
├── .gitignore
└── README.md
```

## Project Status

**In Progress** — Data cleaning and preparation are underway, followed by exploratory analysis and business recommendations.