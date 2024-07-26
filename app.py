from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'sql5.freesqldatabase.com'
app.config['MYSQL_USER'] = 'sql5722384'
app.config['MYSQL_PASSWORD'] = 'LmPeGiVjv1'
app.config['MYSQL_DB'] = 'sql5722384'

mysql = MySQL(app)

#Prueba
@app.route('/datos', methods=['GET'])
def obtener_datos():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM pregunta''')
    datos = cur.fetchall()
    cur.close()
    return jsonify(datos)

#Login
@app.route('/login', methods=['POST'])
def login():
    # Obtiene el username y password del cuerpo de la solicitud
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'mensaje': 'Usuario y contraseña requeridos.', 'exito': False})

    try:
        cursor = mysql.connection.cursor()
        # Consulta para verificar el username y password
        sql = "SELECT nombre FROM usuario WHERE username = %s AND password = %s"
        cursor.execute(sql, (username, password))
        datos = cursor.fetchone()

        if datos:
            return jsonify({'nombre': datos[0], 'mensaje': 'Inicio de sesión exitoso.', 'exito': True})
        else:
            return jsonify({'mensaje': 'Credenciales incorrectas.', 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': 'Error en el servidor.', 'exito': False})

if __name__ == '__main__':
    app.run(debug=True)
