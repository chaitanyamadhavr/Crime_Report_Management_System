import mysql.connector
import mariadb
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="demo_crime"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS crime_details (criminal_id int, criminal_name varchar(15), criminal_nickname varchar(20), criminal_type varchar(20), crime_location varchar(20), crime_date varchar(10));')


def add_data(criminal_id, criminal_name, criminal_nickname, criminal_type, crime_location, crime_date):
    c.execute('INSERT INTO crime_details (criminal_id, criminal_name, criminal_nickname, criminal_type, crime_location, crime_date) VALUES (%s,%s,%s,%s,%s,%s);',
              (criminal_id, criminal_name, criminal_nickname, criminal_type, crime_location, crime_date))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM crime_details')
    data = c.fetchall()
    return data


def view_only_criminal_names():
    c.execute('SELECT criminal_name FROM crime_details')
    data = c.fetchall()
    return data


def get_details(criminal_name):
    c.execute('SELECT * FROM crime_details WHERE criminal_name="{}"'.format(criminal_name))
    data = c.fetchall()
    return data


def edit_details(new_criminal_id, new_criminal_name, new_criminal_nickname, new_criminal_type, new_crime_location, new_crime_date, criminal_id, criminal_name, criminal_nickname, criminal_type, crime_location, crime_date):
    
    c.execute("UPDATE crime_details SET criminal_id=%s, criminal_name=%s, criminal_nickname=%s, criminal_type=%s, crime_location=%s, crime_date=%s WHERE  criminal_id=%s and criminal_name=%s and criminal_nickname=%s and criminal_type=%s and crime_location=%s and crime_date=%s", (new_criminal_id, new_criminal_name, new_criminal_nickname, new_criminal_type, new_crime_location, new_crime_date, criminal_id, criminal_name, criminal_nickname, criminal_type, crime_location, crime_date))
    mydb.commit()
    return view_all_data()
    


def delete_data(criminal_name):
    c.execute('DELETE FROM crime_details WHERE criminal_name ="{}"'.format(criminal_name))
    mydb.commit()

def view_only_criminal_id():
    c.execute("select criminal_id from crime_details")
    data=c.fetchall()
    return data