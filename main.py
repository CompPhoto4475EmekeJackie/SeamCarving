# Controls the window for seam carving

#
import sys
import Tkinter as tk
from PIL import ImageTk, Image
from seam_carving import SeamCarver

def main(argv):
    window = tk.Tk()
    window.title("Seam Carving Example")

    #Creates Image from Path
    # path = "static/dolphin.jpeg"

    # Creates Image from Path specified by input commands
    img = ImageTk.PhotoImage(Image.open(argv[1]))

    #Get dimensions for window
    dimensions = "image size: %dx%d" % (img.width(), img.height())

    label = tk.Label(window, compound="top", image=img, text=dimensions)
    label.pack()
    #
    # # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
    # panel = tk.Label(window, image=img)

    window.configure(background='grey')
    window.mainloop()

    pass

if __name__ == "__main__":
    main(sys.argv)


