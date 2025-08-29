from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class VehicleDB(Base):
    __tablename__ = 'vehicles'
    brand = Column(String, primary_key=True)
    id = Column(Integer)
    VIN = Column(String)