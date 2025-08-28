from fastapi import FastAPI
from service import add_new_vehicle_to_db
from model import VehicleDB

app = FastAPI()

@app.post("/add_vehicle")
def add_vehicle(brand: str, gate_id: int, VIN: str):
    vehicle = VehicleDB(brand=brand, gate_id=gate_id, VIN=VIN)
    try:
        add_new_vehicle_to_db(vehicle)
    except Exception as e:
        return f"Failed to add vehicle"
    return f"Successfully added vehicle {brand} with VIN {VIN} at gate {gate_id}"