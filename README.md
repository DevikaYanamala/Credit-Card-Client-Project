# Credit-Card-Client-Project
📌 Project Description

This project analyzes the Default of Credit Card Clients Dataset, which contains demographic and financial information of 30,000 credit card holders from Taiwan.
The goal is to perform Exploratory Data Analysis (EDA) and prepare the dataset for potential predictive modeling (default payment prediction).

# 💳 Credit Card Clients Default Analysis

This repository contains an exploratory data analysis (EDA) of the **Default of Credit Card Clients Dataset**, which consists of information about 30,000 credit card holders.  
The objective is to analyze customer demographics, payment history, bill statements, and repayment behavior to understand key factors contributing to **default payment risk**.

---

## 📊 Project Overview
The dataset contains the following:
- **30,000 entries**, each representing a credit card holder  
- **25 features** including:
  - Demographics: `SEX`, `EDUCATION`, `MARRIAGE`, `AGE`
  - Credit Limit: `LIMIT_BAL`
  - Payment history: `PAY_0` … `PAY_6`
  - Bill statements: `BILL_AMT1` … `BILL_AMT6`
  - Payments: `PAY_AMT1` … `PAY_AMT6`
  - Target: `default payment next month`

---

## ⚙️ Features
- Data loading from Excel dataset  
- Inspection of dataset structure, unique values, and distributions  
- Data cleaning & handling categorical features  
- Exploratory data analysis (EDA) using **matplotlib** & **seaborn**  
- Visualizations of payment delays, age distribution, education levels, marriage status, and default trends  

---

## 🚀 Tech Stack
- **Python 3**  
- **pandas** for data manipulation  
- **NumPy** for numerical operations  
- **matplotlib** & **seaborn** for visualization  

---

## 🔧 Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/DevikaYanamala/Credit-Card-Client-Project.git
   cd Credit-Card-Client-Project
   pip install -r requirements.txt
   jupyter notebook credi_card_clients_project.ipynb

