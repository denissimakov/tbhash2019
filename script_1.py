from scoring import calc_score
from simple_solutions import *
from hash_io import Input_parser

if __name__ == '__main__':
    input_paths = ['input/a_example.txt',
                   'input/b_lovely_landscapes.txt',
                   'input/c_memorable_moments.txt',
                   'input/d_pet_pictures.txt',
                   'input/e_shiny_selfies.txt']

    total_score = 0
    for input_path in input_paths:
        images = Input_parser(input_path).images
        slides = dumb_solution(images)
        total_score = total_score + calc_score(slides)
    print(total_score)




