from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame, random, time, sys
from pygame.locals import *
from gerak import *


w,h= 1680,1000
ludo = True
menustart = True
menulevel = False
PilihanLevel = None

def papan():
    glBegin(GL_QUADS)
    glColor3f(1,1,1)
    glVertex2f(30,30)#A
    glVertex2f(30,720)#B
    glVertex2f(720,720)#O
    glVertex2f(720,30)#P

    #merah
    glColor3f(1,0,0)
    glVertex2f(50, 50)#A
    glVertex2f(50, 300)#D
    glVertex2f(300, 300)#C1
    glVertex2f(300, 50)#E1

    glVertex2f(300, 100)#L4
    glVertex2f(400, 100)#N4
    glVertex2f(400, 150)#I4
    glVertex2f(300, 150)#K4

    glVertex2f(400, 150)#I4
    glVertex2f(350, 150)#J4
    glVertex2f(350, 300)#B3
    glVertex2f(400, 300)#C3

    #ijo
    glColor3f(0,1,0)
    glVertex2f(50, 700)#B
    glVertex2f(300, 700)#W
    glVertex2f(300, 450)#V
    glVertex2f(50, 450)#U

    glVertex2f(100, 450)#v1
    glVertex2f(100, 350)#m1
    glVertex2f(150, 350)#O1
    glVertex2f(150, 450)#W1

    glVertex2f(150, 400)#N1
    glVertex2f(300, 400)#T1
    glVertex2f(300, 350)#U1
    glVertex2f(150, 350)#O1

    #biru
    glColor3f(0,1,1)
    glVertex2f(450, 700)#Z
    glVertex2f(700, 700)#O
    glVertex2f(700, 450)#B1
    glVertex2f(450, 450)#A1

    glVertex2f(450, 650)#H2
    glVertex2f(350, 650)#J2
    glVertex2f(350, 600)#M2
    glVertex2f(450, 600)#O2

    glVertex2f(350, 600)#M2
    glVertex2f(400, 600)#N2
    glVertex2f(400, 450)#Z2
    glVertex2f(350, 450)#A3

    #pink
    glColor3f(1,0,1)
    glVertex2f(450, 300)#f1
    glVertex2f(700, 300)#H1
    glVertex2f(700, 50)#P
    glVertex2f(450, 50)#G1

    glVertex2f(650, 300)#U3
    glVertex2f(600, 300)#Q3
    glVertex2f(600, 400)#O3
    glVertex2f(650, 400)#S3

    glVertex2f(450, 400)#E3
    glVertex2f(450, 350)#D3
    glVertex2f(600, 350)#P3
    glVertex2f(600, 400)#O3

    #kotak putih
    glColor3f(1,1,1)
    glVertex2f(100, 250)#d
    glVertex2f(250, 250)#E
    glVertex2f(250, 100)#F
    glVertex2f(100, 100)#C
    
    glVertex2f(650, 100)#R
    glVertex2f(650, 250)#S
    glVertex2f(500, 250)#T
    glVertex2f(500, 100)#Q

    glVertex2f(500, 650)#K
    glVertex2f(500, 500)#L
    glVertex2f(650, 500)#M
    glVertex2f(650, 650)#N

    glVertex2f(100, 650)#G
    glVertex2f(100, 500)#H
    glVertex2f(250, 500)#I
    glVertex2f(250, 650)#J
    glEnd()

    glBegin(GL_TRIANGLES)
    #merah
    glColor3f(1,0,0)
    glVertex2f(375, 375)#tengah
    glVertex2f(450, 300)#f1
    glVertex2f(300, 300)#C1
    
    #IJO
    glColor3f(0,1,0)
    glVertex2f(375, 375)#tengah
    glVertex2f(300, 300)#c1
    glVertex2f(300, 450)#V
    
    #BIRU
    glColor3f(0,1,1)
    glVertex2f(375, 375)#tengah
    glVertex2f(300, 450)#V
    glVertex2f(450, 450)#A1
    
    #PINK
    glColor3f(1,0,1)
    glVertex2f(375, 375)#tengah
    glVertex2f(450, 450)#A1
    glVertex2f(450, 300)#f1
    glEnd()

