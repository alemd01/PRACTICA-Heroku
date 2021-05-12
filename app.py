from flask import Flask, render_template,request
app = Flask(__name__)	


@app.route('/')
def inicio():
	return render_template("base.html")

@app.route("/potencia/<int:op1>/<int:op2>",methods=["GET","POST"])
def potencia(op1,op2):
	if op2 > 0:
	   res = pow(op1,op2)
	
	elif op2 == 0:
	   res = 1
	
	elif op2 < 0:
	   pos = abs(op2)
	   res = 1/pow(op1,pos)
	
	return render_template("potencia.html",num1=op1,num2=op2,resultado=res)

@app.route("/cuenta/<num1>/<num2>",methods=["GET","POST"])
def cuentas(num1,num2):
	acum=0
	for a in range(0,len(num1)):
	   if num2 == num1[a]:
	      acum=acum+1
	return render_template("cuenta.html",op1=num1,op2=num2,resul=acum)

@app.route("/libro")
def libros():
	return render_template("libro.html")
app.run("0.0.0.0",5555,debug=True)
