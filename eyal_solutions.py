from hash_classes import *
from scoring import calc_pair_score

def greedy_solution(images):
    images = list(reversed(images))
    next_img = images.pop()
    result = [next_img]

    while images:
        img_last = result[-1]
        img_first = result[0]
        max_s = 0
        max_i = -1
        last = True
        for i, pair in enumerate(images):
            score_first = calc_pair_score(img_first, pair)
            score_last = calc_pair_score(img_last, pair)
            if score_first>= score_last and score_first>max_s:
                last = False
                max_s = score_first
                max_i = i
            elif score_last>= score_first and score_last>max_s:
                last = True
                max_s = score_last
                max_i = i
        if last:
            result.append(images.pop(max_i))
        else:
            result.insert(0, images.pop(max_i))
    slides = [Slide((res,)) for res in result]

    return slides
