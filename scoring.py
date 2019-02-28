from hash_classes import *

def pair_score(slide0, slide1):
    tags0 = slide0.tags
    tags1 = slide1.tags
    return min(min(len(tags0-tags1),len(tags1-tags0)), len(tags0&tags1))

def all_pair_scores(slides):
    return (pair_score(slides[i],slides[i+1]) for i in range(len(slides)-1))

def score(slides):
    return sum(all_pair_scores(slides))
