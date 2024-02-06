import pygame as py
from pygame.locals import *
from settings import *
from classes import *

py.init()
py.display.set_caption("Pygame")

flags = HWSURFACE | DOUBLEBUF
surf = py.display.set_mode(SCALED_RES, flags)



c = Car((21, 64), (6, 6), surf)
c.draw_car()
FPS = 12
roadTiles = [
    RoadTile((0,0),2,0, surf),
    RoadTile((0,48),1,1, surf),
]

while 1:
    surf.fill(COLOR_1)

    for e in py.event.get():
        if e.type == QUIT:
            py.quit()
            exit()


    for r in roadTiles:
        r.draw()
    c.draw()
    py.display.update()
    py.time.Clock().tick(FPS)