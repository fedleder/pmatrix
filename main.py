import curses 
import keyboard
import time
import random

caratteri = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "А", "В", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "Т", "U", "V", "W", "X", "Y", "Z", ",", ";", ".", ":", "-", "_", "#", "@", "!", "£", "$", "%", "&", "/", "(", ")", "=", "?", "'", "^", "+", "*", ">", "<"]

class FallingChar:
    def __init__(self, h, w, stdscr, x, y, color):
        self.stdscr = stdscr
        self.h = h
        self.w = w
        self.x = x
        self.y = y
        self.char = random.choice(caratteri)
        self.color = color

    def draw_char(self):
        try:
            self.stdscr.addstr(self.y, self.x, self.char, self.color)
        except:
            pass

class Coda:
    def __init__(self, h, w, stdscr):
        self.stdscr = stdscr
        self.h = h
        self.w = w
        self.lenght = random.randint(3, int(h/20*15))
        self.array_coda = []
        self.x = random.randrange(0, w , 2)
        self.y = 0

    def setup(self):
        self.primo = True
        for i in range(self.lenght):
            if self.primo:
                self.array_coda.append(FallingChar(self.h, self.w, self.stdscr, self.x, self.y, curses.color_pair(2)))
                self.primo = False
            else:
                self.array_coda.append(FallingChar(self.h, self.w, self.stdscr, self.x, self.y, curses.color_pair(1)))
            self.y -= 1

    def draw_coda(self):
        for self.char in self.array_coda:
            self.char.draw_char()

    def move_coda(self):
        self.cp_char = self.array_coda[0].char
        for self.char in self.array_coda:
            self.char.y += 1
            if self.array_coda.index(self.char) == 0:
                self.char.char = random.choice(caratteri)
            else:
                self.index = self.array_coda.index(self.char) 
                self.old_char = self.array_coda[self.index].char
                self.char.char = self.cp_char
                self.cp_char = self.old_char
        

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

    lista_code = []

    prova = True

    while True:

        stdscr.clear()

        h, w = stdscr.getmaxyx()

        max_nuove_liste = int(w/30)

        nuove_liste = random.randint(0, max_nuove_liste)

        for i in range(nuove_liste):
            lista_code.append(Coda(h, w, stdscr))
            lista_code[len(lista_code)-1].setup()
            
        for coda in lista_code:
            coda.draw_coda()
            coda.move_coda()

        if keyboard.is_pressed('escape'):
            break

        stdscr.refresh()

        time.sleep(0.01)

curses.wrapper(main)
