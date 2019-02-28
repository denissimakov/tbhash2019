#input_path = 'input/a_example.txt'
#input_path = 'input/a_example.txt'
#input_path = 'input/a_example.txt'
input_paths = ['input/e_shiny_selfies.txt',
              'input/b_lovely_landscapes.txt',
              'input/c_memorable_moments.txt',
              'input/d_pet_pictures.txt',
                'input/e_shiny_selfies.txt']


from scoring import *
from simple_solutions import *
from hash_io import Input_parser

ss = 0
for input_path in input_paths:
    images = Input_parser(input_path).images
    slides = dumb_solution(images)
    print(len(images), 'images')
    print(len(slides), 'slides')
    ss = ss + score(slides)
    # print('score=', score(slides))
    #list(all_pair_scores(slides))
print(ss)
