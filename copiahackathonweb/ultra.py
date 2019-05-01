import time #se necesita para usar las funciones de tiempo
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BOARD) 
disparador1 = 3
Eco1 = 5
disparador2 = 38
Eco2 = 40
 
#Hay que configurar ambos pines del HC-SR04
GPIO.setup(disparador1, GPIO.OUT)
GPIO.setup(Eco1, GPIO.IN)
GPIO.setup(disparador2,GPIO.OUT)
GPIO.setup(Eco2,GPIO.IN)
 
def detectar_lugar1():
 
   GPIO.output(disparador1, False) #apagamos el pin Trig
   time.sleep(2*10**-6) #esperamos dos microsegundos
   GPIO.output(disparador1, True)#encendemos el pin Trig
   time.sleep(10*10**-6) #esperamos diez microsegundos
   GPIO.output(disparador1, False)#y lo volvemos a apagar
 
  #empezaremos a contar el tiempo cuando el pin Echo se encienda
   while GPIO.input(Eco1) == 0:
      start_1 = time.time()
 
   while GPIO.input(Eco1) == 1:
      end_1 = time.time()
      
   #La duracion del pulso del pin Echo sera la diferencia entre
   #el tiempo de inicio y el final
   duracion_1 = end_1-start_1
 
   #Este tiempo viene dado en segundos. Si lo pasamos
   #a microsegundos, podemos aplicar directamente las formulas
   #de la documentacion
   duracion1 = duracion_1*10**6
   medida1 = duracion1/58#hay que dividir por la constante que pone en la documentacion, nos dara la distancia en cm
   return medida1
    #por ultimo, vamos a mostrar el resultado por pantalla
def detectar_lugar2():
   GPIO.output(disparador2, False) #apagamos el pin Trig
   time.sleep(2*10**-6) #esperamos dos microsegundos
   GPIO.output(disparador2, True)#encendemos el pin Trig
   time.sleep(10*10**-6) #esperamos diez microsegundos
   GPIO.output(disparador2, False)#y lo volvemos a apagar
 
  #empezaremos a contar el tiempo cuando el pin Echo se encienda
   while GPIO.input(Eco2) == 0:
      start_2 = time.time()
 
   while GPIO.input(Eco2) == 1:
      end_2 = time.time()
      
   #La duracion del pulso del pin Echo sera la diferencia entre
   #el tiempo de inicio y el final
   duracion_2 = end_2-start_2
 
   #Este tiempo viene dado en segundos. Si lo pasamos
   #a microsegundos, podemos aplicar directamente las formulas
   #de la documentacion
   duracion2 = duracion_2*10**6
   medida2 = duracion2/58 #hay que dividir por la constante que pone en la documentacion, nos dara la distancia en cm
   return medida2
#Bucle principal del programa, lee el sensor. Se sale con CTRL+C


while True:
   try:
      d1=detectar_lugar1()
      d2=detectar_lugar2()
      with open('hola.txt','w') as archivo:
         formato="{'sensor1': " + str(d1) + ", 'sensor2':" + str(d2) + "}"
         archivo.write(formato)  #guardar distancias
         #archivo.write('\n')
      if d1>=14:
         print("libre espacio 1")
      
      else:
         print("ocupado espacio 1")
      if 14<=d2:
         print("libre espacio 2")
      else:
         print("ocupado espacio 2")
      time.sleep(2)
      
   except KeyboardInterrupt:
      break

