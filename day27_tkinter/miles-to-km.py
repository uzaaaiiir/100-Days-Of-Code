from tkinter import *

FONT = ("Arial", 10, "normal")

def button_click():
    km = round((float(miles_entry.get()) * 1.60934),3)
    km_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Converter")
# window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

miles_entry = Entry(font=FONT)
# miles_entry.config(padx=10)
miles_entry.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to", font=FONT)
is_equal_to.config(padx=10)
is_equal_to.grid(column=0, row=1)

km_result_label = Label(text=0)
km_result_label.config(padx=10, pady=5)
km_result_label.grid(column=1,row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=button_click, font=FONT)
calculate_button.grid(column=1, row=2)

window.mainloop()