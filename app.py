from flask import Flask, render_template,request
app = Flask(__name__)	


@app.route('/')
def inicio():
	return render_template("base.html")

@app.route("/potencia")
def potencia():
	return render_template("potencia.html")

@app.route("/cuenta")
def cuentas():
	return render_template("cuenta.html")

@app.route("/libro")
def libros():
	return render_template("libro.html")
app.run("0.0.0.0",5555,debug=True)
