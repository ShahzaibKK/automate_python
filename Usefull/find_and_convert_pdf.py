import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import shutil
import os
from openpyxl import load_workbook
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime
import threading


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


def compress_image(image_path, destination_folder):
    image = Image.open(image_path)
    image = image.convert("RGB")
    image.thumbnail((2000, 2000))  # Adjust the size as per your requirements

    # Generate a new file name for the compressed image
    filename = os.path.basename(image_path)
    compressed_image_path = os.path.join(destination_folder, f"compressed_{filename}")

    # Compress and save the image to the specified path
    image.save(
        compressed_image_path, format="JPEG", quality=70
    )  # Adjust the quality as per your requirements

    return compressed_image_path


def create_pdf(image_paths, output_path):
    pdf_canvas = canvas.Canvas(output_path, pagesize=letter)

    for image_path in image_paths:
        pdf_canvas.drawImage(image_path, 0, 0, width=letter[0], height=letter[1])

        # Add a new page
        pdf_canvas.showPage()

    pdf_canvas.save()


# Updated copy_files function with loading bar
def copy_files():
    progress = tk.DoubleVar()

    def perform_copy():
        source_folder = source_folder_entry.get()
        destination_folder = destination_folder_entry.get()
        excel_file = excel_file_entry.get()

        if source_folder == "" or destination_folder == "" or excel_file == "":
            messagebox.showerror(
                "Error", "Please provide all the required information."
            )
            return

        # Define the destination folder for compressed images
        compressed_images_folder = os.path.join(destination_folder, "compressed_images")
        os.makedirs(compressed_images_folder, exist_ok=True)

        missing_files = set()  # Store missing file names

        try:
            workbook = load_workbook(excel_file)
            sheet = workbook.active
            column = sheet["A"]

            # Create a set to store the filenames of compressed images
            compressed_filenames = set()
            # Create a list to store the paths of compressed images
            compressed_image_paths = []

            total_files = len(column)
            processed_files = 0

            # Create the loading bar
            loading_bar = ttk.Progressbar(
                window, length=500, mode="determinate", variable=progress
            )
            loading_bar.pack()

            for cell in column:
                if cell.value is not None:
                    filename = str(cell.value).strip()
                    source_path = os.path.join(source_folder, f"{filename}.jpg")

                    if os.path.exists(source_path):
                        # Check if the image has already been compressed
                        if filename in compressed_filenames:
                            log_text.insert(
                                tk.END, f"Image already compressed: {filename}.jpg\n"
                            )
                        else:
                            # Compress the image and save it to a file
                            compressed_image_path = compress_image(
                                source_path, compressed_images_folder
                            )
                            compressed_image_paths.append(compressed_image_path)
                            compressed_filenames.add(filename)

                            log_text.insert(
                                tk.END, f"Image compressed: {filename}.jpg\n"
                            )
                    else:
                        log_text.insert(
                            tk.END, f"File not found: {filename}.jpg\n", "failed"
                        )
                        missing_files.add(filename)

                    log_text.see(tk.END)  # Scroll to the end of the text
                    log_text.update_idletasks()  # Force an update of the GUI

                    processed_files += 1
                    progress_value = (processed_files / total_files) * 100
                    progress.set(progress_value)
                    loading_bar.update()

            # Generate the compressed PDF file
            current_date = datetime.date.today()
            formatted_date = current_date.strftime("%d-%m-%Y")
            output_pdf_path = os.path.join(
                destination_folder, f"Available_Stock_{formatted_date}.pdf"
            )
            create_pdf(compressed_image_paths, output_pdf_path)
            log_text.insert(
                tk.END, "PDF file generated: compressed_images.pdf\n", "success"
            )

            # Save missing file names to a text file
            missing_file_path = os.path.join(destination_folder, "missing_files.txt")
            with open(missing_file_path, "w") as f:
                for file_name in missing_files:
                    f.write(file_name + "\n")

            log_text.insert(
                tk.END, f"Missing file names saved to: {missing_file_path}\n", "success"
            )

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        messagebox.showinfo(
            "Success", "Image compression and PDF generation completed."
        )

    threading.Thread(target=perform_copy).start()


# Create the main window
window = tk.Tk()
window.title("File Copying Tool")
window.geometry("600x500")  # Set the window size

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

# Create and place the log text widget
log_text = tk.Text(window, height=15, width=70)
log_text.pack()
log_text.tag_configure(
    "success", foreground="dark green"
)  # Set the text color for success messages
log_text.tag_configure(
    "failed", foreground="red"
)  # Set the text color for failed messages

# Start the main loop
window.mainloop()
