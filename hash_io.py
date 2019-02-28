from hash_classes import Image

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

class Output_writer(object):
    """ gets list of slides and writes txt file"""
    def __init__(self, slides):
        self.slides = slides

    def write_result_file(self, path):
        img_id_list = []
        for slide in self.slides:
            img_id_list.append([str(img.id) for img in slide.images])
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
