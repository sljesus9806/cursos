'''programa uno'''
"""###Crea un programa que seleccione un texto del usuario, por ejemplo “Hola me llamo Nate, ¿tú cómo te llamas?”  que busque y señale cuántos espacios, puntos y comas existen en la frase."""
tusuario = None
espacios = 0
puntos = 0
comas = 0

print('Hola digita un texto el que quieras: \n')
tusuario=list(input())


for c in tusuario:
    if c == ' ' :
        espacios += 1
    elif c == '.':
        puntos += 1
    elif c == ',':
        comas += 1

print(f'tu texto tiene {espacios} espacios, tiene {puntos} puntos, tiene {comas} comas.')


'''Programa dos'''
'''Crea un programa que cuente cuantas mayúsculas tiene un texto introducido por el usuario.'''


mayusculas = 0
inusuario = None

print('Digita un texto con mayusculas y minusculas por favor ')
inusuario= input()

for c in inusuario:
    if c.isupper() == True:
        mayusculas += 1
        
print(f'tu texto tiene {mayusculas} mayusculas')


'''Programa tres'''

"""Crea un programa que cree la tabla de multiplicar de cualquier número que indique el usuario.
Escribe el código que te permita obtener los resultados esperados y recuerda no mirar la solución antes 🤓###"""  

r = 0
t = 0

print('Cual tabla de multiplicar quieres? ')
t = int(input())

for m in range (0,11):
    
    r = m * t
    print(f'{m} multiplicado por {t} = {r}')
