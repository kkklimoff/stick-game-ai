import time

class Node(object):
    def __init__(self, sticks, level):
        self.sticks = sticks
        self.level = level
        self.children = []
        self.addchildren()

    def addchildren(self):
        if self.sticks == 0:
            return
        elif self.sticks == 1:
            self.children.append(Node(self.sticks - 1, self.switchlevel()))
        elif self.sticks == 2:
            self.children.append(Node(self.sticks - 1, self.switchlevel()))
            self.children.append(Node(self.sticks - 2, self.switchlevel()))
        else:
            self.children.append(Node(self.sticks - 1, self.switchlevel()))
            self.children.append(Node(self.sticks - 2, self.switchlevel()))
            self.children.append(Node(self.sticks - 3, self.switchlevel()))


    def switchlevel(self):
        if self.level == 'MAX':
            return 'MIN'
        else:
            return 'MAX'

    def __str__(self, nlevel=0):
        ret = '\t'*nlevel+repr(self.sticks)+'\n'
        for child in self.children:
            ret += child.__str__(nlevel+1)
        return ret


def main():
    n = Node(21, 'MAX')
    print(n)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print(time.time()-start_time)