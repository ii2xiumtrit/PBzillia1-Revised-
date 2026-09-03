import tkinter as tk
from tkinter import ttk
import psutil

# main
root = tk.Tk()
root.title("PBzillia")
root.geometry("550x550")
root.maxsize(550, 550)
root.resizable(False, False)
# root.configure(bg="black")


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

graph = tk.Canvas(
    content,
    width=400,
    height=150,
    bg="white",
    highlightthickness=1
)
graph.grid(pady=10)




ram_history = []

ram_label = tk.Label(
    content,
    justify="left"
)

ram_label.grid(sticky="w")

def update_ram():
    ram = psutil.virtual_memory()

    # Update text
    ram_label.config(
        text=f"Total RAM:     {ram.total / (1024**3):.2f} GB\n"
             f"Used RAM:      {ram.used / (1024**3):.2f} GB\n"
             f"Available RAM: {ram.available / (1024**3):.2f} GB\n"
             f"RAM Usage:     {ram.percent}%"
    )

    # Save RAM percentage
    ram_history.append(ram.percent)

    # Keep only the latest 50 readings
    if len(ram_history) > 50:
        ram_history.pop(0)

    # Clear graph
    graph.delete("all")

    # Draw graph
    for i in range(1, len(ram_history)):
        x1 = (i - 1) * 400 / 50
        y1 = 150 - (ram_history[i - 1] * 150 / 100)

        x2 = i * 400 / 50
        y2 = 150 - (ram_history[i] * 150 / 100)

        graph.create_line(x1, y1, x2, y2, width=2)

    root.after(200, update_ram)


update_ram()


root.mainloop()
