# Last Epoch Reroll Search Tool (le-search)

## Description

This tool uses PyTesseract to parse image snippets in order to identify reroll worthy unique item without having to leave the game.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/0xdreadnaught/le-search.git
   ```
2. Navigate to the project directory:
   ```bash
   cd le-search
   ```
3. Install the required Python packages:
   ```bash
   pip3 install -r requirements.txt
   ```
4. Install Tesseract: https://github.com/tesseract-ocr/tesseract
   
5. Ensure `tesseract` is in PATH.
   ```bash
   tesseract --version
   ```

## Usage
1. Run the script.
2. Take a screen snippet of the item name(ex: win+shift+s).
3. Press Ctrl+Shift+D to activate the tool.
4. A dialog box will appear showing the search result.

## Exmaple Snippet
### Good
![Good Example](https://github.com/0xdreadnaught/le-search/blob/main/goodsnippet.png)
### Bad
![Bad Example](https://github.com/0xdreadnaught/le-search/blob/main/badsnippet.png)

## Known Issues
The initial dialog is in the background. after that one is closed out, all future dialogs pop up over the game as intended.
