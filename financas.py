from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login')
def login() -> 'html':
	return render_template('formulario_login.html', the_title='Finanças')

@app.route('/login.php', methods=['post'])
def bemvindo() -> 'html':
	email = request.form['email']
	senha = request.form['senha']
	return render_template('bemvindo.html', the_title='Finanças', email=email, senha=senha)

app.run()
