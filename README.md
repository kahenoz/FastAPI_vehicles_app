How to set a virtual environment:
```bash
python3 --version
python3 -m venv my_virtual_env
source my_virtual_env/bin/activate
pip install -r requirements.txt
```

How to run the FastAPI server:
```bash
uvicorn main:app --reload
```     
# Vehicle App

A small practice project using **SQLite** with **FastAPI** to manage vehicles.  

This project demonstrates:
- Creating a database with **SQLAlchemy ORM**.
- Adding, retrieving, and managing vehicles.
- Using **FastAPI** for a simple API interface.

## Features
- Add a new vehicle (brand, id, VIN)
- Retrieve all vehicles
- Retrieve a vehicle by its VIN