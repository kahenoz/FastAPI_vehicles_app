from model import VehicleDB, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import mycursor, mydb

engine = create_engine('sqlite:///vehicles.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def add_new_vehicle_to_db(vehicle: VehicleDB):
    sql = "INSERT INTO vehicles (brand, id, VIN) VALUES (%s, %s, %s)"
    new_vehicle = (vehicle.brand, vehicle.id, vehicle.VIN)
    mycursor.execute(sql, new_vehicle)
    mydb.commit()


def return_vehicle_by_VIN(VIN: str):
    sql = "SELECT * FROM vehicles WHERE VIN = %s"
    val = (VIN,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult

def return_all_vehicles_from_db():
    sql = "SELECT * FROM vehicles"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return myresult