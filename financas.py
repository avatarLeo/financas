from flask import Flask, render_template, request, session, redirect
from banco.banco import Banco
from checker import check_logged_in, check_user

app = Flask(__name__)
app.secret_key = 'ksfjgne537hbigw97rtymsgu4'

@app.route('/financas.com')
def tela_inicial():
	return render_template('bemvindo.html')

@app.route('/login', methods=['get', 'post'])
def login() -> 'html':
	return render_template('login.html', the_title='Finanças')

@app.route('/cadastro')
def cadastro() -> 'html':
	return render_template('cadastroUser.html')

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
	dados = check_user(request.form['username'], request.form['password'])
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
	return render_template('index.html', user=dados[0][1])


@app.route('/despesas')
@check_logged_in
def despesas() -> 'html':
	db = Banco()
	dados = db.get_despesas((session['user']))
	return render_template('despesas.html', despesas=dados)


@app.route('/cadastrar_gastos')
@check_logged_in
def cadastrar_gastos():
	db = Banco()
	dados = db.get_user(session['user'])

	return render_template('cadastroGastos.html', user=dados[0][1])

@app.route('/salvar_gastos', methods=['post'])
@check_logged_in
def salvar_gastos():
	dados = []
	dados.append(session['user'])
	for k, v in request.form.items():
		dados.append(v)

	db = Banco()
	if db.salvar_despesas(dados=dados):
		return 'Dados salvos com sucesso!'
	return 'Ouve um erro'


@app.route('/editar_user')
@check_logged_in
def editar_user():
	db = Banco()
	dados = db.get_user(session['user'])

	return render_template('editarUser.html', user=dados[0][1])

@app.route('/logout')
@check_logged_in
def logoout():
	session.pop('logged_in')

	return 'Você esta deslogado'


app.run(debug=True)