def garis():
    glLineWidth(4)
    glColor3f(0,0,0)
    #ijo
    glBegin(GL_LINE_STRIP)
    glVertex2f(100, 650)#G
    glVertex2f(100, 500)#H
    glVertex2f(250, 500)#I
    glVertex2f(250, 650)#J
    glVertex2f(100, 650)#G
    glEnd()
    
    #merah
    glBegin(GL_LINE_STRIP)
    glVertex2f(100, 250)#d
    glVertex2f(250, 250)#E
    glVertex2f(250, 100)#F
    glVertex2f(100, 100)#C
    glVertex2f(100, 250)#d
    glEnd()
    
    #biru
    glBegin(GL_LINE_STRIP)
    glVertex2f(500, 650)#K
    glVertex2f(500, 500)#L
    glVertex2f(650, 500)#M
    glVertex2f(650, 650)#N
    glVertex2f(500, 650)#K
    glEnd()
    
    #pink
    glBegin(GL_LINE_STRIP)
    glVertex2f(650, 100)#R
    glVertex2f(650, 250)#S
    glVertex2f(500, 250)#T
    glVertex2f(500, 100)#Q
    glVertex2f(650, 100)#R
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(50, 50)#a
    glVertex2f(50, 700)#B
    glVertex2f(700, 700)#O
    glVertex2f(700, 50)#P
    glVertex2f(50, 50)#a
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(50, 450)#u
    glVertex2f(700, 450)#B1
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(50, 300)#D1
    glVertex2f(700, 300)#H1
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(300, 700)#W
    glVertex2f(300, 50)#E1
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(450, 700)#Z
    glVertex2f(450, 50)#G1
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(300, 450)#V
    glVertex2f(450, 300)#F1
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(300, 300)#C1
    glVertex2f(450, 450)#A1
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(50, 400)#J1
    glVertex2f(300, 400)#T1
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(50, 350)#K1
    glVertex2f(300, 350)#U1
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(100, 450)#V1
    glVertex2f(100, 300)#Z1
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(150, 450)#w1
    glVertex2f(150, 300)#A2
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(200, 450)#D2
    glVertex2f(200, 300)#B2
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(250, 450)#D2
    glVertex2f(250, 300)#C2
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(350, 300)#B3
    glVertex2f(350, 50)#P4
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(400, 300)#C3
    glVertex2f(400, 50)#Q4
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(300, 250)#Z3
    glVertex2f(450, 250)#C4
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(300, 200)#D4
    glVertex2f(450, 200)#G4
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(300, 150)#K4
    glVertex2f(450, 150)#H4
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(300, 100)#L4
    glVertex2f(450, 100)#O4
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(450, 400)#E3
    glVertex2f(700, 400)#V3
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(450, 350)#D3
    glVertex2f(700, 350)#W3
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(500, 450)#F3
    glVertex2f(500, 300)#I3
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(550, 450)#J3
    glVertex2f(550, 300)#M3
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(600, 450)#N3
    glVertex2f(600, 300)#Q3
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(650, 450)#R3
    glVertex2f(650, 300)#U3
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(350, 700)#F2
    glVertex2f(350, 450)#A3
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(400, 700)#G2
    glVertex2f(400, 450)#Z2
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(300, 650)#K2
    glVertex2f(450, 650)#H2
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(300, 600)#L2
    glVertex2f(450, 600)#O2
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(300, 550)#S2
    glVertex2f(450, 550)#P2
    glEnd()
   
    glBegin(GL_LINE_STRIP)
    glVertex2f(300, 500)#T2
    glVertex2f(450, 500)#W2
    glEnd()

def bintang1():
    glColor3f(0,0,0)
    # glTranslatef(x,y,0)
    glBegin(GL_POLYGON)
    glVertex2f(174, 322)#d2 tengah
    glVertex2f(175, 345)#r4
    glVertex2f(180, 330)#C5
    glVertex2f(195, 330)#B5
    glVertex2f(185, 320)#A5
    glVertex2f(190, 305)#Z4
    glVertex2f(175, 315)#W4
    glVertex2f(160, 305)#V4
    glVertex2f(165, 320)#U4
    glVertex2f(155, 330)#T4
    glVertex2f(170, 330)#S4
    glVertex2f(175, 345)#r4
    glEnd()

