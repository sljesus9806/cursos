print('la mazmorra de abadur')

print('///////////////////////')

print('Hola viajero haz caido en la mazmorra de abadur, tienes solo 5 minutos para escapar\n')

print('para tomar el camino correcto debes solucionar la siguiente operacion \n '
      'si respondes correctamente la puerta se abrira ')
r = int(input('1+1 es igual a: '))

if r == 2:
    print('perfecto eres muy inteligente pasaras a la salida...\n  '
          'o mira alguien se ha dejado una escopeta explosiva mata trolss 3000 super delux\n'
          'creo que deberias tomarla tio')
    s = input('para tomarla presiona "y" para no tomarla presiona "n": ')
    if s == 'n':
        print('tio....creo que deberias tomarla')
        s = input('tomar o no: ')
        if s == 'y':
            print('bien hecho, con esta arma has asesinado a Abadur el troll y has logrado escapar bien hecho!')
            print('fin!')

        else:
            print('no tio en serio....DEBERIAS TOMARLA')
            s = input('tomar o no: ')
            if s == 'n':
                print('serÃ¡s idi...... que te den')
                print('haz avanzado a la salida sin el arma, abadur el troll destructor amante del bondage te estÃ¡ esperando\
                tio te he dicho que tomaras esa arma.........')
                print('fin...')
            else:
                print('bien hecho, con esta arma has asesinado a Abadur el troll y has logrado escapar bien hecho!')
                print('fin!')
    else:
        print('bien hecho, con esta arma has asesinado a Abadur el troll y has logrado escapar bien hecho!')
        print('fin!')
else:
    print('vale tio si no sabes cuanto es 1 + 1 no creo que puedas sobrevivir mucho, has muerto, fin....')
    