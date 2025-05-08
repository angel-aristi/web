# Escribe esta linea de codigo
print('Bienvenidos al entrnamiento con python, vamos a disfrutar al maximo esta sesion.')


'''
    Descueto en una compra:
    Si compras mas de $1000, obtienes un descuento del 20%
    Pide el monto de la compra y muestra el precio final
'''

# Pedir datos por teclado al usuario int entero float decimales str cadenas de caracteres bool boleanos

compra = float(input('Digite el valor de la compra: '))

# Si compar mas de $1000, obtienes un descuento del 20%
# Siempre que la salida tenga mas de un camino de resolucion, debo implementar condicionales

# Operadores combinados
# Operadores de asignacion = , Operadores aritmeticos +-*/ , operadores logicos and y, or o, not,
# Operadores de comparacion ==, !=, >, <, >=, <=

if compra < 1000:
    print('\n---------------------------------')
    print(f'El valor de tu compra es: {compra}')
    print('---------------------------------')
else:
    descuento = compra * 0.2
    compra_descuento = compra - descuento
    print('\n--------------------------------------------------------------------')
    print(f'El descuento es de ${descuento}, por lo tanto su valor a pagar es ${compra_descuento}')
    print('--------------------------------------------------------------------')


