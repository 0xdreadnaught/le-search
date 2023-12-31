# Last Epoch Reroll Search Tool (le-search)

This tool uses PyTesseract to parse image snippets in order to identify reroll worthy unique item without having to leave the game.

[![Bandit](https://github.com/0xdreadnaught/le-search/actions/workflows/bandit.yml/badge.svg)](https://github.com/0xdreadnaught/le-search/actions/workflows/bandit.yml)

Tested With:
```
- Last Epoch 0.9.2f
- Windows 11
- Python 3.11.2
- Tesseract 5.3.1
```

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

## Example Snippet
### Good
![Good Example](https://github.com/0xdreadnaught/le-search/blob/main/goodsnippet.png)
### Bad
![Bad Example](https://github.com/0xdreadnaught/le-search/blob/main/badsnippet.png)

## Result
![Ressult](https://github.com/0xdreadnaught/le-search/blob/main/result.png)



## Known Issues
Items like `Isadora's Revenge` are sometimes misread. A new snippet usually fixes it.
