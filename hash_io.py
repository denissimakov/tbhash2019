class Input_parser(object):
    """ Reads file from path, creates header string and a list of all lines in file (excluding header)"""
    def __init__(self, path):
        self.f = open(path, 'r')
        self.all_lines = self.f.readlines()
        self.header = self.all_lines.pop(0)
        self.n_lines = len(self.all_lines)  # excluding header

class Output_writer(object):

    def __init__(self, path):
        pass


if __name__ == '__main__':
    tmp = Input_parser('2019_practice/d_big.in')
    print('Header:')
    print(tmp.header)
    print('All lines:')
    for l in tmp.all_lines:
        print(l)

