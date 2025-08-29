from fastapi import FastAPI
from service import add_new_vehicle_to_db, return_vehicle_by_VIN, return_all_vehicles_from_db
from model import VehicleDB

app = FastAPI()

@app.post("/add_vehicle")
def add_vehicle(brand: str, id: int, VIN: str):
    vehicle = VehicleDB(brand=brand, id=id, VIN=VIN)
    try:
        add_new_vehicle_to_db(vehicle)
    except Exception as e:
        return f"Failed to add vehicle: {e}"
    return f"Successfully added vehicle {brand} with VIN {VIN} at gate {id}"

@app.get("/vehicle_by_VIN")
def get_vehicle_by_VIN(VIN: str):
    vehicle = return_vehicle_by_VIN(VIN)
    return {"data": vehicle}

@app.get("/get_all_vehicles")
def get_all_vehicles():
    vehicles = return_all_vehicles_from_db()
    return {"data": vehicles}