from tkinter import *

def button_clicked():
    print("Button was clicked!")
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height = 300)
window.config(padx=100, pady=200, bg='black') #Widget'in etrafına dolgu eklemek istiyorsam

#Label
my_label = Label(text="I am a label", font=("Arial",24,"bold"), bg='black', fg='white')
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Button
button = Button(text="Click me", command=button_clicked, bg='grey', fg='white')
button.grid(column=1, row=1)

new_button = Button(text="New Button", bg='grey', fg='white')
new_button.grid(column=2, row=0)

#Entry
input = Entry(width=10, bg='white', fg='black')
print(input.get())
input.grid(column=3, row=2)

#Grid ile pack birbirne uyumsuzdur.



window.mainloop() #Hep en sonda kalmalıdır