def bintang2():
    glColor3f(0,0,0)
    # glTranslatef(x,y,0)
    glBegin(GL_POLYGON)
    glVertex2f(174+150, 322+250)#d2 tengah
    glVertex2f(175+150, 345+250)#r4
    glVertex2f(180+150, 330+250)#C5
    glVertex2f(195+150, 330+250)#B5
    glVertex2f(185+150, 320+250)#A5
    glVertex2f(190+150, 305+250)#Z4
    glVertex2f(175+150, 315+250)#W4
    glVertex2f(160+150, 305+250)#V4
    glVertex2f(165+150, 320+250)#U4
    glVertex2f(155+150, 330+250)#T4
    glVertex2f(170+150, 330+250)#S4
    glVertex2f(175+150, 345+250)#r4
    glEnd()

def bintang3():
    glColor3f(0,0,0)
    # glTranslatef(x,y,0)
    glBegin(GL_POLYGON)
    glVertex2f(174+400, 322+100)#d2 tengah
    glVertex2f(175+400, 345+100)#r4
    glVertex2f(180+400, 330+100)#C5
    glVertex2f(195+400, 330+100)#B5
    glVertex2f(185+400, 320+100)#A5
    glVertex2f(190+400, 305+100)#Z4
    glVertex2f(175+400, 315+100)#W4
    glVertex2f(160+400, 305+100)#V4
    glVertex2f(165+400, 320+100)#U4
    glVertex2f(155+400, 330+100)#T4
    glVertex2f(170+400, 330+100)#S4
    glVertex2f(175+400, 345+100)#r4
    glEnd()

def bintang4():
    glColor3f(0,0,0)
    # glTranslatef(x,y,0)
    glBegin(GL_POLYGON)
    glVertex2f(174+250, 322-150)#d2 tengah
    glVertex2f(175+250, 345-150)#r4
    glVertex2f(180+250, 330-150)#C5
    glVertex2f(195+250, 330-150)#B5
    glVertex2f(185+250, 320-150)#A5
    glVertex2f(190+250, 305-150)#Z4
    glVertex2f(175+250, 315-150)#W4
    glVertex2f(160+250, 305-150)#V4
    glVertex2f(165+250, 320-150)#U4
    glVertex2f(155+250, 330-150)#T4
    glVertex2f(170+250, 330-150)#S4
    glVertex2f(175+250, 345-150)#r4
    glEnd()
