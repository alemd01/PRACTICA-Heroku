from flask import Flask, render_template,request,abort
from lxml import etree
import os
libros = etree.parse('libros.xml')
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

@app.route("/libro/<num1>",methods=["GET","POST"])
def busca_libros(num1):
	codigo = libros.xpath('//codigo/text()')
	for n in range(0,len(codigo)):
	   if num1 == codigo[n]:
	      tit = libros.xpath('//codigo[. ="%s"]/../titulo/text()' % num1)
	      aut = libros.xpath('//codigo[. ="%s"]/../autor/text()' % num1)
	      return render_template("libro.html",titulo=tit[0],autor=aut[0])
	      break
	return abort(404)
port=os.environ["PORT"]
app.run("0.0.0.0",int(port),debug=True)
