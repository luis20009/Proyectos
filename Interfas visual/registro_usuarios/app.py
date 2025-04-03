from flask import Flask, render_template, request, redirect, url_for, flash
from db_manager import conectar, registrar_persona
import re
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/registro', methods=['POST'])
def registro():
    """Verificacion de usuario válido."""

    # Obtener datos del formulario
    username = request.form.get('username')

    conexion = conectar()
    cursor = conexion.cursor()
    # Consulta para verificar si el username existe
    cursor.execute("SELECT EXISTS(SELECT 1 FROM usuarios WHERE username = ?)", (username,))
    existe = cursor.fetchone()[0]
    if existe:
        flash(f"El usuario {username} ya se encuentra registrado.\nPor favor, ingresa otro nombre de usuario","error")
        return redirect(url_for('index'))
    
    
    #Registar persona en la base de datos
    registrar_persona(username,)
    flash("Usuario registrado con éxito", "success")
    return redirect(url_for('index'))

@app.route('/list_users')
def list_users():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conexion.close()
    return render_template('users.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)