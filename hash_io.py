class Input_parser(object):

    def __init__(self, path):
        self.f = open(path, 'r')
        self.all_lines = self.f.readlines()
        self.header = self.all_lines.pop(0)


class Output_writer(object):

    def __init__(self, path):
        pass


if __name__ == '__main__':
    tmp = Input_parser('2019_practice/b_small.in')
    print('Header:')
    print(tmp.header)
    print('All lines:')
    for l in tmp.all_lines:
        print(l)