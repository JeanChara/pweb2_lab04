from interpreter import draw
from chessPictures import *

draw(knight.up(knight.negative().horizontalMirror()).join(knight.negative().up(knight.horizontalMirror())))