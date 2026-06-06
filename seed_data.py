import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(".")), "backend"))
os.chdir("backend")
from database import SessionLocal
from models import Price
db = SessionLocal()
stations = [("Shell Guaynabo","Guaynabo","Regular",0.977),("Shell Guaynabo","Guaynabo","Premium",1.137),("Gulf Bayamon","Bayamon","Regular",0.957),("Gulf Bayamon","Bayamon","Premium",1.067),("Puma San Juan","San Juan","Regular",1.007),("Puma San Juan","San Juan","Premium",1.167),("Total Carolina","Carolina","Regular",1.007),("Total Carolina","Carolina","Premium",1.167),("Shell Caguas","Caguas","Regular",0.977),("Shell Caguas","Caguas","Premium",1.137),("Gulf Ponce","Ponce","Regular",0.957),("Gulf Ponce","Ponce","Premium",1.067),("Ecomaxx Mayaguez","Mayaguez","Regular",0.977),("Ecomaxx Mayaguez","Mayaguez","Premium",1.107),("Sunoco Arecibo","Arecibo","Regular",0.977),("Sunoco Arecibo","Arecibo","Premium",1.157),("Shell Humacao","Humacao","Regular",0.977),("Shell Humacao","Humacao","Premium",1.137),("Total Fajardo","Fajardo","Regular",1.007),("Total Fajardo","Fajardo","Premium",1.167),("Gulf Aguadilla","Aguadilla","Regular",0.957),("Gulf Aguadilla","Aguadilla","Premium",1.067),("Puma Guayama","Guayama","Regular",1.007),("Puma Guayama","Guayama","Premium",1.167),("Shell Toa Baja","Toa Baja","Regular",0.977),("Shell Toa Baja","Toa Baja","Diesel",1.247),("Gulf Trujillo Alto","Trujillo Alto","Regular",0.957),("Ecomaxx Isabela","Isabela","Regular",0.977),("Total Manati","Manati","Regular",1.007),("Shell Rio Grande","Rio Grande","Regular",0.977)]
for s in stations:
    db.add(Price(station_name=s[0],municipality=s[1],fuel_type=s[2],price=s[3],is_outdated=False,thumbs_up=0,thumbs_down=0))
db.commit()
db.close()
print("Done! Added",len(stations),"prices")
