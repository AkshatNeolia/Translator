
# Translator GUI Application

This project is a **simple translation tool** built using **Tkinter** for the graphical user interface (GUI) and **deep_translator** for translation functionality. The user can input text in one language, select the source and destination languages from a dropdown menu, and get the translated output.

## Features

- **User-friendly GUI**: Built using Tkinter with an intuitive interface for easy use.
- **Language Selection**: Dropdown menus for selecting both the source and destination languages.
- **Translation**: Translates input text between multiple languages using `deep_translator` (powered by Google Translate).
- **Error Handling**: Handles unsupported languages and translation errors gracefully.
- **Real-time Feedback**: Displays the translation or relevant error messages in the output box.

## Technologies Used

- **Python**: Core programming language.
- **Tkinter**: For building the GUI.
- **deep_translator**: For translation using Google Translate.

## Supported Languages

The following languages are currently supported:

- **English**
- **Spanish**
- **French**
- **German**
- **Catalan**

More languages can be added by expanding the dictionary in the code.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/AkshatNeolia/translator-gui.git
   ```

2. Install the required dependencies:
   ```bash
   pip install deep-translator
   ```

3. Run the application:
   ```bash
   python translator_gui.py
   ```

## How to Use

1. Select the **Source Language** from the first dropdown.
2. Select the **Destination Language** from the second dropdown.
3. Enter the text you want to translate in the input text box.
4. Click on the **Translate** button.
5. The translated text will appear in the output text box.
