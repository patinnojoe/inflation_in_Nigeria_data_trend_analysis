# Nigeria Inflation Dynamics Analysis (2019–2025)

## Project Overview

This project analyzes inflation trends in Nigeria between 2019 and 2025 using monthly Consumer Price Index (CPI) data. The analysis explores how inflation evolved across major sectors of the Nigerian economy, with special attention to:

- Food inflation
- Transport inflation
- Housing and energy costs
- Core vs headline inflation
- The effects of COVID-19
- The effects of fuel subsidy removal and FX liberalization
- Inflation volatility and structural changes

The goal of this project is to combine:

- Data analysis
- Economic reasoning
- Public policy interpretation
- Data storytelling
- Visualization

This project is designed as both:

1. A portfolio-quality data analysis project
2. A public policy/data journalism article

---

# Research Questions

## Primary Questions

Question 1: How has headline inflation evolved in scale and volatility across Nigeria from 2019 to 2025?

Question 2: Did the June 2023 fuel subsidy removal trigger a permanent structural regime shift in inflation dynamics?

Question 3: Which specific CPI consumption categories drove this price expansion, and which sectors exhibited the highest month-on-month volatility?

---

# Dataset Description

The dataset contains 84 monthly observations from January 2019 to December 2025.

## Dataset Dimensions

- Rows: 84
- Columns: 30

## Key Variables

### General Inflation Indicators

| Column               | Description                      |
| -------------------- | -------------------------------- |
| All Items            | Headline CPI                     |
| Month-on (%)         | Monthly inflation rate           |
| Year-on (%)          | Yearly inflation rate            |
| 12-month average (%) | Rolling yearly average inflation |

---

### Core Inflation Measures

| Column                                  | Description            |
| --------------------------------------- | ---------------------- |
| All Items less Farm Produce.            | Core inflation         |
| All Items less Farm Produce. and Energy | Refined core inflation |
| ALL ITEMS LESS FOOD (NONFOOD INDEX)     | Non-food inflation     |

---

### Food Inflation Metrics

| Column                    | Description                  |
| ------------------------- | ---------------------------- |
| Food                      | Food CPI                     |
| Imported Food             | Imported food inflation      |
| Food & Non Alcoholic Bev. | Food-related consumer prices |
| FARM PRODUCE              | Farm produce inflation       |

---

### Sectoral Inflation Categories

| Column                                           | Description                     |
| ------------------------------------------------ | ------------------------------- |
| Transport                                        | Transportation costs            |
| Health.                                          | Healthcare inflation            |
| EDUCATION SERVICES                               | Education-related costs         |
| HOUSING, WATER, ELECTRICITY, GAS AND OTHER FUELS | Housing and utilities           |
| INFORMATION AND COMMUNICATION                    | Telecom and communication costs |
| RECREATION, SPORT AND CULTURE                    | Entertainment and recreation    |

---

# Project Objectives

The project aims to:

- Understand inflation trends in Nigeria
- Identify periods of economic instability
- Analyze policy-related inflation shocks
- Compare sectoral inflation behavior
- Visualize inflation growth over time
- Build an analytical narrative around economic hardship and cost-of-living increases

---

# Proposed Analysis Sections

## 1. Data Cleaning and Preparation

### Tasks

- Handle missing values
- Standardize column names
- Create datetime column
- Convert Month + Year into proper timestamps
- Validate data consistency
- Separate sparse columns from complete columns

### Expected Output

- Cleaned analysis-ready DataFrame

---

## 2. Exploratory Data Analysis (EDA)

### Questions

- What does the inflation distribution look like?
- Which sectors have the highest average inflation?
- Which categories are most volatile?
- Are there visible structural breaks?

### Techniques

- Summary statistics
- Histograms
- Correlation matrices
- Line plots
- Rolling averages

---

## 3. Headline Inflation Trend Analysis

### Questions

- How did overall inflation evolve?
- Which years experienced the largest increases?
- Was inflation stable before COVID?

### Suggested Visualizations

- Line chart of headline inflation
- Rolling average inflation trend
- Yearly grouped inflation averages

---

## 4. Food Inflation Analysis

### Questions

- Is food inflation consistently higher than headline inflation?
- Did imported food inflation accelerate after FX liberalization?
- Which period experienced the strongest food inflation growth?

### Suggested Visualizations

- Food vs headline inflation line chart
- Imported food inflation trend
- Inflation gap visualization

---

## 5. Transport and Energy Shock Analysis

### Questions

- Did transport inflation spike after fuel subsidy removal?
- Is transport inflation strongly correlated with headline inflation?
- How severe was the post-2023 increase?

### Suggested Visualizations

- Transport inflation timeline
- Pre/post subsidy comparison
- Correlation heatmap

