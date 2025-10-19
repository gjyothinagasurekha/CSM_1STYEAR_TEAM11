import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Name Entry Form")
root.geometry("350x300")
root.config(bg="#f0f4f7")

# Function to display confirmation message
def submit_details():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    
    if name == "" or email == "" or age == "":
         messagebox.showwarning("input Error","please fill all the fields.")
    else:
        messagebox.showinfo("Confirmation", f"Thank you, {name}!\nYour details have been recorded successfully.")

# Labels and Entry fields
tk.Label(root, text="Name Entry Form", font=("Arial", 14, "bold"), bg="#f0f4f7", fg="blue").pack(pady=10)

tk.Label(root, text="Full Name:", bg="#f0f4f7").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

tk.Label(root, text="Email:", bg="#f0f4f7").pack()
email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)

tk.Label(root, text="Age:", bg="#f0f4f7").pack()
age_entry = tk.Entry(root, width=30)
age_entry.pack(pady=5)

# Submit button
tk.Button(root, text="Submit", bg="green", fg="white", command=submit_details).pack(pady=15)

root.mainloop()