from hash_classes import *

def dumb_solutions(images):
    horiz_images = [im for im in images if im.orientation=='H']
    vert_images = [im for im in images if im.orientation=='V']
    slides_horiz = [Slide((im,)) for im in horiz_images]
    slides_vert = [Slide(vert_images[i:i+2]) for i in range(0,len(vert_images)-1,2)]
    slides = slides_horiz + slides_vert
    return slides
