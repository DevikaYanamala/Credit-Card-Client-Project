# 💳 Credit Card Clients Default Analysis

This project explores the **Default of Credit Card Clients Dataset**, which contains demographic and financial information for **30,000 credit card holders in Taiwan**.  
The main goal is to perform **Exploratory Data Analysis (EDA)** to understand the factors that may influence **default payment risk**.

---

## 📊 Dataset Overview
- **30,000 records**  
- **25 features** including:  
  - **Demographics**: `SEX`, `EDUCATION`, `MARRIAGE`, `AGE`  
  - **Credit information**: `LIMIT_BAL` (credit limit)  
  - **Payment history**: `PAY_0` … `PAY_6` (repayment status for past 6 months)  
  - **Bill statements**: `BILL_AMT1` … `BILL_AMT6`  
  - **Payments made**: `PAY_AMT1` … `PAY_AMT6`  
  - **Target variable**: `default payment next month`  

---

## ⚙️ Features of the Notebook
- Load dataset from Excel using **pandas**  
- Data inspection (shape, info, missing values, unique values)  
- Summary statistics and data distribution checks  
- Visualizations using **matplotlib** to explore:  
  - Age distribution  
  - Gender and education breakdown  
  - Marriage status  
  - Payment history trends  
  - Default vs non-default clients  

---

## 🚀 Tech Stack
- **Python 3**  
- **pandas** → data manipulation  
- **NumPy** → numerical computations  
- **matplotlib** → visualization  

---

## 🔧 Installation & Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/DevikaYanamala/Credit-Card-Client-Project.git
   cd Credit-Card-Client-Project
   pip install -r requirements.txt
   jupyter notebook credi_card_clients_project.ipynb

