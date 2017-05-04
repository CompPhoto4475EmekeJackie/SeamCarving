# # Controls the window for seam carving

# #
# import sys
# import Tkinter as tk
# from PIL import ImageTk, Image
# from seam_carving import SeamCarver

# def main(argv):
#     window = tk.Tk()
#     window.title("Seam Carving Example")

#     #Creates Image from Path
#     # path = "static/dolphin.jpeg"

#     # Creates Image from Path specified by input commands
#     img = ImageTk.PhotoImage(Image.open(argv[1]))
#     self.sc = SeamCarver(Image.open(argv[1]))

#     #Get dimensions for window
#     dimensions = "image size: %dx%d" % (img.width(), img.height())

#     label = tk.Label(window, compound="top", image=img, text=dimensions)
#     label.pack()
#     #
#     # # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
#     # panel = tk.Label(window, image=img)

#     window.configure(background='grey')
#     window.mainloop()

#     pass

# if __name__ == "__main__":
#     main(sys.argv)

# Controls the window for seam carving


# import sys
# import Tkinter as tk
# from PIL import ImageTk, Image
# from seam_carving import SeamCarver

# def resize(event):
#     global sc
#     global label
#     img2 = sc.resize(200,300)
#     dimensions = "image size: %dx%d" % (sc.image.width, sc.image.height)
#     label.configure(image = img2, text=dimensions)
#     label.image = img2
#     label.text = dimensions
#     label.pack()

# def main(argv):
#     window = tk.Tk()
#     window.title("Seam Carving Example")


#     #Creates Image from Path
#     # path = "static/dolphin.jpeg"

#     # Creates Image from Path specified by input commands
#     img = ImageTk.PhotoImage(Image.open(argv[1]))
#     global sc
#     global label
#     sc = SeamCarver(argv[1])

#     #Get dimensions for window
#     dimensions = "image size: %dx%d" % (sc.image.width, sc.image.height)

#     label = tk.Label(window, compound="top", image=img, text=dimensions)
#     label.pack()
#     #
#     # # The Label widget is a standard Tkinter widget used to display a text or image on the screen.
#     # panel = tk.Label(window, image=img)

#     window.configure(background='grey')
#     window.resizable(width=True, height=False)
#     window.bind('<ButtonRelease-1>', resize)
#     window.mainloop()

#     pass
import sys
import Tkinter as tk
from PIL import ImageTk, Image
from seam_carving import SeamCarver

def main(argv):
    global word
    global img
    global img2
    global panel
    global sc
    global heightText
    global widthText

    root = tk.Tk()

    img = ImageTk.PhotoImage(Image.open(argv[1]))
    img2 = ImageTk.PhotoImage(Image.open(argv[2]))

    sc = SeamCarver(argv[1])

    panel = tk.Label(root, compound="top", image = img, text="hey")
    panel.pack()
    # heightText = tk.StringVar()
    # widthText = tk.StringVar()
    # heightEntry = tk.Entry(root, textvariable=heightText)
    # # heightText.place(x=50, y=50)
    # # heightText.pack("bottom")
    # widthEntry = tk.Entry(root, textvariable=heightText)
    # # widthText.place(x=100, y=50)
    # # widthText.pack("bottom")
    # submit = tk.Button(root, height=1, width=5, text="Submit", command=lambda: updatePhoto())
    word=True
    # panel.pack(side = "bottom", fill = "both", expand = "yes")


    root.bind("<Return>", callback)
    root.mainloop()

# def updatePhoto(e):
#     global panel
#     global sc
#     image = sc.resize(widthText.get(1.0,END)[:-1], heightTextget(1.0,END)[:-1])
#     panel.configure(image=image)
#     panel.image = image

def callback(e):
    global word
    # global img
    global panel
    global sc
    image_shown = img
    if (word):
        text="hey"
        image_shown = img
        word = False
    else:
        text="bye"
        image_shown = img2
        word = True
    panel.configure(text=text, image=image_shown)
    panel.text = text
    panel.image = image_shown


# if __name__ == "__main__":
#     main()

if __name__ == "__main__":
    main(sys.argv)





