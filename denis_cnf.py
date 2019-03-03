#input_path = 'input/a_example.txt'
input_path = 'input/b_lovely_landscapes.txt'

from hash_io import *

images = Input_parser(input_path).images
print(input_path)
print(len(images), 'images')

from simple_solutions import *
slides = dumb_solution(images)
print(len(slides), 'slides')

from scoring import *
print('dumb score=', calc_score(slides))

def find_best_pair(slide_chains):
    """slide_chains: list of lists of chains"""
    n_chains = len(slide_chains)
    n_chains = 5000
    print('calculating {} scores'.format(n_chains*n_chains))
    best_pair = None
    best_score = 0
    for ind_0 in range(n_chains):
        for ind_1 in range(n_chains):
            score = calc_pair_score(slide_chains[ind_0][-1], slide_chains[ind_1][0])
            if score > best_score:
                best_score = score
                best_pair = (ind_0, ind_1)
    return best_pair

def init_slide_chains(slides):
    """Return trivial slide chains"""
    return [(s,) for s in slides]

slide_chains = init_slide_chains(slides)
print(slide_chains)

best_pair = find_best_pair(slide_chains)
print(best_pair)

#writer = Output_writer(slides)
#writer.write_result_file('a_dumb.txt')


