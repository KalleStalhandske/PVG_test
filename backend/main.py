# backend/main.py
import os
from datetime import datetime
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

import database
import models
import schema
from database import get_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Körs vid uppstart
    # Lägg till temporär testdata, om databasen är tom.
    # Bra under utveckling/testining, men ta bort i produktion!
    db = database.SessionLocal()
    if db.query(schema.Competitor).count() == 0:
        comp1 = schema.Competitor(start_number="123", name="Alice")
        comp2 = schema.Competitor(start_number="456", name="Bob")
        db.add_all([comp1, comp2])
        db.commit()

        db.refresh(comp1)
        db.refresh(comp2)

        db.add_all(
            [
                schema.TimeEntry(
                    competitor_id=comp1.id, timestamp=datetime(2025, 6, 27, 12, 31, 39)
                ),
                schema.TimeEntry(
                    competitor_id=comp2.id, timestamp=datetime(2025, 6, 27, 12, 32, 15)
                ),
                schema.TimeEntry(
                    competitor_id=comp2.id, timestamp=datetime(2025, 6, 27, 12, 47, 38)
                ),
                schema.TimeEntry(
                    competitor_id=comp1.id, timestamp=datetime(2025, 6, 27, 12, 52, 5)
                ),
            ]
        )
        db.commit()
    db.close()

    yield  # startup done


app = FastAPI(lifespan=lifespan)
schema.Base.metadata.create_all(bind=database.engine)

# Mount the frontend dist folder (after build)
if os.path.exists("../frontend/dist"):
    print("Mounting static files from ../frontend/dist")
    app.mount("/", StaticFiles(directory="../frontend/dist", html=True), name="static")
else:
    print("No frontend dist folder found, not serving static files.")
    print(
        "Make sure to build the frontend with 'npm run build' in the frontend directory."
    )

# Enable CORS for dev if frontend runs separately
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/competitors", response_model=list[models.CompetitorOut])
def list_competitors(db: Session = Depends(get_db)):
    return db.query(schema.Competitor).all()


@app.get("/times", response_model=list[models.TimeEntryOut])
def list_times(db: Session = Depends(get_db)):
    return db.query(schema.TimeEntry).all()


@app.get("/times/{start_number}", response_model=list[models.TimeEntryOut])
def get_times_by_start_number(start_number: str, db: Session = Depends(get_db)):
    return (
        db.query(schema.TimeEntry)
        .filter(schema.TimeEntry.start_number == start_number)
        .all()
    )


@app.post("/record_time")
def record_time(data: models.RecordTimeIn, db: Session = Depends(get_db)):
    competitor = (
        db.query(schema.Competitor).filter_by(start_number=data.start_number).first()
    )
    if not competitor:
        raise HTTPException(status_code=404, detail="Competitor not found")
    # Databasen lägger automatiskt till nuvarande tid som timestamp.
    # Man skulle också kunna skicka in en timestamp i requesten.
    # Hmm... vilket är bäst?
    entry = schema.TimeEntry(competitor_id=competitor.id)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return {
        "status": "ok",
        "timestamp": entry.timestamp,
        "competitor_id": entry.competitor_id,
    }
