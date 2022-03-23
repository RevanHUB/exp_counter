from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    28.0, -86.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()
