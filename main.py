from tkinter import *
from screenshot import take_screenshot

root = Tk()
root.title("Simpel Screenshot")
root.geometry('275x200')

window_icon = PhotoImage(file="./window_icon.png")
root.iconphoto(False, window_icon)

text_font = "Consolas"

welcome_lbl = Label(
    root,
    text="Simpel Screenshot App",
    # rg="black"
    font=text_font
).place(x=45, y=5)

screenshot_button = Button(
    root,
    command=lambda:take_screenshot(root),
    text="Take Screenshot",
    bg="black",
    fg="white",
    font=text_font
).place(x=50, y=100)

root.mainloop()
