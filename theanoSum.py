# Import libraries
import theano
from theano import tensor
# Creando dos escalares de punto flotante
x = tensor.dscalar()
y = tensor.dscalar()
# Creando una expresión de adición
z = x + y
# Convierte la expresión en un objeto llamable que toma los valores (x,y) como entrada y calcula un valor para z
fun = theano.function([x, y], z)
# llamar a la función una prueba e imprimir el resultado
print(fun(11.6, 1.1))
