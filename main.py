import tkinter.filedialog
from tkinter import *
from PIL import Image, ImageTk

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#ffffff"
BLACK = "#000000"
FONT_NAME = "Courier"

def upload_image():
    path = tkinter.filedialog.askopenfile(mode='r')
    print(path.name)
    image = Image.open(path.name)
    watermark = Image.open('images/imageWatermark.png')
    im = merge(image, watermark)
    im.show()

def merge(im1: Image.Image, im2: Image.Image):
    width, height = im1.size
    im2 = im2.resize((width, height))
    im2.putalpha(50)
    im = Image.new("RGBA", (width, height))
    im.paste(im1, (0, 0))
    im.paste(im2, (0, 0), im2.convert("RGBA"))
    return im
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Image Watermark")
window.config(pady=80, padx=100, bg=WHITE)

header = Label(window)
header.config(text="Image Watermark", fg=BLACK, bg=WHITE, font=(FONT_NAME, 24, "bold"))
header.grid(row=0, column=1)

subheader = Label(window)
subheader.config(text='select an image on which to apply a watermark', fg=BLACK, bg=WHITE, font=(FONT_NAME, 18, "bold"))
subheader.grid(row=1, column=1)

canvas = Canvas(width=200, height=230, bg=WHITE, borderwidth=0, highlightthickness=0)
start_button = Button(text="Upload", command=upload_image)
start_button.grid(row=2, column=1)

window.mainloop()