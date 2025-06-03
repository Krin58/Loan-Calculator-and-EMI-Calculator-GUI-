import tkinter as tk
from tkinter import messagebox

def calculate_emi(principal, annual_rate, months):
    monthly_rate = annual_rate / (12 * 100)
    if monthly_rate == 0:
        return principal / months
    emi = principal * monthly_rate * (((1 + monthly_rate) ** months) / (((1 + monthly_rate) ** months) - 1))
    return emi

def show_stats():
    stats = "The list of banks and their rate of interest:\n"
    stats += "+---------------------+---------------------+-----------------------+\n"
    stats += "| Banks                    | Loan Type            | Rate of Interest    |\n"
    stats += "+---------------------+---------------------+-----------------------+\n"
    D = {"ICICI": {'Car': 9.1, 'Home': 8.75, 'Gold': 9.25},
         "HDFC": {'Car': 9.4, 'Home': 8.5, 'Gold': 9.3},
         "SBI": {'Car': 9.2, 'Home': 8, 'Gold': 9}}
    for bank, loans in D.items():
        for loan_type, rate in loans.items():
            stats += f"| {bank:<5} \t\t| {loan_type:<13} \t| {rate:<21} \t|\n"
    stats += "+---------------------+---------------------+-----------------------+\n"
    return stats

def calculate_loan():
    try:
        loan_type = loan_type_var.get()
        total_amount = float(total_amount_entry.get())
        down_payment = float(down_payment_entry.get())
        principal = total_amount - down_payment
        bank_name = bank_name_var.get()

        D = {"ICICI": {'Car': 9.1, 'Home': 8.75, 'Gold': 9.25},
             "HDFC": {'Car': 9.4, 'Home': 8.5, 'Gold': 9.3},
             "SBI": {'Car': 9.2, 'Home': 8, 'Gold': 9}}
        
        annual_rate = D[bank_name][loan_type]
        months = int(tenure_entry.get())

        emi = calculate_emi(principal, annual_rate, months)
        total_payment = emi * months
        total_interest = total_payment - principal
        interest_pct = (total_interest / total_payment) * 100

        result = f"\n--- Loan Summary for {loan_type.title()} Loan ---\n"
        result += f"Monthly EMI: ₹{emi:.2f}\n"
        result += f"Total Interest Payable: ₹{total_interest:.2f}\n"
        result += f"Total Repayment Amount: ₹{total_payment:.2f}\n"
        result += f"Interest as % of Total Repayment: {interest_pct:.2f}%"
        
        messagebox.showinfo("Loan Summary", result)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Loan EMI & Interest Calculator")

# Bank and Loan Type Selection
bank_name_var = tk.StringVar(value="ICICI")
loan_type_var = tk.StringVar(value="Car")

# Bank Selection
tk.Label(root, text="Select Bank:").grid(row=0, column=0)
tk.OptionMenu(root, bank_name_var, "ICICI", "HDFC", "SBI").grid(row=0, column=1)

# Loan Type Selection
tk.Label(root, text="Select Loan Type:").grid(row=1, column=0)
tk.OptionMenu(root, loan_type_var, "Car", "Home", "Gold").grid(row=1, column=1)

# Total Amount Entry
tk.Label(root, text="Total Loan Amount:").grid(row=2, column=0)
total_amount_entry = tk.Entry(root)
total_amount_entry.grid(row=2, column=1)

# Down Payment Entry
tk.Label(root, text="Down Payment:").grid(row=3, column=0)
down_payment_entry = tk.Entry(root)
down_payment_entry.grid(row=3, column=1)

# Tenure Entry
tk.Label(root, text="Loan Tenure (months):").grid(row=4, column=0)
tenure_entry = tk.Entry(root)
tenure_entry.grid(row=4, column=1)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate EMI", command=calculate_loan)
calculate_button.grid(row=5, columnspan=2)

# Show Bank Stats Button
show_stats_button = tk.Button(root, text="Show Bank Stats", command=lambda: messagebox.showinfo("Bank Stats", show_stats()))
show_stats_button.grid(row=6, columnspan=2)

# Start the GUI event loop
root.mainloop()
