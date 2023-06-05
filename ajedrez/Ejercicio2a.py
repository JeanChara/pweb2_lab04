from interpreter import draw
from chessPictures import *

draw(knight.negative().under(knight).join(knight.negative().up(knight)))