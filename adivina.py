from flask import Flask, request
import random
app = Flask(__name__)

numeroAdivinar = random.randint(0, 100)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method=="POST":
        numero=request.form.get("numero")
        if int(numero)== int(numeroAdivinar):
            return "<p>El numero aleatorio es {}</p>".format(str(numeroAdivinar))
        else:
            return "<p>No has acertado</p>"
    else:
        return """<form  method="POST">
                <label>Numero:</label></br>
                <input type="number" name="numero"/><br/><br/>
                <input type="submit"/>
                </form>"""