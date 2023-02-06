from flask import Flask, request, flash, url_for, redirect, render_template
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '2.2 Project'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

#Creating a connection cursor
with app.app_context():
    cursor = mysql.connection.cursor()

    #Executing SQL Statements
    cursor.execute(''' create table if not exists chicken(id int NOT NULL AUTO_INCREMENT, id_chicken int NOT NULL, timestamp DATETIME NOT NULL, temperature FLOAT, latitude varchar(45), longitude varchar(45), PRIMARY KEY(id))''')

    #Saving the Actions performed on the DB
    mysql.connection.commit()

    #Closing the cursor
    cursor.close()

    
    @app.route('/')
    def form():
        return render_template('index.html')

    @app.route('/login', methods = ['POST', 'GET'])
    def login():
        if request.method == 'GET':
            return "Login via the login Form"
        
        if request.method == 'POST':
            id_chicken = request.form['id_chicken']
            timestamp = datetime.now()
            temperature = request.form['temperature']
            latitude = request.form['latitude']
            longitude = request.form['longitude']
            cursor = mysql.connection.cursor()
            cursor.execute(''' INSERT INTO chicken(id_chicken, timestamp, temperature, latitude, longitude) VALUES(%s,%s, %s, %s, %s)''',
            (id_chicken,timestamp, temperature, latitude, longitude))
            mysql.connection.commit()
            cursor.close()
            return f"Done!!"

    @app.route('/data', methods = ['GET'])
    def data():
        if request.method == 'GET':
            id_chicken = request.args.get('id_chicken')
            timestamp = datetime.now()
            temperature = request.args.get('temperature')
            latitude = request.args.get('latitude')
            longitude = request.args.get('longitude')
            cursor = mysql.connection.cursor()
            cursor.execute(''' INSERT INTO chicken(id_chicken, timestamp, temperature, latitude, longitude) VALUES(%s,%s, %s, %s, %s)''',
            (id_chicken,timestamp, temperature, latitude, longitude))
            mysql.connection.commit()
            cursor.close()
            return f"Done!!"
    app.run(host='0.0.0.0', port=5000)