import random
import string
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("600x400") 

        self.background_image = Image.open("background.jpeg")
        self.background_image = self.background_image.resize((600, 400), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        
        self.length_label = tk.Label(root, text="Password Length:", bg="#ffffff", fg="#000000")
        self.length_label_window = self.canvas.create_window(50, 50, anchor="nw", window=self.length_label)
        self.length_entry = tk.Entry(root)
        self.length_entry_window = self.canvas.create_window(200, 50, anchor="nw", window=self.length_entry)

        self.include_letters_var = tk.BooleanVar()
        self.include_letters_check = tk.Checkbutton(root, text="Include Letters", variable=self.include_letters_var, bg="#ffffff")
        self.include_letters_check_window = self.canvas.create_window(50, 100, anchor="nw", window=self.include_letters_check)

        self.include_digits_var = tk.BooleanVar()
        self.include_digits_check = tk.Checkbutton(root, text="Include Digits", variable=self.include_digits_var, bg="#ffffff")
        self.include_digits_check_window = self.canvas.create_window(50, 150, anchor="nw", window=self.include_digits_check)

        self.include_symbols_var = tk.BooleanVar()
        self.include_symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=self.include_symbols_var, bg="#ffffff")
        self.include_symbols_check_window = self.canvas.create_window(50, 200, anchor="nw", window=self.include_symbols_check)

        self.exclude_chars_label = tk.Label(root, text="Exclude Characters:", bg="#ffffff", fg="#000000")
        self.exclude_chars_label_window = self.canvas.create_window(50, 250, anchor="nw", window=self.exclude_chars_label)

        self.exclude_chars_entry = tk.Entry(root)
        self.exclude_chars_entry_window = self.canvas.create_window(200, 250, anchor="nw", window=self.exclude_chars_entry)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button_window = self.canvas.create_window(50, 300, anchor="nw", window=self.generate_button)

        self.password_label = tk.Label(root, text="", bg="#ffffff", fg="#000000")
        self.password_label_window = self.canvas.create_window(50, 350, anchor="nw", window=self.password_label)

        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button_window = self.canvas.create_window(200, 300, anchor="nw", window=self.copy_button)

    def generate_password(self):
        try:
            length = self.validate_length(self.length_entry.get())
            include_letters = self.include_letters_var.get()
            include_digits = self.include_digits_var.get()
            include_symbols = self.include_symbols_var.get()
            exclude_chars = self.exclude_chars_entry.get()

            if not (include_letters or include_digits or include_symbols):
                raise ValueError("Select at least one character type.")

            character_pool = ""
            if include_letters:
                character_pool += letters
            if include_digits:
                character_pool += digits
            if include_symbols:
                character_pool += symbols

            if exclude_chars:
                character_pool = ''.join(c for c in character_pool if c not in exclude_chars)

            if not character_pool:
                raise ValueError("Character pool is empty. Adjust your criteria.")

            password = ''.join(random.choice(character_pool) for i in range(length))
            self.password_label.config(text=password)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def validate_length(self, length_str):
        if len(length_str) == 0:
            return 10
        elif not length_str.isdigit():
            raise ValueError("Password length must be a valid number.")
        length = int(length_str)
        if length <= 0:
            raise ValueError("Password length must be a positive number.")
        return length

    def copy_to_clipboard(self):
        password = self.password_label.cget("text")
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
