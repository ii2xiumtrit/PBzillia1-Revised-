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


# ===== Settings tab buttons =====

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


home_container = tk.Frame(root)
home_container.pack(
    fill="both",
    expand=True
)


home_canvas = tk.Canvas(
    home_container,
    highlightthickness=0
)

home_canvas.pack(
    side="left",
    fill="both",
    expand=True
)


home_scrollbar = ttk.Scrollbar(
    home_container,
    orient="vertical",
    command=home_canvas.yview
)

home_scrollbar.pack(
    side="right",
    fill="y"
)


home_canvas.configure(
    yscrollcommand=home_scrollbar.set
)


content = tk.Frame(home_canvas)

content_window = home_canvas.create_window(
    (0, 0),
    window=content,
    anchor="nw"
)


def update_scroll_region(event):
    home_canvas.configure(
        scrollregion=home_canvas.bbox("all")
    )


content.bind(
    "<Configure>",
    update_scroll_region
)


# Make content fill the width
def resize_content(event):
    home_canvas.itemconfig(
        content_window,
        width=event.width
    )


home_canvas.bind(
    "<Configure>",
    resize_content
)


# Mouse wheel scrolling
def scroll_home(event):
    home_canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )


home_canvas.bind(
    "<MouseWheel>",
    scroll_home
)



ram_label = tk.Label(
    content,
    justify="left"
)

ram_label.grid(
    sticky="w",
    padx=10
)



ram_graph = tk.Canvas(
    content,
    width=450,
    height=180,
    bg="white",
    highlightthickness=1
)

ram_graph.grid(
    pady=10
)


ram_history = []



process_graph = tk.Canvas(
    content,
    width=450,
    height=180,
    bg="white",
    highlightthickness=1
)

process_graph.grid(
    pady=10
)



def update_ram():

    ram = psutil.virtual_memory()

    ram_label.config(
        text=f"Total RAM:     {ram.total / (1024**3):.2f} GB\n"
             f"Used RAM:      {ram.used / (1024**3):.2f} GB\n"
             f"Available RAM: {ram.available / (1024**3):.2f} GB\n"
             f"RAM Usage:     {ram.percent}%"
    )




    ram_history.append(ram.percent)


    if len(ram_history) > 50:
        ram_history.pop(0)



    ram_graph.delete("all")


    for percent in [0, 25, 50, 75, 100]:

        y = 160 - (percent * 1.5)

        
        ram_graph.create_line(
            0,
            y,
            410,
            y,
            fill="lightgray"
        )

       
        ram_graph.create_text(
            440,
            y,
            text=f"{percent}%",
            fill="black",
            anchor="e"
        )
        

    for i in range(1, len(ram_history)):

        x1 = (i - 1) * 410 / 49
        y1 = 160 - (ram_history[i - 1] * 1.5)

        x2 = i * 410 / 49
        y2 = 160 - (ram_history[i] * 1.5)

        ram_graph.create_line(
            x1,
            y1,
            x2,
            y2,
            width=2,
            fill="blue"
        )


    
    # RAM USAGE
    

    process_graph.delete("all")

    processes = []


    
    for process in psutil.process_iter(
        ["name", "memory_info"]
    ):

        try:

            name = process.info["name"]
            memory = process.info["memory_info"].rss

            processes.append(
                (name, memory)
            )

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            pass


    # Sort 
    processes.sort(
        key=lambda x: x[1],
        reverse=True
    )

    

    # Process Graph
    top_processes = processes[:10]
    y = 25


    for name, memory in top_processes:

        memory_mb = memory / (1024 ** 2)


       
        if len(name) > 18:
            name = name[:18] + "..."


        
        bar_width = min(
            memory_mb / 10,
            250
        )


        
        process_graph.create_text(
            5,
            y,
            text=name,
            anchor="w",
            fill="black"
        )


        
        process_graph.create_rectangle(
            140,
            y - 7,
            140 + bar_width,
            y + 7,
            fill="blue"
        )


        
        process_graph.create_text(
            440,
            y,
            text=f"{memory_mb:.0f} MB",
            anchor="e",
            fill="black"
        )


        y += 30


    
    root.after(
       1000,
        update_ram
    )


update_ram()


root.mainloop()