from math import sin, cos, radians

def ptoEsferaUnidad(alfa, beta):
    '''
    OBJ: convierte coordenadas esfericas a rectangulares.
    alfa, beta en grados sexagesimales -> x, y, z
    formula obtenida a partir de las proyecciones vertical y horizontal
    calcula el punto o vector d sobre la esfera unidad
    '''
    alfa, beta = radians(alfa), radians(beta)
    x, y, z = cos(alfa) * cos(beta), sin(beta) * cos(alfa), sin(alfa)

    return (round(x, 2), round(y, 2), round(z, 2))
    
#PROBADOR
print(ptoEsferaUnidad(alfa = 45, beta = 45))

