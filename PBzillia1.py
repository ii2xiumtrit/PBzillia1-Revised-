import tkinter as tk
from tkinter import ttk
import psutil

# main
root = tk.Tk()
root.title("PBzillia")
root.geometry("550x550")
root.maxsize(550, 550)
root.resizable(False, False)
root.configure(bg="black")


# ribbon

ribbon = tk.Frame(root, height=50, bd=1, relief="flat")
ribbon.pack(fill="x")

# Ribbon tabs
tabs = ttk.Notebook(ribbon)
tabs.pack(fill="x")

home_tab = tk.Frame(tabs)
settings_tab = tk.Frame(tabs)

tabs.add(home_tab, text="Home")
tabs.add(settings_tab, text="Settings")


# ===== Home tab buttons =====


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


# Main tab

content = tk.Frame(root)
content.pack(fill="both", expand=True)

# tk.Label(
#     content,
#     text="Main program area"
# ).pack(pady=50)
#Example

#Ram Usage
ram = psutil.virtual_memory()

#diagram here

ram_label = tk.Label(
    content,
    justify="left"
)
ram_label.grid(sticky="w")

def update_ram():
    ram = psutil.virtual_memory()

    ram_label.config(
        text=f"Total RAM:     {ram.total / (1024**3):.2f} GB\n"
             f"Used RAM:      {ram.used / (1024**3):.2f} GB\n"
             f"Available RAM: {ram.available / (1024**3):.2f} GB\n"
             f"RAM Usage:     {ram.percent}%"
    )

    root.after(500, update_ram)  # run again after 2 seconds


update_ram()



root.mainloop()
