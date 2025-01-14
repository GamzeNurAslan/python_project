#Bu da uygulama tarzındaki hali
import pandas as pd
import tkinter as tk
from tkinter import messagebox

data = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

root = tk.Tk()
root.title("NATO Fonetik Alfabe Çevirici")
root.geometry("400x250")

def convert_to_phonetic():
    word = entry.get().upper()
    output_list = []

    if not word.isalpha():
        messagebox.showerror("Geçersiz Girdi", "Lütfen sadece harf girin.")
        return

    for letter in word:
        if letter in phonetic_dict:
            output_list.append(phonetic_dict[letter])

    output_label.config(text=" ".join(output_list))


instruction_label = tk.Label(root, text="Fonetik alfabe için bir kelime girin:")
instruction_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=20)
entry.pack(pady=10)

convert_button = tk.Button(root, text="Çevir", font=("Arial", 14), command=convert_to_phonetic)
convert_button.pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 14), fg="black")
output_label.pack(pady=10)

root.mainloop()
