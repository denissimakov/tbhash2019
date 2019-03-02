from scoring import *
from simple_solutions import *
from hash_io import Input_parser
import random
from simple_solutions import dumb_solution
from submission import run_on_all, run_on_one
from hash_classes import Image, Slide


def random_dumb_solution(images):
    images_new, rnd_state = shuffle_images(images)
    slides = dumb_solution(images_new)
    return slides

def shuffle_images(images):
    rnd_state = random.getstate()
    perm = list(range(len(images)))
    random.shuffle(perm)
    images_new = [images[index] for index in perm]
    return images_new, rnd_state


if __name__ == '__main__':
    input_paths = ['input/b_lovely_landscapes.txt',
                   'input/c_memorable_moments.txt',
                   'input/d_pet_pictures.txt',
                   'input/e_shiny_selfies.txt']

    for file in input_paths:
        for _ in range(100):
            try:
                run_on_one(file, random_dumb_solution)
            except:
                continue

