#input_path = 'input/a_example.txt'
input_path = 'input/b_lovely_landscapes.txt'

from scoring import *
from hash_io import *

images = Input_parser(input_path).images
print(input_path)
print(len(images), 'images')

slides = dumb_solution(images)
print(len(slides), 'slides')

print('dumb score=', score(slides))

def find_best_pair(slide_chains):
    """slide_chains: list of lists of chains"""
    

#writer = Output_writer(slides)
#writer.write_result_file('a_dumb.txt')


