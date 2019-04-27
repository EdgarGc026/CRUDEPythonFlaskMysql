from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL

app = Flask (__name__)
mysql = MySQL()


app.config['MYSQL_DATABASE_HOST'] = '172.19.0.1'
app.config['MYSQL_DATABASE_DB'] = 'rojisDB'
app.config['MYSQL_DATABASE_USER'] = 'edgargc026'
app.config['MYSQL_DATABASE_PASSWORD'] = 'taringa07'
mysql.init_app(app)

app.config ['SECRET_KEY'] = 'cocaCola' #Diccionario 

@app.route('/')
def index():
	conexion = mysql.connect()
	cursor = conexion.cursor()
	cursor.execute('SELECT * FROM estudiante')
	resultado = cursor.fetchall()
	return render_template('index.html', resultado =resultado)

#Aqui aplicamos el insertar los datos en la BD
@app.route('/insert', methods = ['POST'])
def insert():
    matricula = request.form['matricula']
    nombre = request.form['nombre']
    correo = request.form['correo']
    semestre = request.form['semestre']
    carrera = request.form['carrera']
    
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO estudiante (matricula, nombre, correo, semestre, carrera) VALUES(%s, %s, %s, %s, %s)", (matricula, nombre, correo, semestre, carrera))
    conexion.commit()
    return redirect(url_for('index'))

@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM estudiante WHERE matricula = %s", (id_data))
    conexion.commit()
    return redirect(url_for('index'))

@app.route('/update/', methods=['POST','GET'])
def update():
    if request.method == 'POST':
        id_data = request.form['matricula']
        nombre = request.form['nombre']
        correo = request.form['correo']
        semestre = request.form['semestre']
        carrera = request.form['carrera']
        
        conexion = mysql.connect()
        cursor = conexion.cursor()
        cursor.execute("UPDATE estudiante SET nombre = %s, correo = %s, semestre = %s, carrera = %s WHERE matricula = %s", (nombre, correo, semestre, carrera, id_data))
        conexion.commit()
        return redirect(url_for('index'))


app.run(host= '0.0.0.0', debug = True)
