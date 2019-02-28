class Input_parser(object):
    """ Reads file from path, creates header string and a list of all lines in file (excluding header)"""
    def __init__(self, path):
        self.f = open(path, 'r')
        self.all_lines = self.f.readlines()
        self.header = self.all_lines.pop(0)
        self.n_lines = len(self.all_lines)  # excluding header
        self.N = int(self.header)
    def create_image_list(self):
        self.images = []
        for l in self.all_lines:
            line = l.split()
            self.images.append(Image(id=line[0], orientation=line[1], M=line[2], tags=set(line[3:])))

class Output_writer(object):

    def __init__(self, path):
        pass


if __name__ == '__main__':
    tmp = Input_parser('input/a_example.txt')
    print('Header:')
    print(tmp.header)
    print('All lines:')
    for l in tmp.all_lines:
        print(l)

