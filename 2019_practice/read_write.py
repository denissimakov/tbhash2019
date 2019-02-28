"""Read and write files"""

class Problem:
    
    def __init__(self):
        pass

    def read(self, fpath):
        with f is open(fpath):
            first = f.readline()
            R,C,L,H = map(int, first.split())
            pizza = R*['']
            for row in range(R):
                row_str = f.readline()
                pizza[row] = row_str
            self.L = L
            self.H = H
            self.pizza = pizza
