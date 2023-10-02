import keyboard
from PIL import ImageGrab
import pytesseract
import ctypes
import subprocess

def check_tesseract_installed():
    try:
        subprocess.run(["tesseract", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Tesseract not found. Please install it to proceed.")
        exit(1)

# Check if Tesseract is installed
check_tesseract_installed()

def get_clipboard_image():
    return ImageGrab.grabclipboard()

def ocr_image(image):
    return pytesseract.image_to_string(image)

def filter_capitalized_words(text):
    words = text.split()
    capitalized_words = [word for word in words if word.isupper()]

    # Remove single-letter words from the beginning
    while capitalized_words and len(capitalized_words[0]) == 1:
        capitalized_words.pop(0)

    return ' '.join(capitalized_words)

def show_dialog(text):
    print("RESULT:")
    print(text)
    ctypes.windll.user32.MessageBoxW(0, text, "OCR Result", 0)

def main():
    image = get_clipboard_image()
    if image is None:
        show_dialog("No image found on clipboard.")
        return

    text = ocr_image(image)

    if text:
        filtered_text = filter_capitalized_words(text)
        show_dialog(filtered_text)
    else:
        show_dialog("No text found.")

keyboard.add_hotkey('ctrl+shift+d', main)
keyboard.wait()
