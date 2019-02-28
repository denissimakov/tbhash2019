#input_path = 'input/a_example.txt'
input_path = 'input/b_lovely_landscapes.txt'

from scoring import *
from simple_solutions import *
from hash_io import *

def greedy_solution(images):
    slides = [Slide((im,)) for im in images]
    solution = [slides.pop(0)]
    aaa = 0;
    while len(slides) > 0:
        max_score = 0
        best = None
        side = None
        ind_best = 0
        pos_right = len(solution[-1].tags)/2;
        pos_left = len(solution[0].tags)/2;
        for idx, s in enumerate(slides):
            
            
            sr = score( [solution[-1],s])
            if sr > max_score:
                best = s
                ind_best = idx
                side = 'r'
                max_score = sr
                if max_score > 0:
                    break
            sl = score([s, solution[0]])
            if  sl > max_score:
                best = s
                side = 'l'               
                ind_best = idx
                max_score = sl
                if max_score > 0:
                    break
             
        if best is None:
            solution += [slides.pop(0)]
        else:
            if side == 'l':
                solution = ([best] + solution)
            else:
                solution = ( solution + [best])
            slides.pop(ind_best)
        aaa += max_score    
        print(len(slides),' ',aaa)
    return solution
        









images = Input_parser(input_path).images

print(len(images), 'images')
#list(all_pair_scores(slides))
slides = greedy_solution(images)
print(len(slides), 'slides')
print('score=', score(slides))

# writer = Output_writer(slides)
# writer.write_result_file('a_dumb.txt')


