input_paths = ['input/a_example.txt',
              'input/b_lovely_landscapes.txt',
              'input/c_memorable_moments.txt',
              'input/d_pet_pictures.txt',
                'input/e_shiny_selfies.txt']

from scoring import *
from simple_solutions import *
from hash_io import *

import os
import datetime

def save_result(input_file, slides, score=None):
    if score is None:
        score = calc_score(slides)
    writer = Output_writer(slides)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    name, ext = os.path.splitext(os.path.basename(input_file))
    output_file = timestamp + '-' + name + '-score{}'.format(score) + ext
    writer.write_result_file(output_file)
    print(output_file)


def run_on_all(solution_func):
    scores = [run_on_one(input_file=input_file, solution_func=solution_func) \
                for input_file in sorted(input_paths)]
    print(5*'=')
    print('Total score:', sum(scores))

def run_on_one(input_file, solution_func, all_horizontal=False):
    print(5*'-')
    print(input_file)
    if all_horizontal:
        images = Input_parser(input_file).all_horizontal_list()
    else:
        images = Input_parser(input_file).images

    print(len(images), 'images')
    slides = solution_func(images)
    print(len(slides), 'slides')
    score_ = calc_score(slides)
    print('score=', score_)
    save_result(input_file, slides, score=score_)
    return score_

