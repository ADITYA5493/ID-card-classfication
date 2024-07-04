from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

# Example usage:
extracted_text = extract_text_from_image('Image2.png')
print(extracted_text)
