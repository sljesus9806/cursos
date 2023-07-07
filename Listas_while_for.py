listacompra = []
inusuario= None
respuesta= None
x = None

print('Programa lista de compra\n')

while respuesta != 'No':
   
   
    print('deseas agregar algo a la lista?\n ' )
    respuesta = input('Si o No: ')
   
   
    if respuesta != 'No':
        print('Que deseas agregar a la lista de compra?\n ')
        inusuario = input()
        
        
        if inusuario in listacompra:
            print('Este articulo ya esta en la listaa, seguro que quieres agregar este articulo? S/n')
            if input() == 'S':
                listacompra.append(inusuario)
            
        else:
            listacompra.append(inusuario)     
        
    
print('Esta es tu lista de compra: ')  
for item in listacompra:
     print(item)
    
    

    