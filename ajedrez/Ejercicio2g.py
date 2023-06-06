from interpreter import draw
from chessPictures import *

#draw((knight.join(knight.negative())).verticalMirror())
# version original
"""draw(knight.inSquare(0).negative().join(knight.inSquare(1)))
torres = rock.join(knight).join(bishop).join(queen).join(king).join(bishop).join(knight).join(rock)
peones = pawn.horizontalRepeat(8)

fila = (square.join(square.negative())).horizontalRepeat(4)
espacio = (fila.up(fila.negative())).verticalRepeat(2)

fichas = (torres.under(peones))
fichasN = (peones.negative().under(torres.negative()))

tablero = (fichasN.up(espacio).up(fichas))

draw(tablero)
"""
# version mejorada, con piezas en los cuadros
torres = rock.inSquare(1).join(knight.inSquare(0)).join(bishop.inSquare(1)).join(queen.inSquare(0)).join(king.inSquare(1)).join(bishop.inSquare(0)).join(knight.inSquare(1)).join(rock.inSquare(0))
peones = (pawn.inSquare(0).join(pawn.inSquare(1))).horizontalRepeat(4)

fila = (square.join(square.negative())).horizontalRepeat(4)
espacio = (fila.up(fila.negative())).verticalRepeat(2)

fichas = (torres.under(peones))
fichasN = (peones.negative().under(torres.negative()))

tablero = (fichasN.up(espacio).up(fichas))

draw(tablero) # imprime el tablero