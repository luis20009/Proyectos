from flask import Flask, render_template, request, redirect, url_for, flash,session, make_response
import json
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'clave_secreta'
app.config['SESSION_TYPE'] = 'filesystem'

# Ruta de la base de datos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "usuarios.db")

# Función para conectar a la base de datos
def conectar():
    return sqlite3.connect(DB_PATH)

# Crear la tabla si no existe
def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT NOT NULL UNIQUE
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tareas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        categoria TEXT NOT NULL,
        descripcion TEXT NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
    )
    """)
    conexion.commit()
    conexion.close()

# Llama a la función para crear la tabla al iniciar la aplicación
crear_tabla()


# Ruta principal para mostrar el formulario
@app.route('/')
def formulario():
    return render_template('formulario.html')

# Ruta para manejar el registro de usuarios
@app.route('/registrar', methods=['POST'])
def registrar():
    nombre = request.form.get('nombre')
    correo = request.form.get('correo')

    # Validar que los campos no estén vacíos
    if not nombre or not correo:
        flash("El nombre y el correo son obligatorios")
        return redirect(url_for('formulario'))

    # Conectar a la base de datos y verificar si el correo y el nombre ya existen juntos
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE correo = ?", (correo,))
        correo_repetido = cursor.fetchone()

        cursor.execute("SELECT * FROM usuarios WHERE nombre = ?", (nombre,))
        nombre_repetido = cursor.fetchone()
        if correo_repetido and nombre_repetido:
            flash("El nombre y el correo estan repetidos","error")
            return redirect(url_for('formulario'))
        elif correo_repetido:
            flash("El correo esta repetido","error")
            return redirect(url_for('formulario'))
        elif nombre_repetido:
            flash("El nombre esta repetido","error")
            return redirect(url_for('formulario'))
        else:
            # Si el usuario no está registrado, agregarlo a la base de datos
            cursor.execute("INSERT INTO usuarios (nombre, correo) VALUES (?, ?)", (nombre, correo))
            conexion.commit()
            flash(f"¡Bienvenido, {nombre}! Te has registrado exitosamente","success") 
            return redirect(url_for('formulario'))
    finally:
        conexion.close()
@app.route('/usuarios')
def mostrar_usuarios():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, correo FROM usuarios")
    usuarios = cursor.fetchall()
    conexion.close()

    # Renderiza una plantilla HTML para mostrar los usuarios
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/login', methods=['GET'])
def mostrar_login():
    return render_template('inicio.html')
@app.route('/login', methods=['POST'])
def login():
    nombre = request.form.get('nombre')
    correo = request.form.get('correo')

    # Validar que los campos no estén vacíos
    if not nombre or not correo:
        flash("El nombre y el correo son obligatorios")
        return redirect(url_for('formulario'))

    # Conectar a la base de datos y verificar si el correo y el nombre ya existen juntos
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE correo = ? AND nombre = ?", (correo,nombre))
        usuario_full = cursor.fetchone()
        if usuario_full:
            session['usuario_id'] = usuario_full[0]
            flash(f"¡Bienvenido de nuevo {nombre}!","success") 
            return redirect(url_for('mostrar_homework'))
            
        else:
            flash("El nombre y el correo no coinciden", "error")
            return redirect(url_for('mostrar_login'))
            
    finally:
        conexion.close()
@app.route('/homework', methods=['GET', 'POST'])
def mostrar_homework():
    # Verificar si el usuario ha iniciado sesión
    usuario_id = session.get('usuario_id')
    if not usuario_id:
        flash("Debes iniciar sesión para acceder a esta página", "error")
        return redirect(url_for('mostrar_login'))

    # Si el método es POST, procesar el formulario para agregar una nueva tarea
    if request.method == 'POST':
        categoria = request.form.get('categoria')
        descripcion = request.form.get('descripcion')

        # Validar que los campos no estén vacíos
        if not categoria or not descripcion:
            flash("Todos los campos son obligatorios", "error")
            return redirect(url_for('mostrar_homework'))

        # Guardar la tarea en la base de datos
        conexion = conectar()
        try:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO tareas (usuario_id, categoria, descripcion) VALUES (?, ?, ?)",
                           (usuario_id, categoria, descripcion))
            conexion.commit()
            flash("Tarea agregada exitosamente", "success")
        finally:
            conexion.close()

    # Obtener las tareas del usuario desde la base de datos
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT categoria, descripcion FROM tareas WHERE usuario_id = ?", (usuario_id,))
        tareas = cursor.fetchall()
        print(tareas)
    finally:
        conexion.close()

    # Renderizar la plantilla con las tareas del usuario
    return render_template('tareas.html', tareas=tareas)
@app.route('/logout')
def logout():
    session.pop('usuario_id', None)
    flash("Has cerrado sesión exitosamente", "success")
    return redirect(url_for('mostrar_login'))

@app.route('/homewor_users')
def mostrar_husers():
    usuario_id = session.get('usuario_id')
    try:
     conexion = conectar()
     cursor = conexion.cursor()
     cursor.execute("SELECT categoria, descripcion FROM tareas WHERE usuario_id = ?", (usuario_id,))
     usuariosn = cursor.fetchall()
    finally:
     conexion.close()

    # Renderiza una plantilla HTML para mostrar los usuarios
    return render_template('tareas_full.html', tareas=usuariosn)

@app.route('/eliminar_tarea', methods=['POST'])
def eliminar_tarea():
    # Obtener los datos enviados desde el formulario
    categoria = request.form.get('categoria')
    descripcion = request.form.get('descripcion')
    usuario_id = session.get('usuario_id')

    # Verificar que el usuario haya iniciado sesión
    if not usuario_id:
        flash("Debes iniciar sesión para realizar esta acción", "error")
        return redirect(url_for('mostrar_login'))

    # Conectar a la base de datos y eliminar la tarea
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "DELETE FROM tareas WHERE usuario_id = ? AND categoria = ? AND descripcion = ?",
            (usuario_id, categoria, descripcion)
        )
        conexion.commit()
        flash("Tarea eliminada exitosamente", "success")
    finally:
        conexion.close()

    return redirect(url_for('mostrar_homework'))
@app.route('/eliminar_users', methods=['POST'])
def eliminar_users():
    # Obtener los datos enviados desde el formulario
    nombre = request.form.get('nombre')
    correo = request.form.get('correo')
    

    # Verificar que el usuario haya iniciado sesión
    if not id:
        flash("Debes iniciar sesión para realizar esta acción", "error")
        return redirect(url_for('mostrar_login'))

    # Conectar a la base de datos y eliminar la tarea
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute(
            "DELETE FROM usuarios WHERE nombre= ? AND correo = ?",
            (nombre, correo)
        )
        conexion.commit()
        flash("Usuario eliminado exitosamente", "success")
    finally:
        conexion.close()

    return redirect(url_for('mostrar_login'))
@app.route("/buscar_tarea", methods=['GET'])
def buscar_tarea():
    usuario_id = session.get('usuario_id')
    query= request.args.get('query')
    conexion=conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("""
                    SELECT categoria, descripcion 
                    FROM tareas 
                    WHERE usuario_id = ? AND (categoria LIKE ? OR descripcion LIKE ?)
        """, (usuario_id, f"%{query}%", f"%{query}%"))
        tareas = cursor.fetchall()
        print(tareas)
    finally:
        conexion.close()
    return render_template('tareas_full.html', tareas=tareas)

@app.route('/exportar_tareas', methods=['GET'])
def exportar_tareas():
    usuario_id = session.get('usuario_id')
    if not usuario_id:
        flash("Debes iniciar sesión para realizar esta acción", "error")
        return redirect(url_for('mostrar_login'))

    # Obtener las tareas del usuario desde la base de datos
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT categoria, descripcion FROM tareas WHERE usuario_id = ?", (usuario_id,))
        tareas = cursor.fetchall()
    finally:
        conexion.close()

    # Convertir las tareas a formato JSON
    tareas_json = [{"categoria": tarea[0], "descripcion": tarea[1]} for tarea in tareas]

    # Crear una respuesta para descargar el archivo JSON
    response = make_response(json.dumps(tareas_json, indent=4))
    response.headers['Content-Type'] = 'application/json'
    response.headers['Content-Disposition'] = 'attachment; filename=tareas.json'
    return response


@app.route('/importar_tareas', methods=['POST'])
def importar_tareas():
    usuario_id = session.get('usuario_id')
    if not usuario_id:
        flash("Debes iniciar sesión para realizar esta acción", "error")
        return redirect(url_for('mostrar_login'))

 

    archivo = request.files['archivo']
 

    # Leer el archivo JSON
    try:
        tareas = json.load(archivo)
    except Exception as e:
        flash("El archivo no tiene un formato válido", "error")
        return redirect(url_for('mostrar_homework'))

    # Insertar las tareas en la base de datos
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        for tarea in tareas:
            categoria = tarea.get('categoria')
            descripcion = tarea.get('descripcion')
            if categoria and descripcion:
                cursor.execute("INSERT INTO tareas (usuario_id, categoria, descripcion) VALUES (?, ?, ?)",
                               (usuario_id, categoria, descripcion))
        conexion.commit()
        flash("Tareas importadas exitosamente", "success")
    finally:
        conexion.close()

    return redirect(url_for('mostrar_homework'))
if __name__ == '__main__':
    app.run(debug=True)
# Ruta para mostrar los usuarios registrados
