from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.sql import func
from database import Base

class Station(Base):
    __tablename__ = "stations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    municipality = Column(String, index=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

class Price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True, index=True)
    station_id = Column(Integer, index=True)
    station_name = Column(String)
    municipality = Column(String, index=True)
    fuel_type = Column(String, index=True)
    price = Column(Float)
    reported_at = Column(DateTime(timezone=True), server_default=func.now())
    is_outdated = Column(Boolean, default=False)
    thumbs_up = Column(Integer, default=0)
    thumbs_down = Column(Integer, default=0)
