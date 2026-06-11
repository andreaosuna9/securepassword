from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generar_password(palabras):

    simbolos = ["@", "#", "$", "&", "!"]

    base = "".join(
        palabra.capitalize()
        for palabra in palabras
    )

    numero = str(random.randint(10, 99))
    simbolo = random.choice(simbolos)

    return f"{base}{numero}{simbolo}"


@app.route("/", methods=["GET", "POST"])
def verificador():

    sugerencias = []

    if request.method == "POST":

        palabras = request.form.get("palabras", "")

        lista_palabras = palabras.split()

        if len(lista_palabras) > 0:

            for i in range(4):

                sugerencias.append(
                    generar_password(lista_palabras)
                )

    return render_template(
        "index.html",
        sugerencias=sugerencias
    )


@app.route("/felicidades")
def felicidades():
    return render_template("felicidades.html")


if __name__ == "__main__":
    app.run(debug=True)