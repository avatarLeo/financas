from flask import Flask, render_template, request, session
from banco.banco import Banco

app = Flask(__name__)
app.secret_key = 'ksfjgne537hbigw97rtymsgu4'

@app.route('/login')
def login() -> 'html':
	return render_template('formulario_login.html', the_title='Finanças')

@app.route('/cadastro')
def cadastro() -> 'html':
	return render_template('formulario_cadastro.html', the_title='Finanças')

@app.route('/salvar', methods=['post'])
def salvar():
	dados = []
	for k, v in request.form.items():
		dados.append(v)

	db = Banco()
	db.insert(dados=dados)	

	return '<h2>Dados salvos com sucesso!</h2>'



app.run()
