import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def select_source():
    global source_dir
    source_dir = filedialog.askdirectory()
    source_label.config(text=source_dir)

def select_destination():
    global destination_dir
    destination_dir = filedialog.askdirectory()
    destination_label.config(text=destination_dir)

def execute_files():
    if not source_dir or not destination_dir:
        messagebox.showerror("Error", "Please select both source and destination directories.")
        return
    
    file_ext = ext_entry.get().strip()
    if file_ext and not file_ext.startswith("."):
        file_ext = f".{file_ext}"  # Ensure the extension starts with a dot
    
    operation = "Cutting" if cut_var.get() else "Copying"
    
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if not file_ext or file.endswith(file_ext):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(destination_dir, file)
                if cut_var.get():  # If checkbox is selected, move (cut) the file
                    shutil.move(src_file, dest_file)
                else:  # Otherwise, copy the file
                    shutil.copy2(src_file, dest_file)
    
    messagebox.showinfo("Success", f"Files {operation} completed successfully!")

# Create the main window
root = tk.Tk()
root.title("File Copy/Cut Utility")

# Source Directory
tk.Label(root, text="Source Directory:", anchor="w").grid(row=0, column=0, padx=10, pady=10, sticky="w")
source_label = tk.Label(root, text="(No folder selected)", anchor="w", bg="white", relief="sunken")
source_label.grid(row=0, column=1, padx=10, sticky="ew")
tk.Button(root, text="Browse", command=select_source).grid(row=0, column=2, padx=10)

# Destination Directory
tk.Label(root, text="Destination Directory:", anchor="w").grid(row=1, column=0, padx=10, pady=10, sticky="w")
destination_label = tk.Label(root, text="(No folder selected)", anchor="w", bg="white", relief="sunken")
destination_label.grid(row=1, column=1, padx=10, sticky="ew")
tk.Button(root, text="Browse", command=select_destination).grid(row=1, column=2, padx=10)

# File Extension
tk.Label(root, text="File Extension (e.g., jpg, mp4):", anchor="w").grid(row=2, column=0, padx=10, pady=10, sticky="w")
ext_entry = tk.Entry(root)
ext_entry.grid(row=2, column=1, padx=10, sticky="ew")

# Cut Option
cut_var = tk.BooleanVar(value=False)  # Default to copy, checkbox checked means cut
tk.Checkbutton(root, text="Cut files", variable=cut_var, onvalue=True, offvalue=False).grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Execute Button
execute_button = tk.Button(root, text="Execute", command=execute_files)
execute_button.grid(row=4, column=0, columnspan=3, pady=20)

# Configure column weights
root.columnconfigure(1, weight=1)

# Start the Tkinter event loop
root.mainloop()
