from colors import *
class Picture:
  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
      vertical.append(value[::-1])
    return Picture(None)
  
  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(None)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    neg = []
    for linea in self.img:
        lineaNeg = ""
        for caracter in linea:
          lineaNeg += ""+self._invColor(caracter)
        neg.append(lineaNeg)
    return Picture(neg)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    nuevaFigura = []
    for i in range(len(self.img)):
      nuevaFigura.append(self.img[i] + p.img[i]) # concatenamos de fila en fila
    return Picture(nuevaFigura)

  def up(self, p):
    """ Devuelve una nueva figura poniendo la figura p debajo de la figura actual """
    nuevaFigura = []
    for i in self.img:
      nuevaFigura.append(i)
    for j in p.img:
      nuevaFigura.append(j)
    return Picture(nuevaFigura)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    nuevaFigura = []
    for i in p.img:
      nuevaFigura.append(i)
    for j in self.img:
      nuevaFigura.append(j)

    return Picture(nuevaFigura)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

