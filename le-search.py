import keyboard
from PIL import ImageGrab
import pytesseract
import ctypes
import subprocess
import csv


def check_tesseract_installed():
    """
    Checks if Tesseract is installed on the system.
    """
    try:
        subprocess.run(
            ["tesseract", "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Tesseract not found. Please install it to proceed.")
        exit(1)


def get_clipboard_image():
    """
    Grabs the image from the clipboard.
    """
    return ImageGrab.grabclipboard()


def ocr_image(image):
    """
    Performs OCR on the given image.
    """
    return pytesseract.image_to_string(image)


def filter_capitalized_words(text):
    """
    Filters out capitalized words from the given text.
    """
    words = text.split()
    capitalized_words = [word for word in words if word.isupper()]

    # Remove single-letter words from the beginning
    while capitalized_words and len(capitalized_words[0]) == 1:
        capitalized_words.pop(0)
    return " ".join(capitalized_words)


def get_reroll_chance(item_name):
    """
    Retrieves the reroll chance for the given item name from the database.
    """
    with open("items.db", mode="r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0].upper() == item_name.upper():
                return row[1]
    return None


def show_dialog(text):
    """
    Displays a dialog box with the given text.
    """
    ctypes.windll.user32.MessageBoxW(0, text, "LE Search Result", 0x1000)


def main():
    """
    Main function to execute the OCR and display the result.
    """
    image = get_clipboard_image()
    if image is None:
        show_dialog("No image found on clipboard.")
        return
    text = ocr_image(image)

    if text:
        filtered_text = filter_capitalized_words(text)
        reroll_chance = get_reroll_chance(filtered_text)

        if reroll_chance is not None:
            if reroll_chance == "0% (Common)":
                reroll_text = "Nothing special"
            elif reroll_chance == "–":
                reroll_text = "No weight assigned"
            else:
                reroll_text = f"Reroll Chance: {reroll_chance}"
            show_dialog(f"{filtered_text}\n{reroll_text}")
        else:
            show_dialog(f"{filtered_text}\nItem not found in database.")
    else:
        show_dialog("No text found.")


# Check if Tesseract is installed
check_tesseract_installed()

keyboard.add_hotkey("ctrl+shift+d", main)
keyboard.wait()
