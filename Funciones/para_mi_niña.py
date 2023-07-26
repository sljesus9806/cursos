import random 


def mood(sentir):
    otra = 'Si'
    if sentir == 'Triste':
        
          
        while otra == 'Si':
            fsecreta = random.randint(0,7)
            print('Ay mi vida hermosa, no te preocupes chula vamos a recargarte esos animos \n')
            ltriste = ['En el gran caos del infinito, tu existencia es la coincidencia a la que yo llamaría milagro\n',
                   'Sonríe, un Leo siempre encuentra la forma de salir adelante\n',
                   'Dios era el unico que hacía milagros, hasta que  su oponente fue tu sonrisa\n',
                   'he visto de lo que eres capaz y en verdad estoy orgulloso de ti\n',
                   'te amo sin sus letras, pues lo mio es un sentimiento que no cabe dentro de ellas\n',
                   'si, eres perfecta incluso con tus errores y con tus imperfecciones, si fueses perfecta Dios tendría envidia\n',
                   'No todo depende de ti, haces siempre lo que puedes y das lo mejor de ti, eso es lo que más valoro de ti\n',
                   'Llorar un poco...Listo! , levantarme...Listo!, Sacudirme el polvo...Listo! Y seguir adelante.....Te amo mi amor\n']
            print(ltriste[fsecreta])

            otra = input('Amor te gustaría otra frase? Si/No: ')
        print('Espero haberte hecho sentir mejor mi vida, te amo!')    
    elif sentir == 'Feliz':
        
        print('Esoooooom mi amooooor eres fantastica, en verdad no sabes cuanto te amo corazón me alegra mucho verte feliz ')
    
    elif sentir == 'Angustiada':


        while otra == 'Si':        
            fsecreta = random.randint(0,3)
            langustiada = ['Todo estara bien mi amorita, yo siempre estaré a tu lado','AMOR eres Leo, el miedo o angustia siempre los superan','eres perfecta mi amor no temas todo estará bien\n',
                       'animo bebé recuerda quien eres, de donde vienes y recuerda todo aquello que has superado, estoy orgulloso de ti\n',
                       'Chula, hermosa, increible, talentosa, fuerte, perseverante, capaz, obstinada, inteligente, perseverante, son algunas cuantas de las caracteristicas que te definen preciosa\n',
                       'Llorar un poco...Listo! , levantarme...Listo!, Sacudirme el polvo...Listo! Y seguir adelante.....Te amo mi amor\n']
            print(langustiada[fsecreta])
            otra = input('Amor te gustaría otra frase? Si/No: ')
        print('Espero haberte hecho sentir mejor mi vida, te amo!')



respuesta = input('Hola mi amor como te sientes el dia de hoy? Triste/Feliz/Angustiada: ')

if __name__== '__main__':
    mood(respuesta)

