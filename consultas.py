import sqlite3
from key_generator.key_generator import generate

def comprobar_company_api_key(company_api_key):
    nombre_db = 'datos'
    con = sqlite3.connect(nombre_db)
    cur = con.cursor()
    res = cur.execute("select ID,company_api_key from Company")
    res=res.fetchall()
    for i in res:
        if i[1]==company_api_key:
            return i[0]
    return 'error'

def comprobar_admin(user,clave):
    nombre_db = 'datos'
    con = sqlite3.connect(nombre_db)
    cur = con.cursor()
    res = cur.execute("select Username,Password from Admin")
    res=res.fetchone()
    if res[0]==user and res[1]==clave:
        return True
    else:
        return False
    
def comprobar_sensor(sensor_api_key):
    nombre_db = 'datos'
    con = sqlite3.connect(nombre_db)
    cur = con.cursor()
    res = cur.execute("select Sensor_api_key from Sensor where Sensor_api_key='%s'"%sensor_api_key)
    res=res.fetchone()
    if res== None:
        return False
    else:
        return True


# Consultas de Locations


def obtener_locations(company_id):
    nombre_db = 'datos'
    con = sqlite3.connect(nombre_db)
    cur = con.cursor()
    res = cur.execute("select * from Location where company_id=%s"%company_id)
    res=res.fetchall()
    return res

def obtener_location(company_id,id):
    nombre_db = 'datos'
    con = sqlite3.connect(nombre_db)
    cur = con.cursor()
    res = cur.execute("select * from Location where company_id=%s and id=%s"%(company_id,id))
    res=res.fetchone()
    return res

def update_location(location_name,location_country,location_city,location_meta,company_id,id):
    nombre_db = 'datos'
    con = sqlite3.connect(nombre_db)
    cur = con.cursor()
    cur.execute("UPDATE Location SET location_name='%s' , location_country='%s',location_city='%s' ,location_meta='%s' WHERE company_id=%s and id=%s"%(location_name,location_country,location_city ,location_meta,company_id,id))
    con.commit()

def delete_location(company_id,id):
    nombre_db = 'datos'
    con = sqlite3.connect(nombre_db)
    cur = con.cursor()
    cur.execute("DELETE FROM Location WHERE company_id=%s and id=%s"%(company_id,id))
    con.commit()



# Consultas de sensores



def obtener_sensores(company_id):
    nombre_db = 'datos'
    con = sqlite3.connect(nombre_db)
    cur = con.cursor()
    res = cur.execute("select Sensor.ID,Sensor.Location_ID,Sensor.Sensor_name,Sensor.Sensor_category,Sensor.Sensor_meta,Sensor.Sensor_api_key from Sensor inner join location on Sensor.Location_ID=location.ID where Location.Company_ID=%s;"%company_id)
    res=res.fetchall()
    return res

def obtener_sensor(company_id,id):
    nombre_db = 'datos'
    con = sqlite3.connect(nombre_db)
    cur = con.cursor()
    res = cur.execute("select Sensor.ID,Sensor.Location_ID,Sensor.Sensor_name,Sensor.Sensor_category,Sensor.Sensor_meta,Sensor.Sensor_api_key from Sensor inner join location on Sensor.Location_ID=location.ID where Location.company_ID=%s and Sensor.ID=%s;"%(company_id,id))
    res=res.fetchall()
    return res

def update_sensor(sensor_name,sensor_category,sensor_meta,company_id,id):
    nombre_db = 'datos'
    con = sqlite3.connect(nombre_db)
    cur = con.cursor()
    res = cur.execute("UPDATE Sensor SET Sensor_name='%s',Sensor_category='%s',Sensor_meta='%s' WHERE Sensor.ID='%s' AND Sensor.Location_ID = (SELECT Location.ID FROM Location, Company WHERE Location.Company_ID='%s');"%(sensor_name,sensor_category,sensor_meta,id,company_id))
    con.commit()

def delete_sensor(company_id,id):
    nombre_db = 'datos'
    con = sqlite3.connect(nombre_db)
    cur = con.cursor()
    res = cur.execute("DELETE FROM Sensor WHERE Sensor.ID='%s' AND Sensor.Location_ID = (SELECT Location.ID FROM Location, Company WHERE Location.Company_ID='%s');"%(id,company_id))
    con.commit()



# Consultas de Admin



def create_company(id,company_name,company_api_key):
    nombre_db = 'datos'
    con = sqlite3.connect(nombre_db)
    cur = con.cursor()
    res=cur.execute("INSERT INTO Company VALUES (%s,'%s','%s')"%(id,company_name,company_api_key))
    con.commit()
def create_location(id,company_id,location_name,location_country,location_city,location_meta):
    nombre_db = 'datos'
    con = sqlite3.connect(nombre_db)
    cur = con.cursor()
    res=cur.execute("INSERT INTO Location VALUES (%s,%s,'%s','%s','%s','%s')"%(id,company_id,location_name,location_country,location_city,location_meta))
    con.commit()
    cur.close()

def create_sensor(sensor_id,location_id,sensor_name,sensor_category,sensor_meta,clave):
    nombre_db = 'datos'
    con = sqlite3.connect(nombre_db)
    cur = con.cursor()
    res=cur.execute("INSERT INTO Sensor VALUES (%s,%s,'%s','%s','%s','%s')"%(sensor_id,location_id,sensor_name,sensor_category,sensor_meta,clave))
    con.commit()
    cur.close()

# SensorData
def agregar_sensor_data(F,T):
    nombre_db = 'datos'
    con = sqlite3.connect(nombre_db)
    cur = con.cursor()
    res=cur.execute("INSERT INTO Sensor_data(F,T) VALUES (%s,%s)"%(F,T))
    con.commit()

def obtener_sensor_data(From,to,id_sensor):
    nombre_db = 'datos'
    con = sqlite3.connect(nombre_db)
    cur = con.cursor()
    res=cur.execute("select * from Sensor_data where Sensor_data.F>=%s and Sensor_data.T<=%s and Sensor_data.ID=%s"%(From,to,id_sensor))
    res=res.fetchall()
    return res