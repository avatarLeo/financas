from flask import session
from banco.banco import Banco

from functools import wraps

def check_logged_in(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		if 'user' in session:
			return func(*args, **kwargs)
		return 'you are not logged in'
	return wrapper

def check_user(email, senha):
	db = Banco()
	cursor = db.get_db()
	sql = """SELECT cpf FROM usuario WHERE email=? and senha=?;"""
	valor = cursor.execute(sql, (email, senha))
	return valor.fetchall()