# (325,125)
class pion:
    def __init__(self,warna,idxx = 0):
        self.warna = warna
        self.idxx = idxx
        self.idxxx = 0
        self.map = True
        self.balik = False
        self.finish = False

    
    def tampil(self):
        if self.warna=="merah":
            glColor3ub(255,0,0) 
        elif self.warna=="ijo":
            glColor3ub(0,255,0)
        elif self.warna=="biru":
            glColor3ub(0,255,255)
        elif self.warna=="pink":
            glColor3ub(255,0,255)
        if self.map:
            glBegin(GL_QUADS)
            glVertex2f(fullmap[self.idxx][0]+15,fullmap[self.idxx][1]-15)
            glVertex2f(fullmap[self.idxx][0]-15,fullmap[self.idxx][1]-15)
            glVertex2f(fullmap[self.idxx][0]-15,fullmap[self.idxx][1]+15)
            glVertex2f(fullmap[self.idxx][0]+15,fullmap[self.idxx][1]+15)
            glEnd()
            glColor3f(0,0,0)
            glLineWidth(4)
            glBegin(GL_LINE_STRIP)
            glVertex2f(fullmap[self.idxx][0]+15,fullmap[self.idxx][1]-15)
            glVertex2f(fullmap[self.idxx][0]-15,fullmap[self.idxx][1]-15)
            glEnd()
            glBegin(GL_LINE_STRIP)
            glVertex2f(fullmap[self.idxx][0]-15,fullmap[self.idxx][1]-15)
            glVertex2f(fullmap[self.idxx][0]-15,fullmap[self.idxx][1]+15)
            glEnd()
            glBegin(GL_LINE_STRIP)
            glVertex2f(fullmap[self.idxx][0]-15,fullmap[self.idxx][1]+15)
            glVertex2f(fullmap[self.idxx][0]+15,fullmap[self.idxx][1]+15)
            glEnd()
            glBegin(GL_LINE_STRIP)
            glVertex2f(fullmap[self.idxx][0]+15,fullmap[self.idxx][1]+15)
            glVertex2f(fullmap[self.idxx][0]+15,fullmap[self.idxx][1]-15)
            glEnd()
        else:
            glBegin(GL_QUADS)
            glVertex2f(Warna[self.warna][self.idxxx][0]+15,Warna[self.warna][self.idxxx][1]-15)
            glVertex2f(Warna[self.warna][self.idxxx][0]-15,Warna[self.warna][self.idxxx][1]-15)
            glVertex2f(Warna[self.warna][self.idxxx][0]-15,Warna[self.warna][self.idxxx][1]+15)
            glVertex2f(Warna[self.warna][self.idxxx][0]+15,Warna[self.warna][self.idxxx][1]+15)
            glEnd()
            glColor3f(0,0,0)
            glLineWidth(4)
            glBegin(GL_LINE_STRIP)
            glVertex2f(Warna[self.warna][self.idxxx][0]+15,Warna[self.warna][self.idxxx][1]-15)
            glVertex2f(Warna[self.warna][self.idxxx][0]-15,Warna[self.warna][self.idxxx][1]-15)
            glEnd()
            glBegin(GL_LINE_STRIP)
            glVertex2f(Warna[self.warna][self.idxxx][0]-15,Warna[self.warna][self.idxxx][1]-15)
            glVertex2f(Warna[self.warna][self.idxxx][0]-15,Warna[self.warna][self.idxxx][1]+15)
            glEnd()
            glBegin(GL_LINE_STRIP)
            glVertex2f(Warna[self.warna][self.idxxx][0]-15,Warna[self.warna][self.idxxx][1]+15)
            glVertex2f(Warna[self.warna][self.idxxx][0]+15,Warna[self.warna][self.idxxx][1]+15)
            glEnd()
            glBegin(GL_LINE_STRIP)
            glVertex2f(Warna[self.warna][self.idxxx][0]+15,Warna[self.warna][self.idxxx][1]+15)
            glVertex2f(Warna[self.warna][self.idxxx][0]+15,Warna[self.warna][self.idxxx][1]-15)
            glEnd()

    def move(self, kkondisi):
        if self.map:
            self.idxx += 1
            if self.idxx == 44:
                self.idxx = 0
            if self.warna == "ijo" and self.idxx == 10:
                self.map = False
            if self.warna == "biru" and self.idxx == 21:
                self.map = False
            if self.warna == "pink" and self.idxx == 32:
                self.map = False
            if self.warna == "merah" and self.idxx == 43:
                self.map = False
        else:
            if self.finish:
                pass
            else:
                if self.balik:
                    self.idxxx -= 1
                    if self.idxxx == -5:
                        self.idxxx = 0
                        self.balik = False
                else:
                    self.idxxx += 1
                    if self.idxxx == 4:
                        self.idxxx = -1
                        self.balik = True
                        
                if kkondisi == True:
                    if self.idxxx == -1:
                        print("MENANK")
                        self.finish = True
                    if self.balik:
                        self.idxxx += 5
                        self.balik = False
    def reset(self):
        self.idxx = 0
    def finishh(self):
        return self.finish

    def tampilstart(self,x,y):
        if self.warna=="merah":
            glColor3ub(255,0,0)
        elif self.warna=="ijo":
            glColor3ub(0,255,0)
        elif self.warna=="biru":
            glColor3ub(0,255,255)
        elif self.warna=="pink":
            glColor3ub(255,0,255)
        glBegin(GL_QUADS)
        glVertex2f(x+15,y-15)
        glVertex2f(x-15,y-15)
        glVertex2f(x-15,y+15)
        glVertex2f(x+15,y+15)
        glEnd()
        glColor3f(0,0,0)
        glLineWidth(4)
        glBegin(GL_LINE_STRIP)
        glVertex2f(x+15,y-15)
        glVertex2f(x-15,y-15)
        glEnd()
        glBegin(GL_LINE_STRIP)
        glVertex2f(x-15,y-15)
        glVertex2f(x-15,y+15)
        glEnd()
        glBegin(GL_LINE_STRIP)
        glVertex2f(x-15,y+15)
        glVertex2f(x+15,y+15)
        glEnd()
        glBegin(GL_LINE_STRIP)
        glVertex2f(x+15,y+15)
        glVertex2f(x+15,y-15)
        glEnd()

