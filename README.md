 Automatic Subscription Detector  
A Python-based smart tool that identifies recurring subscriptions (Netflix, Spotify, iCloud, Amazon Prime, Gym, etc.) from bank transaction history.  
This project detects subscription patterns using *date interval analysis, merchant normalization, and data preprocessing techniques.

Perfect for SDE, Data Engineering, and FinTech-related roles, demonstrating skills in Python, data processing, and pattern analysis.

---

## 🚀 Features

### 1. Automatic Subscription Detection
Detects recurring patterns such as:
- Monthly subscriptions  
- Weekly recurring payments  
- Annual charges  

### 2. Intelligent Data Preprocessing
- Cleans merchant names  
- Normalizes transaction descriptions  
- Converts messy date formats  
- Removes duplicates and invalid entries  

### 3. Pattern Recognition
Calculates:
- Monthly average cost  
- Annual projected cost  
- Number of transactions per merchant  

### 4. Clear Output Results
Outputs a clean table showing:
- Merchant  
- Frequency  
- Average recurrent amount  
- Annual cost  
- Transaction count  

---

## 🧠 How It Works

### 1. Preprocessing Layer (src/preprocess.py)
- Converts dates (dayfirst=True)  
- Parses amounts consistently  
- Cleans merchant names (regex cleaning)

### 2. Pattern Analysis Layer (src/pattern_analysis.py)
- Groups transactions by merchant  
- Detects recurring intervals (approx. 28–32 days)  
- Computes monthly & annual cost

---

## Folder Structure 

---

## 📁 Folder Structure
