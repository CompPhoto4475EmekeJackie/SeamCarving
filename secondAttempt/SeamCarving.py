# import the necessary packages
from skimage import transform
from skimage import filters
from skimage import draw
import Tkinter as tk
from PIL import ImageTk, Image
import argparse
import cv2
import numpy as np

def main():
    global xSeams
    global ySeams
    global mag
    global root
    global panel
    global image
    global mag
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
        help="path to input image file")
    ap.add_argument("-d", "--direction", type=str,
        default="vertical", help="seam removal direction")
    args = vars(ap.parse_args())

    #Instantiate Haar Detection Classifiers
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    upperbody_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
    fullbody_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

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

    masked_img = image.copy()
    hl_color = np.array([0, 1, 0])

    #Compute object detection for faces on greyscale image
    faces = face_cascade.detectMultiScale(gray, 1.02, 5)

    # upperbodies = upperbody_cascade.detectMultiScale(gray, 1.2,5)
    # fullbodies = fullbody)cascade.detectMultiScale(gray, 1.2, 5)

    #Finds corners of faces and colors them in
    for (x,y,w,h) in faces:
        cv2.rectangle(masked_img,(x,y),(x+w,y+h),(255,0,0), 2)

        poly = [(y+h,x), (y+h,x+w), (y,x+w), (y, x)]

        pr = np.array([p[0] for p in poly])
        pc = np.array ([p[1] for p in poly])

        rr, cc = draw.polygon(pr,pc)

        masked_img[rr, cc, :] = masked_img[rr, cc, :]*0.5 + hl_color*.5

        # Sets the highlighted rectangles energy to be very high in
        # order to preserve area during seam carving.
        mag[rr,cc] +=1000

    # show the original image and masked image
    # cv2.imshow("Original", image)
    cv2.imshow("Original Image w/ Face Detection", masked_img)


    root.bind("<Left>", lambda event: updatePhoto(event, "x", "left"))
    root.bind("<Right>", lambda event: updatePhoto(event, "x", "right"))
    root.bind("<Down>", lambda event: updatePhoto(event, "y", "down"))
    root.bind("<Up>", lambda event: updatePhoto(event, "y", "up"))
    root.mainloop()


def updatePhoto(e, direction, arrow):
    global xSeams
    global ySeams
    global mag
    global root
    global panel   
    global image

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

if __name__ == '__main__':
    main()