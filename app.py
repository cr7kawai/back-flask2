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

@app.route('/datos', methods=['GET'])
def obtener_datos():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM usuario''')
    datos = cur.fetchall()
    cur.close()
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True)
