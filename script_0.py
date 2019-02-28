#input_path = 'input/a_example.txt'
input_path = 'input/e_shiny_selfies.txt'

from scoring import *
from simple_solutions import *
from hash_io import *
images = Input_parser(input_path).images
slides = dumb_solution(images)
print(len(images), 'images')
print(len(slides), 'slides')
print('score=', score(slides))
#list(all_pair_scores(slides))

writer = Output_writer()
writer = Output_writer(slides)
writer.write_result_file('a_dumb.txt')


