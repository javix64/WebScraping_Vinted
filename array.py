class PC():

    def __init__(self, pa1, pa2, pa3):
        self.pes1 = pa1
        self.pes2 = pa2
        self.pes3 = pa3

    def __repr__(self):
       return str(self.__dict__)

arr = []
arr.append(PC('a', 'b', 'c'))
arr.append(PC('d', 'e', 'f'))
arr.append(PC('g', 'h', 'i'))
arr.append(PC('j', 'k', 'l'))
for ele in arr:
    print(ele)
