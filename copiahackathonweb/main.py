from flask import Flask, render_template             
import ast

app = Flask(__name__)
@app.route("/")
def index2():
    archivo=open('hola.txt','r')
    mensaje=archivo.read()
    print(mensaje)
    diccionario=ast.literal_eval(mensaje) #convertimos a diccionario
    return render_template("index2.html",msg = diccionario)
    

#Bucle principal del programa, lee el sensor. Se sale con CTRL+C
if __name__ == "__main__":
    app.run(debug=True)
    #subprocess.popen(["python3","ultra.py"])
