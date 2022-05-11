# Import libraries
import theano
from theano import tensor
# Creando dos escalares de punto flotante
a = tensor.dmatrix()
b = tensor.dmatrix()
# Creando una expresión de adición
c = a + b
# Convertir la expresión en un objeto llamable que tome los valores (a,b) como entrada y calcule un valor para c
fun = theano.function([a, b], c)
# Llamada a la función
print(fun([[1, 2], [3, 4]], [[1, 2], [3, 4]]))