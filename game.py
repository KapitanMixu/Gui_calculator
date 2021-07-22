import numpy as np
import math

class Player:
    Name = ""
    Color = ""
    Hexs = [0, 0, 0, 0]
    Techs = [0, 0, 0]
    Stechs = [0, 0, 0, 0]
    Emb = [0, 0, 0, 0]
    points = 0


class Board:
    c = 0
    w = [0, 0, 0, 0, 0, 0]
    z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    o = 20


def pointsCal(P):
    num = 6 * P.Hexs[0] + (3 + P.Stechs[1]) * P.Hexs[1] + 2 * P.Hexs[2] + 1 * math.floor(P.Hexs[3]/(3 - P.Stechs[2]))
    for x in range(4):
        if P.Emb[x] != 0:
            num += P.Emb[x] + P.Stechs[3]
    for y in range(3):
        if P.Techs[y] == 4:
            num += 1
        if P.Techs[y] == 5:
            num += 2
        if P.Techs[y] == 6:
            num += 4
        if P.Techs[y] == 7:
            num += 7
    if P.Stechs[0] == 1:
        num += min(P.Techs)
    return num

class desc:
    Opis = "Aplikacja Eclipse Kalkulator pozwala na szybkie wyliczenie punktów na koniec rozgrywki gry planszowej Eclipse"