from math import sin, cos, radians

def ptoEsferaUnidad(alfa, beta, esX_Origen = True):
    '''
    OBJ: Convierte coordenadas esfericas a rectangulares.
    alfa, beta en grados sexagesimales -> x, y, z
    Formula obtenida a partir de las proyecciones vertical y
    horizontal. Calcula el punto o vector d sobre la esfera unidad

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
    
alfa, beta, v = 0, 0, 5

while True:
    ent = input("\nqe/ad\n")

    if ent in "qead": 
        if ent == "q":
            alfa -= v

        elif ent == "e":
            alfa += v
        
        elif ent == "a":
            beta -= v
        
        elif ent == "d":
            beta += v

        print("\nalfa =", alfa, ", beta =", beta,\
              ", d =", ptoEsferaUnidad(alfa, beta))

        
