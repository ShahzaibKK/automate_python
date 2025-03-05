from pdf2image import convert_from_path
import cv2
import numpy as np
import os

# Paths
pdf_path = r"C:\Users\shahz\Downloads\QS\Gaoge GG Full Catalog.pdf"
output_folder = r"C:\Users\shahz\Downloads\QS\doneit"
poppler_path = (
    r"C:\poppler-24.08.0\Library\bin"  # Update this path to your Poppler installation
)

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Convert PDF to images
pages = convert_from_path(pdf_path, dpi=150, poppler_path=poppler_path)

for i, page in enumerate(pages):
    # Convert PIL image to grayscale numpy array
    img = np.array(page.convert("L"))

    # Preprocess: Thresholding to binarize the image
    _, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)

    # Close small gaps in edges
    kernel = np.ones((30, 30), np.uint8)
    dilated = cv2.dilate(thresh, kernel, iterations=1)

    # Find contours
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter and extract
    min_area = 8000  # Adjust based on DPI and expected image size
    for j, cnt in enumerate(contours):
        x, y, w, h = cv2.boundingRect(cnt)
        area = w * h
        if area > min_area:
            # Extract from original color image if needed
            cropped = np.array(page.convert("RGB"))[y : y + h, x : x + w, :]
            cv2.imwrite(
                f"{output_folder}/page_{i+1}_image_{j+1}.png",
                cv2.cvtColor(cropped, cv2.COLOR_RGB2BGR),
            )

print("All images separated and saved successfully!")