---

## 6. COVID-19 Inflation Impact

### Questions

- Did inflation accelerate during the pandemic?
- Which categories were most affected?
- Was inflation volatility higher during COVID?

### Suggested Time Segments

| Period           | Range     |
| ---------------- | --------- |
| Pre-COVID        | 2019      |
| COVID Shock      | 2020–2021 |
| Recovery         | 2022      |
| Subsidy/FX Shock | 2023–2025 |

---

## 7. Structural Break and Policy Analysis

### Major Policy Events

| Event                | Approximate Period |
| -------------------- | ------------------ |
| COVID Economic Shock | 2020               |
| Fuel Subsidy Removal | 2023               |
| FX Liberalization    | 2023               |
| CPI Rebasing         | 2024               |

### Questions

- Did inflation patterns change after policy interventions?
- Which sectors reacted most strongly?
- Did inflation persistence increase?

---

## 8. Inflation Volatility Analysis

### Questions

- Which CPI categories are most unstable?
- Which categories show consistent upward pressure?
- Are some categories more resilient?

### Suggested Metrics

- Standard deviation
- Rolling volatility
- Monthly percentage changes

---

## 9. Correlation Analysis

### Questions

- Which sectors move together?
- Does transport inflation correlate strongly with food inflation?
- Which sectors influence headline inflation most?

### Suggested Techniques

- Correlation matrix
- Heatmap visualization
- Scatter plots

---

## 10. Inflation Narrative and Economic Implications

### Themes

- Cost of living crisis
- Purchasing power erosion
- Transportation burden
- Food insecurity
- Housing pressure
- Economic vulnerability

### Policy Questions

- What sectors require intervention?
- How do inflation shocks affect ordinary Nigerians?
- What patterns suggest structural inflation problems?

---

# Recommended Visualizations

## Essential Charts

### Trend Visualizations

- Headline inflation trend
- Food inflation trend
- Transport inflation trend
- Imported food inflation trend

---

### Comparative Charts

- Food vs headline inflation
- Core vs headline inflation
- Pre/post policy event comparisons

---

### Statistical Visualizations

- Correlation heatmap
- Monthly volatility plots
- Distribution histograms
- Rolling averages

---

# Proposed Folder Structure

```text
inflation-analysis/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_trend_analysis.ipynb
│   ├── 04_policy_analysis.ipynb
│   └── 05_visualization.ipynb
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── cleaning.py
│   ├── visualization.py
│   └── analysis.py
│
├── visuals/
│
├── output/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Technologies Used

| Tool             | Purpose                 |
| ---------------- | ----------------------- |
| Python           | Analysis language       |
| pandas           | Data manipulation       |
| matplotlib       | Visualization           |
| NumPy            | Numerical operations    |
| Jupyter Notebook | Exploratory analysis    |
| VS Code          | Development environment |

---

# Suggested Python Libraries

```bash
pip install pandas matplotlib numpy jupyter seaborn
```

---

# Expected Skills Demonstrated

This project demonstrates:

- Data cleaning
- Exploratory data analysis
- Time-series analysis
- Statistical reasoning
- Public policy interpretation
- Visualization design
- Data storytelling
- Research communication

---

# Potential Extensions

## Future ML/Advanced Analysis

This project can later be extended into:

- Inflation forecasting
- ARIMA models
- Prophet forecasting
- Volatility modeling
- Regime detection
- Economic anomaly detection
- Policy impact modeling

---

# Potential Article Titles

## General Analysis

- 10 Years of Inflation in Nigeria
- Nigeria’s Cost of Living Crisis
- Understanding Inflation Dynamics in Nigeria

---

## Policy-Focused

- What Fuel Subsidy Removal Did to Inflation
- How Food Prices Became Nigeria’s Biggest Economic Pressure
- The Hidden Drivers of Inflation in Nigeria

---

# Methodology Notes

The dataset was sourced from Nigerian CPI and inflation reports compiled from the National Bureau of Statistics (NBS).

The analysis focuses on:

- descriptive statistics
- time-series exploration
- sectoral comparison
- policy-event interpretation

This project does not attempt to establish strict causal relationships, but instead identifies observable patterns and economic trends.

---

# Key Deliverables

## Technical Deliverables

- Cleaned dataset
- Jupyter notebooks
- Visualizations
- Reusable analysis functions
- GitHub repository

---

## Communication Deliverables

- Medium article
- Research-style writeup
- Policy commentary
- Data storytelling visuals

---

# Author Goals

This project was created to:

- strengthen practical data analysis skills
- explore real-world economic datasets
- improve statistical intuition
- develop public policy analysis capabilities
- build a portfolio-ready research project
- combine AI/data science with societal and economic analysis
