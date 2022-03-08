# -*- coding: utf-8 -*-
import sqlite3

class Feinstaub_Datenbank:
    def __init__(self):
        """
        Initialisiert die Klasse

        Returns
        -------
        None.

        """
        self.con = sqlite3.connect("Beispiel.sqlite")
        self.__initialise_tables()

    def __initialise_tables(self):
        """
        Initialisiert die Datenbank mit den zwei Tabellen

        Returns
        -------
        None.

        """
        cur = self.con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS SDS011
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_id INT NOT NULL,
    location INT,
    lon DECIMAL(10, 3),
    lat DECIMAL(10, 3),
    p1 DECIMAL(10, 2),
    dur_p1 DECIMAL,
    ratio_p1 DECIMAL,
    p2 DECIMAL(10, 2),
    dur_p2 DECIMAL,
    ratio_p2 DECIMAL,
    messzeitpunkt DATETIME
    )''')

        self.con.commit()

        cur.execute('''CREATE TABLE IF NOT EXISTS DHT22
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_id INT,
    location INT,
    lon DECIMAL(10, 3),
    lat DECIMAL(10, 3),
    humidity DECIMAL(10, 2),
    temperature DECIMAL(10, 2),
    messzeitpunkt DATETIME
    )''')

        self.con.commit()
    
    def insert_single_sds011_entry(self, sensor_id:int, location:int, lon:float,lat:float,p1:float,dur_p1:float,ratio_p1:float,p2:float, dur_p2:float, ratio_p2:float, messzeitpunkt):
        """

        Parameters
        ----------
        sensor_id : int
            Sensor ID.
        location : int
            Location.
        lon : float
            Longitude.
        lat : float
            Latitude.
        p1 : float
            Messdaten.
        dur_p1 : float
            Empty.
        ratio_p1 : float
            Empty.
        p2 : float
            Messdaten.
        dur_p2 : float
            Empty.
        ratio_p2 : float
            Empty.
        messzeitpunkt : TYPE
            Messzeitpunkt der Daten.

        Returns
        -------
        None.

        """
        self.insert_multiple_sds011_entries([(sensor_id, location, lon, lat, p1, dur_p1, ratio_p1, p2, dur_p2, ratio_p2, messzeitpunkt)])

    def insert_multiple_sds011_entries(self, data:[()]):
        """

        Parameters
        ----------
        data : [(sensor_id:int, location:int, lon:float,lat:float,p1:float,dur_p1:float,ratio_p1:float,p2:float, dur_p2:float, ratio_p2:float, messzeitpunkt), *]
            
            Beinhaltet als ein Array die einzutragenen Werte, 
            diese sind als Tupel zusammengefasst.

        Returns
        -------
        None.

        """
        cur = self.con.cursor()
        command = """
        INSERT INTO SDS011 
            (sensor_id, location, lon, lat, p1, dur_p1, ratio_p1, p2, dur_p2, ratio_p2, messzeitpunkt)
        VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
        cur.executemany(command, data)
        self.con.commit()
    
        
    def inser_single_dht22_entry(self, sensor_id:int, location:int, lon:float,lat:float, humidity:float, temperature:float, messzeitpunkt ):
        """

        Parameters
        ----------
        sensor_id : int
            Sensor ID.
        location : int
            Location.
        lon : float
            Longitude.
        lat : float
            Latitude.
        humidity : float
            Luftfeuchtigkeit.
        temperature : float
            Temperatur.
        messzeitpunkt : TYPE
            Messzeitpunkt.

        Returns
        -------
        None.

        """
        self.insert_multiple_dht22_entries([(sensor_id, location, lon, lat, humidity, temperature, messzeitpunkt)])
        
    def insert_multiple_dht22_entries(self, data:[()]):
        """

        Parameters
        ----------
        data : [(sensor_id:int, location:int, lon:float, lat:float, humidity:float, temperature:float, messzeitpunkt), *]
            
            Beinhaltet als ein Array die einzutragenen Werte, 
            diese sind als Tupel zusammengefasst.

        Returns
        -------
        None.

        """
        cur = self.con.cursor()
        command = """
        INSERT INTO DHT22 
            (sensor_id, location, lon, lat, humidity, temperature, messzeitpunkt)
        VALUES
            (?, ?, ?, ?, ?, ?, ?)
            """
        cur.executemany(command, data)
        self.con.commit()


    """Aufgabe 6:"""

    def get_daily_data(self):
        while True:
            cur = self.con.cursor()
            print("1. Temperatur")
            print("2. Luftfeuchtigkeit")
            print("3. Feinstaub")
            task = input("Welche Werte sollen ausgegeben werden?: ")

            if(task == "1"):
                day = input("Welcher Tag soll ausgegeben werden? Format: YYYY-MM-DD: ")
                time1 = day + "T00:00:00"
                time2 = day + "T23:59:59"
                task = input("Möglichkeit:")

                if (task == "1"):
                    """Möglichkeit1:"""
                    dic = {'start': time1, 'end': time2}
                    sql_query = "SELECT MIN(temperature), MAX(temperature), AVG(temperature) FROM DHT22 WHERE messzeitpunkt >= :start AND messzeitpunkt < :end"
                    cur.execute(sql_query, dic)
                    print(cur.fetchall())
                    break

                if (task == "2"):
                    """Möglichkeit2:"""
                    tuple = (time1, time2)
                    sql_query = "SELECT MIN(temperature),MAX(temperature),AVG(temperature) FROM DHT22 WHERE messzeitpunkt BETWEEN ? AND ?"
                    cur.execute(sql_query, tuple)
                    print(cur.fetchall())
                    break
                break

            if(task == "2"):
                day = input("Welcher Tag soll ausgegeben werden? Format: YYYY-MM-DD: ")
                time1 = day + "T00:00:00"
                time2 = day + "T23:59:59"
                task = input("Möglichkeit:")

                if (task == "1"):
                    """Möglichkeit1:"""
                    dic = {'start': time1, 'end': time2}
                    sql_query = "SELECT MIN(humidity), MAX(humidity), AVG(humidity) FROM DHT22 WHERE messzeitpunkt >= :start AND messzeitpunkt < :end"
                    cur.execute(sql_query, dic)
                    print(cur.fetchall())
                    break

                if (task == "2"):
                    """Möglichkeit2:"""
                    tuple = (time1, time2)
                    sql_query = "SELECT MIN(humidity),MAX(humidity),AVG(humidity) FROM DHT22 WHERE messzeitpunkt BETWEEN ? AND ?"
                    cur.execute(sql_query, tuple)
                    print(cur.fetchall())
                    break
                break

            if(task == "3"):
                day = input("Welcher Tag soll ausgegeben werden? Format: YYYY-MM-DD: ")
                time1 = day + "T00:00:00"
                time2 = day + "T23:59:59"
                task = input("Möglichkeit:")

                if (task == "1"):
                    """Möglichkeit1:"""
                    dic = {'start': time1, 'end': time2}
                    sql_query = "SELECT MIN(p1), MIN(p2) ,MAX(p1), MAX(p2),AVG(p1), AVG(p2) FROM SDS011 WHERE messzeitpunkt >= :start AND messzeitpunkt < :end"
                    cur.execute(sql_query, dic)
                    print(cur.fetchall())
                    break

                if (task == "2"):
                    """Möglichkeit2:"""
                    tuple = (time1, time2)
                    sql_query = "SELECT MIN(p1), MIN(p2) ,MAX(p1), MAX(p2),AVG(p1), AVG(p2) FROM SDS011  WHERE messzeitpunkt BETWEEN ? AND ?"
                    cur.execute(sql_query, tuple)
                    print(cur.fetchall())
                    break
                break

    
    def close(self):
        self.con.close()