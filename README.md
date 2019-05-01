# Hackathon_web
# Instrucciones para el funcionamiento del sistema
1. Correr el archivo ultra.py
2. Correr el servidor de flask, moverte al directorio donde se encuentra el archivo principal de flask
3. Una vez en el directorio del archivo principal de flask, introducir el siguiente comando:
```bash
export FLASK_APP= main.py

```
4. Ahora correr el servidor 
```bash
flask run  --host= ip_raspberry_pi

```
5. Acceder al navegador con la siguiente url: 

```
ip_raspberry_pi: 5000

```


# Tutores Claves: Willi Bobadilla @WilliBobadilla, Lorena Zalazar @Lorelulen y Mauro Gavilan @mauroot
# Objetivo:
       En el presente archivo se intentara realizar una pagina web para el monitoreo de vacancias 
        de estacionamientos funcional en un local determinado utilizando raspberry, que responda en
        una web basica diseñada por nosotros
# Diseño:
       Se necesitaran  por lugar de estacionamiento  1 sensor de ultrasonido, que estaran conectados
       a una misma raspberry pi, que correra una pagina web para el contacto con el cliente sobre
       la disponibilidad del estacionamiento
# Consideraciones:
      1)Para la consideracion de lugares vacios con los sensores de ultrasonidos, se tomara la 
        distancia de 1.95 metros como vacion (teniendo la altura real de piso a techo en el estacionamiento
        de 2.10 metros). Otra medida recibida se tomara como espacio ocupado actualmente
      2)El dato sera enviado por la raspberry pi a la web que se correra en la misma
      3)El cliente recibira una pantalla que le indicara por lugar el estatus de cada estacionamiento de
      bateria dentro del local como ( texto libre+ mas color verde) o (texto ocupado + color rojo)
        
        
