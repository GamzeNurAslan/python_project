from tkinter import *
from tkinter import ttk

def miles_to_km():
    try:
        miles = float(miles_input.get())
        km = miles * 1.609
        kilometer_result_label.config(text=f"{km:.2f}")
    except ValueError:
        kilometer_result_label.config(text="Invalid input")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=30, pady=30, bg='#2e3b4e')


font_style = ("Helvetica", 14)
label_font = ("Helvetica", 12, "bold")
button_font = ("Helvetica", 12)

miles_input = Entry(window, font=font_style, width=15, bd=5, relief=SUNKEN)
miles_input.grid(column=1, row=0, padx=10, pady=10)

miles_label = Label(window, text="Miles", font=label_font, fg="white", bg='#2e3b4e')
miles_label.grid(column=2, row=0, padx=10, pady=10)

is_equal_label = Label(window, text="is equal to", font=label_font, fg="white", bg='#2e3b4e')
is_equal_label.grid(column=0, row=1, padx=10, pady=10)

kilometer_result_label = Label(window, text="0", font=("Helvetica", 18, "bold"), fg="white", bg='#2e3b4e')
kilometer_result_label.grid(column=1, row=1, padx=10, pady=10)

kilometer_label = Label(window, text="Km", font=label_font, fg="white", bg='#2e3b4e')
kilometer_label.grid(column=2, row=1, padx=10, pady=10)

calculate_button = Button(window, text="Calculate", font=button_font, command=miles_to_km, bg='#4CAF50', fg='white', bd=0, relief=RAISED)
calculate_button.grid(column=1, row=2, pady=20)

window.mainloop()
