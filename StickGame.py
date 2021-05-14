import time
from operator import attrgetter
from tkinter import *

class resultScreen:
    def __init__(self,master,winner):
        self.master = master
        self.master.title('Results')
        self.master.geometry("+300+300")
        self.resultablel = Label(self.master, text='{} won!'.format(winner)).grid(row=0,column=1)
        self.playagainButton = Button(self.master,text='Play again!',width=10,command=self.playagain).grid(row=1,column=0)
        self.exitButton = Button(self.master,text='Exit',width=10,command=master.destroy).grid(row=1,column=2)
    def playagain(self):
        self.master.destroy()
        self.master = Tk()
        self.app = setupScreen(self.master)
        self.master.mainloop()

class setupScreen:
    def __init__(self, master):
        self.master = master
        self.master.title('Setup')
        self.master.geometry("+300+300")
        self.setupLablel = Label(self.master, text='Who starts the game?').grid(row=0,column=1)
        self.cpuButton = Button(self.master,text='CPU',width=6,command=lambda: self.playgame('CPU')).grid(row=1,column=0)
        self.playerButton = Button(self.master,text='PLAYER',width=6,command=lambda: self.playgame('ME')).grid(row=1,column=2)
    def playgame(self,fp):
        self.master.destroy()
        self.master = Tk()
        self.app = gameScreen(self.master,fp)
        self.master.mainloop()
    

class gameScreen:
    def __init__(self,master,fp):
        self.master = master
        self.master.title('Subtraction Game')
        self.master.geometry("+300+300")
        self.nSticks = 17
        self.gameState = Label(self.master, text=('| '*self.nSticks))
        self.stickState = Label(self.master, text=self.nSticks)
        self.infoState = Label(self.master, text='')
        self.oneStBut = Button(self.master, text='1', width = 4, command=lambda: self.maketurn(1))
        self.twoStBut = Button(self.master, text='2', width = 4, command=lambda: self.maketurn(2))
        self.threeStBut = Button(self.master, text='3', width = 4, command=lambda: self.maketurn(3))

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
            self.master.destroy()
            self.master = Tk()
            self.app = resultScreen(self.master,'You')
            self.master.mainloop()
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
            self.master.destroy()
            self.master = Tk()
            self.app = resultScreen(self.master,'CPU')
            self.master.mainloop()



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
        ret = '\t'*nlevel+repr(self.level)+' '+repr(self.sticks)+' '+repr(self.value)+'\n'
        for child in self.children:
            ret += child.__str__(nlevel+1)
        return ret
  
def main():
    root = Tk()
    root.title('Subtraction Game')
    ss = setupScreen(root)
    root.mainloop()


if __name__ == '__main__':
    main()