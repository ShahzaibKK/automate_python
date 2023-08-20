import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import datetime


def update_stock_from_sales(stock_file_path, sales_file_path):
    try:
        # Read the stock report
        stock_data = pd.read_excel(stock_file_path, header=None)

        # Create a dictionary with article names as keys and their corresponding quantities as values
        stock_dict = dict(zip(stock_data[0], stock_data[1]))

        # Read the sales report
        sales_data = pd.read_excel(sales_file_path, header=None)

        # Process the sales report and update the stock quantities
        for index, row in sales_data.iterrows():
            article_name = row[0]
            quantity_sold = row[1]

            if article_name in stock_dict:
                current_stock = stock_dict[article_name]
                if quantity_sold <= current_stock:
                    updated_stock = max(current_stock - quantity_sold, 0)
                    stock_dict[article_name] = updated_stock
                else:
                    messagebox.showwarning(
                        "Warning",
                        f"Sale quantity of {quantity_sold} exceeds remaining stock quantity of {current_stock} for article {article_name}. The stock will not be updated.",
                    )
                    return

        # Create a new DataFrame for the updated stock report
        updated_stock_data = pd.DataFrame(
            list(stock_dict.items()), columns=["Article", "Updated Quantity"]
        )

        # Save the updated stock report to a new Excel file
        updated_stock_file_path = (
            f"updated_stock_report_{datetime.date.today().strftime('%d-%m-%Y')}.xlsx"
        )
        updated_stock_data.to_excel(updated_stock_file_path, index=False)

        messagebox.showinfo("Success", "Stock quantities updated successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def browse_stock_file():
    stock_file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if stock_file_path:
        stock_file_entry.delete(0, tk.END)
        stock_file_entry.insert(0, stock_file_path)


def browse_sales_file():
    sales_file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if sales_file_path:
        sales_file_entry.delete(0, tk.END)
        sales_file_entry.insert(0, sales_file_path)


# Create the GUI
root = tk.Tk()
root.title("Stock Update from Sales")
root.geometry("400x400")

stock_file_label = tk.Label(root, text="Select Stock Report:")
stock_file_label.pack(pady=5)

stock_file_entry = tk.Entry(root, width=40)
stock_file_entry.pack(pady=5)

browse_stock_button = tk.Button(root, text="Browse", command=browse_stock_file)
browse_stock_button.pack(pady=5)

sales_file_label = tk.Label(root, text="Select Sales Report:")
sales_file_label.pack(pady=5)

sales_file_entry = tk.Entry(root, width=40)
sales_file_entry.pack(pady=5)

browse_sales_button = tk.Button(root, text="Browse", command=browse_sales_file)
browse_sales_button.pack(pady=5)

update_button = tk.Button(
    root,
    text="Process",
    command=lambda: update_stock_from_sales(
        stock_file_entry.get(), sales_file_entry.get()
    ),
)
update_button.pack(pady=10)

root.mainloop()
