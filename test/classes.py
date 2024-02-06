import pygame as py
from pygame.locals import *
import random
from settings import *
import copy

class Car(py.sprite.Sprite):
    def __init__(self, pos, size, surf):
        super().__init__()
        self.image = py.Surface([size[0]*RES_MULT, size[1]*RES_MULT])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]*RES_MULT
        self.rect.y = pos[1]*RES_MULT
        self.game_surf = surf


        self.carList = [
            [0,0,1,1,0,0],
            [0,1,1,1,1,0],
            [0,1,1,1,1,0],
            [0,1,1,1,1,0],
            [0,1,1,1,1,0],
            [0,1,1,1,1,0],
        ]

    def draw_car(self):



        for i in range(len(self.carList[0])):
            for j in range(len(self.carList[1])):
                if self.carList[j][i] == 1:
                    self.image.fill(COLOR_2, (i*RES_MULT, j*RES_MULT, RES_MULT, RES_MULT))
                else:
                    self.image.fill(COLOR_1, (i*RES_MULT, j*RES_MULT, RES_MULT, RES_MULT))



    def draw(self):
        self.game_surf.blit(self.image, self.rect)


class Test(py.sprite.Sprite):
    def __init__(self, length, surf):
        super().__init__()
        self.image = py.Surface([BASE_RES[0]*RES_MULT, length*RES_MULT])
        self.list = [[0 for i in range(BASE_RES[0])] for j in range(length)]
        for l in self.list:
            l[0],l[len(self.list[0])-1] =1,1


        self.rect = self.image.get_rect()
        self.surf = surf
        self.rect.x, self.rect.y = 0,0
        self.draw_self()
    def draw_self(self):
        for i in range(len(self.list[0])):
            for j in range(len(self.list)):
                if self.list[j][i] == 1:
                    self.image.fill(COLOR_2, (i*RES_MULT, j*RES_MULT, RES_MULT, RES_MULT))
                else:
                    self.image.fill(COLOR_1, (i*RES_MULT, j*RES_MULT, RES_MULT, RES_MULT))
    def angleSelf(self, dir, fact):
        half = int(84/2)
        indent = int(half/fact)
        ___=1

        if dir == "right":
            _ = indent
            for i in range(half):
                for j in range(_):
                    self.list[i][j]=1
                if ___%fact==0:
                    _-=1
                ___+=1
            #doing the same for the bottom half, but opposite
            _= indent
            i = half*2-1
            while _>0 and i>half-11:
                print(i)
                for j in range(_, 48):
                    self.list[i][j]=1
                if ___%fact==0:
                    _+=1
                ___+=1
                i-=1
        self.draw_self()


    def draw(self):
        self.surf.blit(self.image, self.rect)

class RoadTile(py.sprite.Sprite):
    def __init__(self, pos, imgInd, last, surf):
        super().__init__()
        self.image = py.Surface(SCALED_RES)
        self.image = py.transform.scale(py.image.load("sprites/Sprite-000"+str(imgInd)+".png"), (48*RES_MULT, 48*RES_MULT)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]*RES_MULT
        self.rect.y = pos[1]*RES_MULT
        self.surf = surf
        self.last = last

    def draw(self):
        self.rect.y += RES_MULT
        self.surf.blit(self.image, self.rect)
