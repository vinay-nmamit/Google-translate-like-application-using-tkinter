import tkinter as tk
from tkinter import ttk
from textblob import TextBlob

# color palette
PRIMARY_COLOR = "#3E5B7E"  # Blue
SECONDARY_COLOR = "#C70039"  # red
BG_COLOR = "#DAF7A6"  #
TEXT_COLOR = "#333333"  # Dark Gray

LANGUAGES = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Chinese': 'zh-CN',
    'Italian': 'it',
    'Japanese': 'ja',
    'Russian': 'ru'
}

def translate_text():
    text_to_translate = source_text.get("1.0", tk.END).strip()
    source_lang_code = LANGUAGES[source_lang.get()]
    dest_lang_code = LANGUAGES[destination_lang.get()]
    blob = TextBlob(text_to_translate)
    translated_text = blob.translate(from_lang=source_lang_code, to=dest_lang_code)
    destination_text.delete("1.0", tk.END)
    destination_text.insert(tk.END, translated_text)

# main application window
app = tk.Tk()
app.title("🌎 Google Translator")
app.geometry("800x300")
app.config(bg=BG_COLOR)

#custom fonts
title_font = ("Helvetica", 16, "bold")
label_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

# Language selection 
source_lang = tk.StringVar()
destination_lang = tk.StringVar()

source_lang_label = ttk.Label(app, text="Source Language:", font=label_font, foreground=TEXT_COLOR, background=BG_COLOR)
source_lang_label.grid(row=0, column=0, padx=10, pady=10)
source_lang_dropdown = ttk.Combobox(app, textvariable=source_lang, values=list(LANGUAGES.keys()), font=label_font)
source_lang_dropdown.grid(row=0, column=1, padx=10, pady=10)

destination_lang_label = ttk.Label(app, text="Destination Language:", font=label_font, foreground=TEXT_COLOR, background=BG_COLOR)
destination_lang_label.grid(row=0, column=2, padx=10, pady=10)
destination_lang_dropdown = ttk.Combobox(app, textvariable=destination_lang, values=list(LANGUAGES.keys()), font=label_font)
destination_lang_dropdown.grid(row=0, column=3, padx=10, pady=10)

# Set default values 
source_lang_dropdown.set('English')
destination_lang_dropdown.set('Spanish')

# Text input and output areas
source_text = tk.Text(app, wrap=tk.WORD, width=40, height=5, font=label_font)
source_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

destination_text = tk.Text(app, wrap=tk.WORD, width=40, height=5, font=label_font, foreground=SECONDARY_COLOR)
destination_text.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

# Translate button
translate_button = ttk.Button(app, text="Translate", command=translate_text, style="Custom.TButton")
translate_button.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Custom button style
app.style = ttk.Style()
app.style.configure("Custom.TButton", background=PRIMARY_COLOR, foreground="black", font=button_font)

# Adjust column weights for a responsive layout
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
app.grid_columnconfigure(3, weight=1)

app.mainloop()
