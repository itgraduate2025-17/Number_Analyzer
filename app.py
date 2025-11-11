import tkinter as tk
from tkinter import messagebox
import math

# -------------------------
# Functions
# -------------------------

def check_even_odd():
    try:
        n = int(entry.get())
        if n % 2 == 0:
            messagebox.showinfo("Result", f"{n} is Even")
        else:
            messagebox.showinfo("Result", f"{n} is Odd")
    except:
        messagebox.showerror("Error", "Enter a valid number!")

def check_sign():
    try:
        n = int(entry.get())
        if n > 0:
            messagebox.showinfo("Result", f"{n} is Positive")
        elif n < 0:
            messagebox.showinfo("Result", f"{n} is Negative")
        else:
            messagebox.showinfo("Result", "Number is Zero")
    except:
        messagebox.showerror("Error", "Enter a valid number!")

def check_prime():
    try:
        n = int(entry.get())
        if n <= 1:
            messagebox.showinfo("Result", f"{n} is not Prime")
            return
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                messagebox.showinfo("Result", f"{n} is not Prime")
                return
        messagebox.showinfo("Result", f"{n} is Prime")
    except:
        messagebox.showerror("Error", "Enter a valid number!")

def find_factorial():
    try:
        n = int(entry.get())
        if n < 0:
            messagebox.showerror("Error", "No factorial for negative numbers!")
            return
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        messagebox.showinfo("Result", f"Factorial of {n} is {fact}")
    except:
        messagebox.showerror("Error", "Enter a valid number!")

def find_sqrt():
    try:
        n = float(entry.get())
        if n < 0:
            messagebox.showerror("Error", "No real square root for negative numbers!")
            return
        sq = math.sqrt(n)
        messagebox.showinfo("Result", f"Square root of {n} = {sq:.2f}")
    except:
        messagebox.showerror("Error", "Enter a valid number!")

def clear_box():
    entry.delete(0, tk.END)

# -------------------------
# GUI Design
# -------------------------

root = tk.Tk()
root.title("Number Analyzer")
root.geometry("800x600")
root.config(bg="#cfe2ff")

main_frame = tk.Frame(root, bg="white", bd=5, relief="ridge")
main_frame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=400)

title = tk.Label(main_frame, text="Number Analyzer", font=("Arial Rounded MT Bold", 18),
                 bg="white", fg="#0a2472")
title.pack(pady=10)

entry = tk.Entry(main_frame, font=("Arial", 16), justify="center", width=15, bd=3, relief="solid")
entry.pack(pady=10)

btn_frame = tk.Frame(main_frame, bg="white")
btn_frame.pack(pady=15)

def make_btn(text, color, cmd):
    return tk.Button(btn_frame, text=text, font=("Arial", 10, "bold"),
                     bg=color, fg="white", width=10, height=1, relief="flat",
                     activebackground="#333333", command=cmd)

make_btn("Even/Odd", "#093d81", check_even_odd).grid(row=0, column=0, padx=8, pady=8)
make_btn("+ / -", "#01350F", check_sign).grid(row=0, column=1, padx=8, pady=8)
make_btn("Prime", "#705503", check_prime).grid(row=0, column=2, padx=8, pady=8)
make_btn("Factorial", "#3D0347", find_factorial).grid(row=1, column=0, padx=8, pady=8)
make_btn("√", "#240901", find_sqrt).grid(row=1, column=1, padx=8, pady=8)
make_btn("Clear", "#5f6368", clear_box).grid(row=1, column=2, padx=8, pady=8)

exit_btn = tk.Button(main_frame, text="Exit", font=("Arial", 11, "bold"),
                     bg="#d93025", fg="white", width=12, relief="flat",
                     command=root.destroy)
exit_btn.pack(pady=10)

root.mainloop()
