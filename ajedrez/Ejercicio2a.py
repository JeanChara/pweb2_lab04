from interpreter import draw
from chessPictures import *

draw(knight.up(knight.negative()).join(knight.negative().up(knight)))