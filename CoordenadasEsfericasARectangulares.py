from math import sin, cos, radians

from pygame         import init, Color
from pygame.display import set_mode, update
from pygame.gfxdraw import pixel
from pygame.event   import get

from numpy import array
from numpy.linalg import norm

def ptoEsferaUnidad(alfa, beta, esX_Origen = True):
    '''
    OBJ: Convierte coordenadas esfericas a rectangulares.
    alfa, beta en grados sexagesimales -> x, y, z
    Formula obtenida a partir de las proyecciones vertical y
    horizontal. Calcula la normal del planoCam en la supEsfera unidad

    Dos modalidades: con x como origen de beta:
    x, y, z (p. def), con y: (y, x, z)
    '''
    alfa, beta = radians(alfa), radians(beta)
    x, y, z = cos(alfa) * cos(beta), sin(beta) * cos(alfa),\
              sin(alfa)
    x, y, z = round(x, 2), round(y, 2), round(z, 2)
    res = (x, y, z)

    if not esX_Origen:
       res = (y, x, z) 

    return res

def dist(P, P1):
    return P1 - P

def normalizaVector(V):
    return V / norm(V)

v, NEGRO, BLANCO, PANTALLA, ptoCam, posO = 5,\
            (0, 0, 0), (255, 255, 255), set_mode((300, 300)),\
            [[0, 0, 0], [0, 0, 0]], array([2, 0, 0])
posCam, rotCam = array(ptoCam)

dist = dist(posCam, posO)
d = normalizaVector(dist)

print("\n", "d =", d)

def imprimePtoCam():
    posCam, rotCam = ptoCam
    alfa, beta, gamma = rotCam

    print("\nptoCam =", ptoCam, ", n =",\
          ptoEsferaUnidad(alfa, beta))

#pixel(PANTALLA, 150, 150, BLANCO)
init()
update()
imprimePtoCam()

while True:
    posCam, rotCam = ptoCam
    alfa, beta, gamma = rotCam
    
    PANTALLA.fill(NEGRO)
    
    for e in get():
        pass
    
    ent = input("\nqe/zc\n") # TODO: +- para ajustar v

    if ent in "qezc":  
        if ent == "q":
            alfa -= v

        elif ent == "e":
            alfa += v
        
        elif ent == "z": 
            beta -= v
        
        elif ent == "c": 
            beta += v

        rotCam = [alfa, beta, gamma]
        ptoCam = posCam, rotCam

        imprimePtoCam()
        
