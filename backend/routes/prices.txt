from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import List, Optional
from database import get_db
from models import Price
from schemas import PriceCreate, PriceResponse

router = APIRouter()

MUNICIPIOS = ["Adjuntas","Aguada","Aguadilla","Aguas Buenas","Aibonito","Anasco","Arecibo","Arroyo","Barceloneta","Barranquitas","Bayamon","Cabo Rojo","Caguas","Camuy","Canovanas","Carolina","Catano","Cayey","Ceiba","Ciales","Cidra","Coamo","Comerio","Corozal","Culebra","Dorado","Fajardo","Florida","Guanica","Guayama","Guayanilla","Guaynabo","Gurabo","Hatillo","Hormigueros","Humacao","Isabela","Jayuya","Juana Diaz","Juncos","Lajas","Lares","Las Marias","Las Piedras","Loiza","Luquillo","Manati","Maricao","Maunabo","Mayaguez","Moca","Morovis","Naguabo","Naranjito","Orocovis","Patillas","Penuelas","Ponce","Quebradillas","Rincon","Rio Grande","Sabana Grande","Salinas","San German","San Juan","San Lorenzo","San Sebastian","Santa Isabel","Toa Alta","Toa Baja","Trujillo Alto","Utuado","Vega Alta","Vega Baja","Vieques","Villalba","Yabucoa","Yauco"]

@router.get("/prices", response_model=List[PriceResponse])
def get_prices(municipality: Optional[str] = None, fuel_type: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Price).filter(Price.is_outdated == False)
    if municipality:
        query = query.filter(Price.municipality == municipality)
    if fuel_type:
        query = query.filter(Price.fuel_type == fuel_type)
    return query.order_by(Price.price.asc()).all()

@router.post("/prices", response_model=PriceResponse)
def report_price(price: PriceCreate, db: Session = Depends(get_db)):
    db_price = Price(**price.dict())
    db.add(db_price)
    db.commit()
    db.refresh(db_price)
    return db_price

@router.post("/prices/{price_id}/thumbs_up")
def thumbs_up(price_id: int, db: Session = Depends(get_db)):
    price = db.query(Price).filter(Price.id == price_id).first()
    if not price:
        raise HTTPException(status_code=404, detail="Precio no encontrado")
    price.thumbs_up += 1
    db.commit()
    return {"message": "Voto registrado"}

@router.post("/prices/{price_id}/thumbs_down")
def thumbs_down(price_id: int, db: Session = Depends(get_db)):
    price = db.query(Price).filter(Price.id == price_id).first()
    if not price:
        raise HTTPException(status_code=404, detail="Precio no encontrado")
    price.thumbs_down += 1
    db.commit()
    return {"message": "Voto registrado"}

@router.get("/municipios")
def get_municipios():
    return {"municipios": MUNICIPIOS}