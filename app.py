from flask import Flask, render_template, request, redirect, url_for,flash
from flaskext.mysql import MySQL 

app = Flask (__name__)
app.secret_key = "mensaje"
mysql = MySQL()

app.config['MYSQL_DATABASE_DB'] = 'rojisDB'
app.config['MYSQL_DATABASE_USER'] = 'edgargc'
app.config['MYSQL_DATABASE_PASSWORD'] = 'taringa07'
app.config['MYSQL_DATABASE_HOST'] = '172.19.0.1'
app.config['MYSQL_DATABASE_PORT'] = '3306'

mysql.init_app(app)

@app.route('/')
def index():

    conexion = mysql.connect()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM estudiante")
    resultado = cursor.fetchall()

    return render_template('index.html')

""" @app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Datos insertados correctamente") 
        matricula = request.form['matricula']
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        carrera = request.form['carrera']

         conexion = mysql.connect()
        cursor = conexion.cursor()
        conexion.close()
        return 'agregado' 

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO estudiante (matricula, nombre, telefono, carrera) VALUES(%s, %s, %s, %s)", (matricula, nombre, telefono, carrera))
        mysql.connection.commit()
        return redirect(url_for('index')) """

""" @app.route('/delete/<string:id_data>', methods =['GET'])
def delete(id_data):
    flash("El alumno ha sido eliminado")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM estudiante WHERE matricula= %s",(id_data))
    mysql.connection.commit()
    return redirect(url_for('index)) """

app.run(host= '0.0.0.0', debug = True)

""" docker run -it -w /app -v //home/edgargc/docker:/app -p 8086:5000 edgargc/proyecto01:teco bash
 """