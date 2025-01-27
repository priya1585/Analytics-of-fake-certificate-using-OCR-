import cv2
import pytesseract
from pytesseract import Output

# Set the path to Tesseract OCR executable
# For Windows users: Update the path as needed
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract text from the image
def extract_text(image_path):
    try:
        # Load the image
        image = cv2.imread(image_path)

        # Preprocess the image
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)  # Thresholding

        # Use OCR to extract text
        extracted_text = pytesseract.image_to_string(binary, lang='eng')
        return extracted_text

    except Exception as e:
        return f"Error: {str(e)}"

# Function to analyze text for authenticity
def analyze_text(text, valid_keywords):
    for keyword in valid_keywords:
        if keyword.lower() not in text.lower():
            return f"Potential fake certificate: Missing keyword '{keyword}'"
    return "Certificate appears authentic"

# Main function
if __name__ == "__main__":
    # Path to the certificate image
    image_path = "certificate_sample.jpg"  # Replace with your image path

    # Keywords to validate certificate authenticity
    valid_keywords = ["University", "Name", "Date", "Certificate"]

    # Extract and analyze text
    text = extract_text(image_path)
    print("Extracted Text:\n", text)

    # Validate certificate
    result = analyze_text(text, valid_keywords)
    print("\nAnalysis Result:", result)
