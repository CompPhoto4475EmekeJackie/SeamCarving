from seam_carving import SeamCarver


IMAGE_FILE = 'static/jack1.jpg'


def scale_down_example():
    sc = SeamCarver(IMAGE_FILE)
    image = sc.resize(450, 390)
    image.save("static/jack1TestWithFaceRec.jpg")
    sc.debug_animation.export_gif("static/jack1TestWithFaceRec.gif")


# def scale_up_example():
#     sc = SeamCarver(IMAGE_FILE)
#     image = sc.resize(500, 500)
#     image.save("static/biggerpeople.jpg")
#     sc.debug_animation.export_gif("static/biggerpeople.gif")


if __name__ == '__main__':
    scale_down_example()
    # scale_up_example()