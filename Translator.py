import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException, TranslationNotFound

# Dictionary to map full language names to language codes
language_codes = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Catalan": "ca"
}

# Function to handle translation
def translate_text():
    try:
        sentence = input_text.get("1.0", "end-1c")  # Get text from input
        src_lang = src_lang_var.get()
        dest_lang = dest_lang_var.get()

        if not sentence.strip():  # Check if input is empty
            output_text.delete("1.0", "end")
            output_text.insert("end", "Please enter some text to translate.")
            return

        # Map full language names to codes
        src_lang_code = language_codes[src_lang]
        dest_lang_code = language_codes[dest_lang]

        # Attempt translation
        translated_sentence = GoogleTranslator(source=src_lang_code, target=dest_lang_code).translate(sentence)
        output_text.delete("1.0", "end")  # Clear output text box
        output_text.insert("end", translated_sentence)

    except LanguageNotSupportedException as lang_error:
        output_text.delete("1.0", "end")
        output_text.insert("end", f"Error: Language not supported ({lang_error})")
    except TranslationNotFound as trans_error:
        output_text.delete("1.0", "end")
        output_text.insert("end", f"Error: Translation not found ({trans_error})")
    except Exception as general_error:
        output_text.delete("1.0", "end")
        output_text.insert("end", f"Error: {general_error}")

# GUI setup
root = tk.Tk()
root.title("Translator")
root.geometry("600x500")
root.configure(bg="white")

# Heading with larger font size and adjusted position
heading = tk.Label(root, text="Translator", font=("Arial", 32, "bold"), bg="white", fg="black")  # Increased font size to 32
heading.pack(pady=30)  # Increased pady to bring the heading down

# Language selection frame
frame = tk.Frame(root, bg="white")
frame.pack(pady=20)

# Language selection
src_lang_var = tk.StringVar(value='English')  # Default to English
dest_lang_var = tk.StringVar(value='Catalan')  # Default to Catalan

src_label = tk.Label(frame, text="Source Language:", bg="white")
src_label.grid(row=0, column=0, padx=5)
src_lang_menu = ttk.Combobox(frame, textvariable=src_lang_var, values=list(language_codes.keys()), width=15)
src_lang_menu.grid(row=0, column=1, padx=5)

dest_label = tk.Label(frame, text="Destination Language:", bg="white")
dest_label.grid(row=0, column=2, padx=5)
dest_lang_menu = ttk.Combobox(frame, textvariable=dest_lang_var, values=list(language_codes.keys()), width=15)
dest_lang_menu.grid(row=0, column=3, padx=5)

# Creating Input Textbox
input_label = tk.Label(root, text="Enter text to translate:", bg="white")
input_label.pack(pady=5)
input_text = tk.Text(root, height=7, width=50, borderwidth=2, relief="solid", font=("Arial", 12))
input_text.pack(pady=5)

# Creating Translate Button
translate_button = tk.Button(root, text="Translate", command=translate_text, font=("Arial", 12))
translate_button.pack(pady=10)

# Creating Output Textbox
output_label = tk.Label(root, text="Translated text:", bg="white")
output_label.pack(pady=5)
output_text = tk.Text(root, height=7, width=50, borderwidth=2, relief="solid", font=("Arial", 12))
output_text.pack(pady=5)

root.mainloop()
