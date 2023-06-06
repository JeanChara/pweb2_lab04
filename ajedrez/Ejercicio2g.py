from interpreter import draw
from chessPictures import *

#draw((knight.join(knight.negative())).verticalMirror())
torres = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)
peones = pawn.horizontalRepeat(8)

fila = (square.join(square.negative())).horizontalRepeat(4)
espacio = (fila.up(fila.negative())).verticalRepeat(2)

fichas = (peones.under(torres))
fichasN = (peones.negative().under(torres.negative()))

tablero = (fichasN.up(espacio).up(fichas))

draw(tablero)
