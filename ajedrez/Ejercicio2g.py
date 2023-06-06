from interpreter import draw
from chessPictures import *

#corregido
torres = square.negative().under(rock).join(square.under(knight)).join(square.negative().under(bishop)).join(square.under(queen)).join(square.negative().under(king)).join(square.under(bishop)).join(square.negative().under(knight)).join(square.under(rock))
peones = (square.under(pawn).join(square.negative().under(pawn))).horizontalRepeat(4)

fila = (square.join(square.negative())).horizontalRepeat(4)
espacio = (fila.up(fila.negative())).verticalRepeat(2)

fichas = (peones.up(torres))
fichasN = (torres.negative().up(peones.negative()))

tablero = (fichasN.up(espacio).up(fichas))

draw(tablero)