import sys
import os
from contextlib import asynccontextmanager
from apscheduler.schedulers.asyncio import AsyncIOScheduler
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from database import engine, Base, SessionLocal
from routes.prices import router as prices_router
from models import Price
from datetime import datetime, timedelta

def mark_outdated():
    db = SessionLocal()
    cutoff = datetime.utcnow() - timedelta(hours=48)
    db.query(Price).filter(Price.reported_at < cutoff, Price.is_outdated == False).update({"is_outdated": True})
    db.commit()
    db.close()

scheduler = AsyncIOScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    scheduler.add_job(mark_outdated, "interval", hours=1)
    scheduler.start()
    yield
    scheduler.shutdown()

Base.metadata.create_all(bind=engine)

app = FastAPI(title="GasolinazoPR API", lifespan=lifespan)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(prices_router, prefix="/api")

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def read_root():
    return FileResponse("frontend/index.html")
