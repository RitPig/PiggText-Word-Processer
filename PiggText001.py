import tkinter as tk
from tkinter import filedialog, Text

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as f:
            f.write(text_area.get("1.0", tk.END))

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "r") as f:
            text_area.delete("1.0", tk.END)
            text_area.insert("1.0", f.read())

root = tk.Tk()
root.title("PiggText v0.01")

text_area = Text(root)
text_area.pack(expand=True, fill="both")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Open", command=open_file)
root.config(menu=menu_bar)

root.mainloop()
