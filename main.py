import pygame as py
py.init

ps = py.display.set_mode((600,400))
py.display.set_caption("PIDOR")

WHITE = (255, 255, 255)

py.draw.circle(ps, WHITE, (60, 250), 35)
py.draw.circle(ps, WHITE, (100, 250), 35)
py.draw.ellipse(ps, WHITE, (65, 80, 30, 200))
py.display.update()

while 1:
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()