pionm1 = pion('merah')
pionm2 = pion('merah')
pionm3 = pion('merah')
pionm4 = pion('merah')
piong1 = pion('ijo', 11)
piong2 = pion('ijo', 11)
piong3 = pion('ijo', 11)
piong4 = pion('ijo', 11)
pionb1 = pion('biru', 22)
pionb2 = pion('biru', 22)
pionb3 = pion('biru', 22)
pionb4 = pion('biru', 22)
pionp1 = pion('pink', 33)
pionp2 = pion('pink', 33)
pionp3 = pion('pink', 33)
pionp4 = pion('pink', 33)

def iterate():
    glViewport(0, 0, 1680, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1680, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def draw_text(text,font, x, y):
    glColor3f(1,1,1)
    glRasterPos2f(x, y)
    for char in text:
        glutBitmapCharacter(font, ord(char))

truefalse = [True,True,True,True,True,True,True,True,True,True,True,True,True,True,True,True]
idx = 0
dadu = 0
player = ['m','i','b','p']
turn = 0
kpion = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

def level(button, state, x, y):
    global menulevel, menustart, ludo, dadu, PilihanLevel
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        print(x,y)
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if menustart:
            ax = 635
            bx = 920
            ay = 390
            by = 440
            ayq = 505
            byq = 555
            if ax <= x <= bx and ay <= y <= by:
                menustart = False
                menulevel = True
            elif ax <= x <= bx and ayq <= y <= byq:
                ludo = False
                sys.exit() # errorrr
        elif menulevel:
            axl = 635
            bxl = 820
            ayeasy = 305
            byeasy = 355
            aymed = 380
            bymed = 425
            ayhard = 450
            byhard = 500
            axback = 655
            bxback = 790
            ayback = 550
            byback = 595
            if axl <= x <= bxl and ayeasy <= y <= byeasy:
                menulevel = False
                PilihanLevel = "e"
                # return easy()
            elif axl <= x <= bxl and aymed <= y <= bymed:
                menulevel = False
                PilihanLevel = "m"
                # return medium()
            elif axl <= x <= bxl and ayhard <= y <= byhard:
                menulevel = False
                PilihanLevel = "h"
                # return hard()
            elif axback <= x <= bxback and ayback <= y <= byback:
                menulevel = False
                menustart = True

def easy():
    return random.randint(1,6)
def medium():
    angka = [1,2,3,4,5,6]
    peluang = [0.2, 0.2, 0.2, 0.2, 0.2, 0.1]
    return random.choices(angka, weights=peluang)[0]
def hard():
    angka = [1,2,3,4,5,6]
    peluang = [0.3, 0.3, 0.3, 0.3, 0.2, 0.1]
    return random.choices(angka, weights=peluang)[0]

def keyboard(key, x, y):
    global dadu,idx,truefalse,turn,kpion, PilihanLevel
    if key == b'w' :
        # level()
        if PilihanLevel == "e":
            dadu = easy()
        elif PilihanLevel == "m":
            dadu = medium()
        elif PilihanLevel == "h":
            dadu = hard()
        if dadu == 6:
            if player[turn] == 'm':
                kpion[0] = True
                if truefalse[0] :
                    truefalse[0] = False
                    return
                if truefalse[1] and pionm1.finishh():
                    truefalse[1] = False
                    return
                if truefalse[2] and pionm2.finishh():
                    truefalse[2] = False
                    return
                if truefalse[3] and pionm3.finishh():
                    truefalse[3] = False
                    return
            if player[turn] == 'i':
                kpion[4] = True
                if truefalse[4]:
                    truefalse[4] = False
                    return
                if truefalse[5] and piong1.finishh():
                    truefalse[5] = False
                    return
                if truefalse[6] and piong2.finishh():
                    truefalse[6] = False
                    return
                if truefalse[7] and piong3.finishh():
                    truefalse[7] = False
                    return
            if player[turn] == 'b':
                kpion[8] = True
                if truefalse[8]:
                    truefalse[8] = False
                    return
                if truefalse[9] and pionb1.finishh():
                    truefalse[9] = False
                    return
                if truefalse[10] and pionb2.finishh():
                    truefalse[10] = False
                    return
                if truefalse[11] and pionb3.finishh():
                    truefalse[11] = False
                    return
            if player[turn] == 'p':
                kpion[12] = True
                if truefalse[12]:
                    truefalse[12] = False
                    return
                if truefalse[13] and pionp1.finishh():
                    truefalse[13] = False
                    return
                if truefalse[14] and pionp2.finishh():
                    truefalse[14] = False
                    return
                if truefalse[15] and pionp3.finishh():
                    truefalse[15] = False
                    return
        else:
            turn+=1
            if turn == 4:
                turn = 0
        idx = 0
        def coba(value):
            global idx, kondisi, dadu, kpion
            kondisi = False
            if idx < dadu:
                if idx == dadu-1:
                    kondisi = True
                if kpion[0] and player[turn] == "m": pionm1.move(kondisi)
                if kpion[1] and player[turn] == "m": pionm2.move(kondisi)
                if kpion[2] and player[turn] == "m": pionm3.move(kondisi)
                if kpion[3] and player[turn] == "m": pionm4.move(kondisi)
                if kpion[4] and player[turn] == "i": piong1.move(kondisi)
                if kpion[5] and player[turn] == "i": piong2.move(kondisi)
                if kpion[6] and player[turn] == "i": piong3.move(kondisi)
                if kpion[7] and player[turn] == "i": piong4.move(kondisi)
                if kpion[8] and player[turn] == "b": pionb1.move(kondisi)
                if kpion[9] and player[turn] == "b": pionb2.move(kondisi)
                if kpion[10] and player[turn] == "b": pionb3.move(kondisi)
                if kpion[11] and player[turn] == "b": pionb4.move(kondisi)
                if kpion[12] and player[turn] == "p": pionp1.move(kondisi)
                if kpion[13] and player[turn] == "p": pionp2.move(kondisi)
                if kpion[14] and player[turn] == "p": pionp3.move(kondisi)
                if kpion[15] and player[turn] == "p": pionp4.move(kondisi)
                idx += 1
                glutTimerFunc(50,coba,0)
    glutTimerFunc(50,coba,0)

def load_texture(file_path):
    image = pygame.image.load(file_path)
    image_data = pygame.image.tostring(image, "RGBA", 1)

    width, height = image.get_size()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

    return texture_id

def draw_image(texture_id, x, y, width, height):
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex2f(x, y)

    glTexCoord2f(1, 0)
    glVertex2f(x + width, y)

    glTexCoord2f(1, 1)
    glVertex2f(x + width, y + height)

    glTexCoord2f(0, 1)
    glVertex2f(x, y + height)
    glEnd()

    glDisable(GL_TEXTURE_2D)

def main():
    global truefalse,turn, dadu, kpion
    sudahfinish = [
        pionm1.finishh() + pionm2.finishh() + pionm3.finishh() + pionm4.finishh(), 
        piong1.finishh() + piong2.finishh() + piong3.finishh() + piong4.finishh(), 
        pionb1.finishh() + pionb2.finishh() + pionb3.finishh() + pionb4.finishh(),
        pionp1.finishh() + pionp2.finishh() + pionp3.finishh() + pionp4.finishh()
    ]
    papan()
    garis()
    bintang1()
    bintang2()
    bintang3()
    bintang4()
    p = fullmap
    WARNa = ""
    if player[turn] == "m": WARNa="merah"
    elif player[turn] == "i":WARNa="hijau"
    elif player[turn] == "b":WARNa="biru"
    elif player[turn] == "p":WARNa="pink"
    draw_text(f"daDu : {dadu}",GLUT_BITMAP_HELVETICA_18, 900, 470)
    draw_text(f"tUrn : {WARNa}",GLUT_BITMAP_HELVETICA_18, 900, 420)
    draw_text(f"skor merah : {sudahfinish[0]}",GLUT_BITMAP_HELVETICA_18, 900, 370)
    draw_text(f"skor hijou : {sudahfinish[1]}",GLUT_BITMAP_HELVETICA_18, 900, 320)
    draw_text(f"skor biru : {sudahfinish[2]}",GLUT_BITMAP_HELVETICA_18, 900, 270)
    draw_text(f"skor pink : {sudahfinish[3]}",GLUT_BITMAP_HELVETICA_18, 900, 220)
    if kpion[0] : #merah    
        pionm1.tampil()
    else:
        pion("merah").tampilstart(225,125)
    if pionm1.finishh() and truefalse[1] == False:
        kpion[1] = True
        pionm2.tampil()
    else:
        pion("merah").tampilstart(225,225)
    if pionm2.finishh() and truefalse[2] == False:
        kpion[2] = True
        pionm3.tampil()
    else:
        pion("merah").tampilstart(125,225)
    if pionm3.finishh() and truefalse[3] == False:
        kpion[3] = True
        pionm4.tampil()
    else:
        pion("merah").tampilstart(125,125)

    if kpion[4]: #ijo
        piong1.tampil()
    else:
        pion("ijo").tampilstart(125,525)
    if piong1.finishh() and truefalse[5] == False:
        kpion[5] = True
        piong2.tampil()
    else:
        pion("ijo").tampilstart(125,625)
    if piong2.finishh() and truefalse[6] == False:
        kpion[6] = True
        piong3.tampil()
    else:
        pion("ijo").tampilstart(225,625)
    if piong3.finishh() and truefalse[7] == False:
        kpion[7] = True
        piong4.tampil()
    else:
        pion("ijo").tampilstart(225,525)

    if kpion[8]: #biru
        pionb1.tampil()
    else:
        pion("biru").tampilstart(525,525)
    if pionb1.finishh() and truefalse[9] == False:
        kpion[9] = True
        pionb2.tampil()
    else:
        pion("biru").tampilstart(525,625)
    if pionb2.finishh() and truefalse[10] == False:
        kpion[10] = True
        pionb3.tampil()
    else:
        pion("biru").tampilstart(625,625)
    if pionb3.finishh() and truefalse[11] == False:
        kpion[11] = True
        pionb4.tampil()
    else:
        pion("biru").tampilstart(625,525)

    if kpion[12]: #pink
        pionp1.tampil()
    else:
        pion("pink").tampilstart(525,125)
    if pionp1.finishh() and truefalse[13] == False:
        kpion[13] = True
        pionp2.tampil()
    else:
        pion("pink").tampilstart(525,225)
    if pionp2.finishh() and truefalse[14] == False:
        kpion[14] = True
        pionp3.tampil()
    else:
        pion("pink").tampilstart(625,225)
    if pionp3.finishh() and truefalse[15] == False:
        kpion[15] = True
        pionp4.tampil()
    else:
        pion("pink").tampilstart(625,125)

    if sudahfinish[0] == 4:
        glClear(GL_COLOR_BUFFER_BIT)
        draw_text("merah menang",GLUT_BITMAP_HELVETICA_18, 900, 170)
    elif sudahfinish[1] == 4:
        glClear(GL_COLOR_BUFFER_BIT)
        draw_text("hijou menang",GLUT_BITMAP_HELVETICA_18, 900, 170)
    elif sudahfinish[2] == 4:
        glClear(GL_COLOR_BUFFER_BIT)
        draw_text("biru menang",GLUT_BITMAP_HELVETICA_18, 900, 170)
    elif sudahfinish[3] == 4:
        glClear(GL_COLOR_BUFFER_BIT)
        draw_text("pink menang",GLUT_BITMAP_HELVETICA_18, 900, 170)
def showScreen():
    global truefalse,turn, dadu, kpion
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    if ludo:
        if menustart:
            texture_id = load_texture("menu.png")
            draw_image(texture_id, 0, 0, 1450,800)
        elif menulevel:
            texture_id = load_texture("level.png")
            draw_image(texture_id, 0, 0, 1450,800)
        if not menustart and not menulevel:
            main()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1450, 800)
glutInitWindowPosition(0, 0)
glutCreateWindow("LUDO STRES")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMouseFunc(level)
glutKeyboardFunc(keyboard)
glutMainLoop()