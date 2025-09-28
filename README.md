# 💳 Credit Card Clients Default Analysis

This project explores the **Default of Credit Card Clients Dataset**, which contains demographic and financial information for **30,000 credit card holders in Taiwan**.  
The main goal is to perform **Exploratory Data Analysis (EDA)** and demonstrate how it can be turned into a **Flask web application** deployed online.

---

## 📒 Part 1: Jupyter Notebook (EDA)

### 📊 Dataset Overview
- **30,000 records**  
- **25 features** including:  
  - **Demographics**: `SEX`, `EDUCATION`, `MARRIAGE`, `AGE`  
  - **Credit information**: `LIMIT_BAL` (credit limit)  
  - **Payment history**: `PAY_0` … `PAY_6`  
  - **Bill statements**: `BILL_AMT1` … `BILL_AMT6`  
  - **Payments made**: `PAY_AMT1` … `PAY_AMT6`  
  - **Target variable**: `default payment next month`

### ⚙️ Features of the Notebook
- Load dataset from Excel using **pandas**  
- Data inspection (shape, info, missing values, unique values)  
- Summary statistics and data distribution checks  
- Visualizations with **matplotlib**:
  - Age distribution  
  - Gender and education breakdown  
  - Marriage status  
  - Payment history trends  
  - Default vs non-default clients  

---

## 🌐 Part 2: Flask Web App (Deployment)

This repository also contains a **Flask web application** built on the same dataset.  
It demonstrates how analysis can be served as an **interactive web app**, deployed with **Render**.

### 🚀 Live Demo
👉 [https://credit-card-client-project-6.onrender.com](https://credit-card-client-project-6.onrender.com)

Available routes:
- `/` → Homepage  
- `/summary` → Dataset summary statistics  
- `/plot` → Age distribution visualization  

### 📂 Project Structure
credit_card_clients_app/
├── app.py # Flask application
├── requirements.txt # Python dependencies
├── default_of_credit_card_clients_0.xlsx # Dataset (demo)


### ⚙️ Run Locally

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd credit_card_clients_app
pip install -r requirements.txt
python app.py

Visit http://127.0.0.1:5000

🌐 Render Deployment

Build Command
pip install -r requirements.txt

Start Command
gunicorn credit_card_clients_app:app

✅ Future Work

Add styled HTML templates

More visualizations (e.g., payment defaults by education)

Cloud storage/database integration

## 📜 License

For educational purposes.  
Dataset source: UCI Machine Learning Repository

