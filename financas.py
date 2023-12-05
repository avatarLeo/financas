from flask import Flask, render_template, request, session, redirect
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
	dados = check_user(request.form['email'], request.form['senha'])
	
	if len(dados) > 0:
		session['logged_in'] = True
		session['user'] = dados[0][0]
		return redirect('/home')
	return '<h1>Email ou senha estão incorretos</h1>'

@app.route('/home')
@check_logged_in
def home() -> 'html':
	db = Banco()
	dados = db.get_user(session['user'])
	return render_template('home.html', cpf=dados[0][0], nome=dados[0][1], email=dados[0][2])


@app.route('/despesas')
@check_logged_in
def despesas() -> 'html':
	db = Banco()
	dados = db.get_despesas((session['user']))
	return render_template('despesas.html', nome=dados[0][1], despesas=dados[0][0])

@app.route('/logout')
def logoout():
	session.pop('logged_in')

	return 'Você esta deslogado'


app.run(debug=True)
