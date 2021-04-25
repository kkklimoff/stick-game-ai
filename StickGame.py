import time
from operator import attrgetter
from tkinter import *


class setupScreen:
    def __init__(self, master):
        self.master = master
        self.setupLablel = Label(self.master, text='Who starts the game?').grid(row=0,column=1)
        self.cpuButton = Button(self.master,text='CPU',padx=10,command=lambda: self.playgame('CPU')).grid(row=1,column=0)
        self.playerButton = Button(self.master,text='PLAYER',padx=10,command=lambda: self.playgame('ME')).grid(row=1,column=2)
    def playgame(self,fp):
        self.master.destroy()
        self.master = Tk()
        self.app = gameScreen(self.master,fp)
        self.master.mainloop()
    

class gameScreen:
    def __init__(self,master,fp):
        self.master = master
        self.nSticks = 21
        self.gameState = Label(self.master, text=('| '*21))
        self.stickState = Label(self.master, text=21)
        self.infoState = Label(self.master, text='')
        self.oneStBut = Button(self.master, text='1', command=lambda: self.maketurn(1))
        self.twoStBut = Button(self.master, text='2', command=lambda: self.maketurn(2))
        self.threeStBut = Button(self.master, text='3', command=lambda: self.maketurn(3))

        self.gameState.grid(row=0,column=1)
        self.stickState.grid(row=0,column=2)
        self.infoState.grid(row=1,column=1)
        self.oneStBut.grid(row=2,column=0)
        self.twoStBut.grid(row=2,column=1)
        self.threeStBut.grid(row=2,column=2)

        self.n = Node(self.nSticks, 'MAX')
        if fp == 'CPU':
            self.cputurn()
    def maketurn(self, ns):
        self.nSticks -= ns
        for child in self.n.children:
            if child.sticks == self.nSticks:
                self.n = child
        self.gameState['text']=('| '*self.nSticks)
        self.stickState['text']=(str(self.nSticks))
        if self.nSticks == 0:
            self.infoState['text'] = 'YOU WON'
        else:
            self.cputurn()
    def cputurn(self):
        for child in self.n.children:
            if self.n.value == child.value:
                self.infoState['text']=('CPU picked up {} sticks'.format(self.nSticks-child.sticks))
                self.nSticks = child.sticks
                self.n = child
                break
        self.gameState['text']=('| '*self.nSticks)
        self.stickState['text']=(str(self.nSticks))
        if self.nSticks == 0:
            self.infoState['text'] = 'CPU WON'



class Node(object):
    def __init__(self, sticks, level, value=0):
        self.sticks = sticks
        self.level = level
        self.children = []
        if self.sticks > 0:
            self.addchildren()
            if self.level == 'MAX':
                self.value = (max(self.children, key=attrgetter('value')).value)
            else:
                self.value = (min(self.children, key=attrgetter('value')).value)
        else:
            if self.level == 'MAX':
                self.value = -1
            else:
                self.value = 1

    def addchildren(self):
        if self.sticks == 1:
            self.children.append(Node(self.sticks - 1, self.switchlevel()))
        elif self.sticks == 2:
        #else:
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
        ret = '\t'*nlevel+repr(self.sticks)+' '+repr(self.value)+'\n'
        for child in self.children:
            ret += child.__str__(nlevel+1)
        return ret


def play(fp, scount):
    sticks = scount
    if (fp=="CPU"):
        n = Node(sticks, 'MAX')
    else:
        nsticks = input("Pick up 1, 2 or 3 sticks ")
        sticks -= int(nsticks)
        n = Node(sticks,'MAX')
    while(sticks>0):
        print('|'*sticks)
        for child in n.children:
            if n.value == child.value:
                print('CPU is picking up {} sticks'.format(sticks-child.sticks))
                sticks = child.sticks
                n = child
                break
        if sticks == 0:
            break
        print('|'*sticks)
        nsticks = input("Pick up 1, 2 or 3 sticks ")
        sticks -= int(nsticks)
        for child in n.children:
            if child.sticks == sticks:
                n = child
    if n.level == 'MIN':
        print('CPU WON')
    else:
        print('YOU WON')

def playcpubutton():
    root.destroy()
    return
def playhumanbutton():
    return
def main():
    root = Tk()
    root.title('Stick Game')
    ss = setupScreen(root)

    root.mainloop()



if __name__ == '__main__':
    main()