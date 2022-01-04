import tkinter 

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
my_label.grid(column=0, row=0)
my_label.config(padx=10,pady=10)

# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Entry 
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

button2 = tkinter.Button(text="New Button", command=button_clicked)
button2.grid(column=2, row=0)

window.mainloop()