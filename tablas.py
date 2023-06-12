import sqlite3

def create_tables():
    nombre_db = 'datos'

    #Conexion a la base de datos
    db = sqlite3.connect(nombre_db)

    #Definimos el cursor
    cursor = db.cursor()

    #Creamos als tablas
    cursor.executescript(
    '''
        CREATE TABLE IF NOT EXISTS Admin(
            Username TEXT PRIMARY KEY,
            Password TEXT
        );

        CREATE TABLE IF NOT EXISTS Company(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Company_name TEXT,
            Company_api_key TEXT
        );

        CREATE TABLE IF NOT EXISTS Location(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Company_ID INTEGER,
            Location_name TEXT,
            Location_country TEXT,
            Location_city TEXT,
            Location_meta TEXT
        );

        CREATE TABLE IF NOT EXISTS Sensor(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Location_ID INTEGER,
            Sensor_name INTEGER,
            Sensor_category TEXT,
            Sensor_meta TEXT,
            Sensor_api_key TEXT
        );

        CREATE TABLE IF NOT EXISTS Sensor_data(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            F INTEGER,
            T INTEGER
        )
    '''
    )



    cursor.executescript('''INSERT OR IGNORE INTO Admin(Username, Password) VALUES ('lukas', '123');''')
    cursor.executescript('''INSERT OR IGNORE INTO Admin(Username, Password) VALUES ('gabriel', '123');''')  
    cursor.executescript('''INSERT OR IGNORE INTO Sensor_data(ID,F,T) VALUES (0,0,0);''')


    db.commit()
    db.close()
