from hash_io import *
from hash_classes import *
import os

f = 'b_lovely_landscapes.txt'
f = 'c_memorable_moments.txt'

f = os.path.join('input',f)
input_loader = Input_parser(f)
image_list = input_loader.images

only_horizontal = input_loader.all_horizontal_list()
# only_vertical = [img for img in image_list if img.orientation == 'V']
# only_horizontal = [img for img in image_list if img.orientation == 'H']
#
# only_vertical.sort(key=lambda x: x.M)
#
# while len(only_vertical)>=2:
#     img = only_vertical.pop()
#     max_M = 0
#     max_j = -1
#     for j, pair_img in enumerate(only_vertical):
#         union_set = pair_img.tags | img.tags
#         if len(union_set) > max_M:
#             max_M = len(union_set)
#             max_j = j
#     pair = only_vertical.pop(max_j)
#     new_img = Image(id=(img.id,pair.id), orientation='H', tags = pair.tags | img.tags)
#     only_horizontal.append(new_img)

for im in image_list:
    print(im.id, im.orientation, im.M, im.tags)

# for im in only_vertical:
#     print(im.id, im.orientation, im.M, im.tags)
for im in only_horizontal:
    print(im.id, im.orientation, im.M, im.tags)
