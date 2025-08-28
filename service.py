from model import VehicleDB, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///vehicles.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def add_new_vehicle_to_db(vehicle: VehicleDB):
    session = Session()
    new_vehicle = VehicleDB(brand=vehicle.brand, gate_id=vehicle.gate_id, VIN=vehicle.VIN)
    session.add(new_vehicle)
    session.commit()
    session.close()

def return_vehicle_by_VIN(VIN: str):
    session =Session()
    vehicle = session.query(VehicleDB).filter(VehicleDB.VIN == VIN).first()
    session.close()
    return vehicle