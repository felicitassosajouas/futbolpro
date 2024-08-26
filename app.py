from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'futbolpro'
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/jugadores')
def jugadores():
    return render_template ('jugadores.html')

@app.route('/equipos')
def equipos():
    return render_template ('equipos.html')

@app.route('/iniciarsesion', methods=['POST'])
def iniciarsesion():
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        contrasena = request.form['contrasena']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuarios (fullname, email, contrasena) VALUES (%s, %s, %s)',(fullname, email, contrasena))
        mysql.connection.commit()
        flash('success')
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port = 3000, debug = True)