# Loan-Calculator-and-EMI-Calculator-GUI-

# 🧮 Loan & EMI Calculator in Python

## 📌 Overview

This is a simple Python-based **Loan and EMI Calculator** that helps users compute:
- Monthly EMI (Equated Monthly Installment)
- Total interest payable
- Total repayment amount

This tool is useful for individuals to plan their loan repayments by understanding the financial burden over time based on different inputs like loan amount, interest rate, and tenure.

---

## ⚙️ Features

- Calculate EMI for a loan based on user inputs
- Display total interest and total repayment
- User-friendly input/output in console
- Accurate financial calculations using standard EMI formula

---

## 📐 EMI Formula

The standard EMI formula is:

EMI = [P × R × (1+R)^N] / [(1+R)^N – 1]


Where:
- `P` = Loan Amount (Principal)
- `R` = Monthly Interest Rate (Annual Rate / 12 / 100)
- `N` = Tenure (in months)

---

## 💻 How to Use

1. Clone or download this repository.
2. Make sure you have Python 3 installed.
3. Run the script using:

```bash
python Loan Calculator GUI.py

```

Enter:

    Loan amount (e.g., 500000)

    Annual interest rate (e.g., 7.5)

    Tenure in years (e.g., 5)

The calculator will output:

    EMI per month

    Total interest payable

    Total amount to be repaid
