from hash_classes import *

def dumb_solution(images):
    horiz_images = [im for im in images if im.orientation=='H']
    vert_images = [im for im in images if im.orientation=='V']
    slides_horiz = [Slide((im,)) for im in horiz_images]
    slides_vert = [Slide(vert_images[i:i+2]) for i in range(0,len(vert_images)-1,2)]
    slides = slides_horiz + slides_vert
    return slides

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
