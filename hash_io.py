from hash_classes import Image
import os

class Input_parser(object):
    """ Reads file from path, creates header string and a list of all lines in file (excluding header)"""
    def __init__(self, path):
        self.f = open(path, 'r')
        self.all_lines = self.f.readlines()
        self.header = self.all_lines.pop(0)
        self.n_lines = len(self.all_lines)  # excluding header
        self.N = int(self.header)
        self.create_image_list()

    def create_image_list(self):
        self.images = []
        for i,l in enumerate(self.all_lines):
            line = l.split()
            self.images.append(Image(id=i, orientation=line[0], tags=set(line[2:])))
        return self

    def all_horizontal_list(self):
        only_vertical = [img for img in self.images if img.orientation == 'V']
        only_vertical.sort(key=lambda x: x.M)
        only_horizontal = [img for img in self.images if img.orientation == 'H']

        while len(only_vertical)>=2:
            img = only_vertical.pop()
            max_M = 0
            max_j = -1
            for j, pair_img in enumerate(only_vertical):
                union_set = pair_img.tags | img.tags
                if len(union_set) > max_M:
                    max_M = len(union_set)
                    max_j = j
            pair = only_vertical.pop(max_j)
            new_img = Image(id=(img.id,pair.id), orientation='H', tags = pair.tags | img.tags)
            only_horizontal.append(new_img)

        only_horizontal.sort(key=lambda x: x.M, reverse=True)

        # #test:
        # uniques =
        return only_horizontal

class Output_writer(object):
    """ gets list of slides and writes txt file"""
    def __init__(self, slides):
        self.slides = slides

    def write_result_file(self, path):
        path = os.path.join('results_files', path)
        img_id_list = []
        for slide in self.slides:
            if len(slide.images) == 1 and isinstance(slide.images[0].id,tuple):
                # vertical pairing mode
                ids = [slide.images[0].id[0], slide.images[0].id[0]]
                img_id_list.append(ids)
            else:

                img_id_list.append([str(img.id) for img in slide.images])

        flat_list = [item for sublist in img_id_list for item in sublist]
        assert len(flat_list) == len(set(flat_list)), 'IDs are not all unique!'

        S = len(img_id_list)
        with open(path,'w') as f:
            f.write(str(S))
            f.write('\n')
            for slide in img_id_list:
                f.write(' '.join(slide)+'\n')





if __name__ == '__main__':
    # example
    tmp = Input_parser('input/a_example.txt')
    # tmp.create_image_list()
    for im in tmp.images:
        print(im.id,im.orientation,im.M,im.tags)
    # print('Header:')
    # print(tmp.header)
    # print('All lines:')
    # for l in tmp.all_lines:
    #     print(l)
