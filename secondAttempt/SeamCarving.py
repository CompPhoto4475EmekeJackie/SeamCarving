# import the necessary packages
from skimage import transform
from skimage import filters
import Tkinter as tk
from PIL import ImageTk, Image
import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to input image file")
ap.add_argument("-d", "--direction", type=str,
    default="vertical", help="seam removal direction")
args = vars(ap.parse_args())

xSeams = 0
ySeams = 0

root = tk.Tk()

show_image = Image.open(args["image"])
display_image = ImageTk.PhotoImage(show_image)

image = cv2.cvtColor(np.array(show_image), cv2.COLOR_RGB2BGR)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

panel = tk.Label(root, compound="top", image = display_image, pady=10)

heightText = tk.StringVar()
heightLabel = tk.Label(text="Height:")
widthText = tk.StringVar()
widthLabel = tk.Label(text="Width:")
heightEntry = tk.Entry(root, textvariable=heightText)
widthEntry = tk.Entry(root, textvariable=widthText)
mitButton = tk.Button(root, height=1, width=5, text="Submit", command=updatePhoto)

panel.grid(row=0, columnspan=2, sticky="ew")
mag = filters.sobel(gray.astype("float"))


def updatePhoto(e, direction, arrow):
    global xSeams
    global ySeams
    vh = ""
    seam = 0
    if direction == "x":
        if arrow == "left":
            xSeams+=2
        if arrow == "right":
            xSeams-=2
        vh = "vertical"
        seam = xSeams

    if direction == "y":
        if arrow == "up":
            ySeams+=2
        if arrow == "down":
            ySeams-=2
        vh = "horizontal"
        seam = ySeams

    carved = transform.seam_carve(image, mag, vh, seam)
    b,g,r = cv2.split(carved * 255)
    carved_image = cv2.merge((r,g,b))
    display_image = Image.fromarray(carved_image.astype("uint8"))
    display_image_actual = ImageTk.PhotoImage(image=display_image)
    panel.config(image=display_image_actual)
    panel.image=display_image_actual


root.bind("<Left>", lambda event: updatePhoto(event, "x", "left"))
root.bind("<Right>", lambda event: updatePhoto(event, "x", "right"))
root.bind("<Down>", lambda event: updatePhoto(event, "y", "down"))
root.bind("<Up>", lambda event: updatePhoto(event, "y", "up"))
root.mainloop()
