import re
import tkinter as tk
from tkinter import messagebox

# Password strength checker function
def check_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Include uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Include lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[!@#$%^&*()_+=\-{}\[\]:\";'<>?,./]", password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    if not re.search(r"(1234|password|qwerty|admin)", password.lower()):
        score += 1
    else:
        suggestions.append("Avoid common words or patterns.")

    if score <= 2:
        return "Weak", suggestions
    elif score <= 4:
        return "Medium", suggestions
    else:
        return "Strong", suggestions


# GUI application using tkinter
def evaluate_password():
    password = entry.get()
    strength, suggestions = check_strength(password)
    result_label.config(text=f"Strength: {strength}", fg="green" if strength == "Strong" else "orange" if strength == "Medium" else "red")

    suggestion_text.delete('1.0', tk.END)
    if suggestions:
        suggestion_text.insert(tk.END, "Suggestions:\n" + "\n".join(suggestions))
    else:
        suggestion_text.insert(tk.END, "Your password is strong!")

# GUI Setup
app = tk.Tk()
app.title("Password Strength Checker")
app.geometry("400x300")
app.config(bg="black")

tk.Label(app, text="Enter Password:", bg="black", fg="white", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(app, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(app, text="Check Strength", command=evaluate_password, bg="orange", font=("Arial", 11)).pack(pady=10)

result_label = tk.Label(app, text="", font=("Arial", 12), bg="black")
result_label.pack(pady=5)

suggestion_text = tk.Text(app, height=6, width=45, font=("Arial", 10))
suggestion_text.pack(pady=5)

app.mainloop()
