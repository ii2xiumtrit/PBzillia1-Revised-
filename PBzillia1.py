import tkinter as tk
from tkinter import ttk

# main
root = tk.Tk()
root.title("PBzillia")
root.geometry("550x550")
root.maxsize(550, 550)
root.resizable(False, False)

# ===== Ribbon =====

ribbon = tk.Frame(root, height=100, bd=1, relief="raised")
ribbon.pack(fill="x")

# Ribbon tabs
tabs = ttk.Notebook(ribbon)
tabs.pack(fill="x")

home_tab = tk.Frame(tabs)
settings_tab = tk.Frame(tabs)

tabs.add(home_tab, text="Home")
tabs.add(settings_tab, text="Settings")


# ===== Home tab buttons =====

tk.Button(
    home_tab,
    text="New",
    width=10
).pack(side="left", padx=5, pady=10)

tk.Button(
    home_tab,
    text="Open",
    width=10
).pack(side="left", padx=5, pady=10)

tk.Button(
    home_tab,
    text="Save",
    width=10
).pack(side="left", padx=5, pady=10)


# settings

tk.Button(
    settings_tab,
    text="Scanner",
    width=10
).pack(side="left", padx=5, pady=10)

tk.Button(
    settings_tab,
    text="Settings",
    width=10
).pack(side="left", padx=5, pady=10)


# ===== Main content =====

content = tk.Frame(root)
content.pack(fill="both", expand=True)

tk.Label(
    content,
    text="Main program area"
).pack(pady=50)

root.mainloop()
