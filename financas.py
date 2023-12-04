from flask import Flask, render_template, request, session
from banco.banco import Banco
from checker import check_logged_in, check_user

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


@app.route('/autenticar', methods=['post'])
def autenticar() -> 'html':
	cpf = check_user(request.form['email'], request.form['senha'])
	
	if len(cpf) > 0:
		session['user'] = cpf[0][0]
		return render_template('home.html')
	return '<h1>Email ou senha estão incorretos</h1>'

app.run(debug=True)
