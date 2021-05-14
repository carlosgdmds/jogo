import pygame

def Verifica(w,h):
    if w == 1024 and h == 768:
        w = w
        h = h-50
    elif w == 1280 and h ==720:
        w = w
        h = h
    elif w == 1366 and h == 768:
        w = w
        h = h-50
   # print(w,h)
    return w, h
