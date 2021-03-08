import sqlite3

connection = sqlite3.connect('../db/rbc_planetas.db')
c = connection.cursor()
#SQL
def create_table():
	c.execute("CREATE TABLE IF NOT EXISTS'planeta' (\
	'id'	INTEGER,\
	'nome'	text,\
	'ESI'	INTEGER,\
	'SPH'	REAL,\
	'HZD'	INTEGER,\
	'HZC'	REAL,\
	'HZA'	REAL,\
	'pClass'	INTEGER,\
	'habitalidade'	INTEGER,\
	PRIMARY KEY('id' AUTOINCREMENT)\
  	)");


create_table()

def data_insert(nome, ESI,SPH, HZD, HZC, HZA, pClass, habitalidade):
	c.execute("INSERT INTO 'planeta' (nome, ESI, SPH, HZD, HZC, HZA, pClass, habitalidade) VALUES (?,?,?,?,?,?,?,?)", 
		(nome, ESI, SPH, HZD, HZC, HZA, pClass, habitalidade))
	connection.commit()
	print("valores inseridos")
	

def data_read():
	array = [] 
	sql = "SELECT * FROM planeta"
	for row in c.execute(sql):
		array.append(row)
	return array

def delete_data(param, value):
	sql = "DELETE FROM planeta WHERE %s = ?"%(param)
	c.execute(sql,(value, ))
	connection.commit()
	print("planeta deletado")

def data_update(nome, ESI, SPH, HZD, HZC, HZA, pClass, habitalidade, id):
	sql = "UPDATE'planeta' SET nome = ? ESI = ?, SPH = ?, HZD = ?, HZC = ?, HZA = ?, pClass = ?, habitalidade = ? WHERE id = ?"
	data = (nome, ESI, SPH, HZD, HZC, HZA, pClass, habitalidade, id)
	c.execute(sql, data)
	connection.commit()
	print("planeta alterado")