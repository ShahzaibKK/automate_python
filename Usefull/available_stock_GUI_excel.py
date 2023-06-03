import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import shutil
import os
from openpyxl import load_workbook


def browse_source_folder():
    folder_path = filedialog.askdirectory()
    source_folder_entry.delete(0, tk.END)
    source_folder_entry.insert(tk.END, folder_path)


def browse_destination_folder():
    folder_path = filedialog.askdirectory()
    destination_folder_entry.delete(0, tk.END)
    destination_folder_entry.insert(tk.END, folder_path)


def browse_excel_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")]
    )
    excel_file_entry.delete(0, tk.END)
    excel_file_entry.insert(tk.END, file_path)


def copy_files():
    source_folder = source_folder_entry.get()
    destination_folder = destination_folder_entry.get()
    excel_file = excel_file_entry.get()

    if source_folder == "" or destination_folder == "" or excel_file == "":
        messagebox.showerror("Error", "Please provide all the required information.")
        return

    try:
        workbook = load_workbook(excel_file)
        sheet = workbook.active
        column = sheet["A"]

        for cell in column:
            if cell.value is not None:
                filename = str(cell.value).strip()
                source_path = os.path.join(source_folder, f"{filename}.jpg")
                destination_path = os.path.join(destination_folder, f"{filename}.jpg")

                if os.path.exists(source_path):
                    shutil.copy(source_path, destination_path)
                    print(f"File copied: {filename}.jpg")
                else:
                    print(f"File not found: {filename}.jpg")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

    messagebox.showinfo("Success", "File copying completed.")


# Create the main window
window = tk.Tk()
window.title("File Copying Tool")

# Create and place the source folder label and entry
source_folder_label = tk.Label(window, text="Source Folder:")
source_folder_label.pack()
source_folder_entry = tk.Entry(window)
source_folder_entry.pack()
browse_source_folder_button = tk.Button(
    window, text="Browse", command=browse_source_folder
)
browse_source_folder_button.pack()

# Create and place the destination folder label and entry
destination_folder_label = tk.Label(window, text="Destination Folder:")
destination_folder_label.pack()
destination_folder_entry = tk.Entry(window)
destination_folder_entry.pack()
browse_destination_folder_button = tk.Button(
    window, text="Browse", command=browse_destination_folder
)
browse_destination_folder_button.pack()

# Create and place the Excel file label and entry
excel_file_label = tk.Label(window, text="Excel File:")
excel_file_label.pack()
excel_file_entry = tk.Entry(window)
excel_file_entry.pack()
browse_excel_file_button = tk.Button(window, text="Browse", command=browse_excel_file)
browse_excel_file_button.pack()

# Create and place the copy files button
copy_files_button = tk.Button(window, text="Copy Files", command=copy_files)
copy_files_button.pack()

# Start the main loop
window.mainloop()
