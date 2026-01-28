# backend/app/crud.py

# Kommentar: CRUD står för Create, Read, Update, Delete och innehåller
# funktioner för att interagera med databasen, som anropas från routrar.

from datetime import datetime
from sqlalchemy.orm import Session
from .models import Competitor, TimeEntry


def get_competitors(db: Session):
    """Hämta alla tävlande från databasen."""
    return db.query(Competitor).all()

def get_competitor_by_id(db: Session, competitor_id: int) -> Competitor | None:
    """Hämta en tävlande baserat på dess ID."""
    return db.query(Competitor).filter(Competitor.id == competitor_id).first()

def add_competitor(db: Session, start_number: str, name: str):
    """Lägg till en ny deltagare i databasen."""
    existing = db.query(Competitor).filter_by(start_number=start_number).first()
    if existing is not None:
        return None
    competitor = Competitor(start_number=start_number, name=name)
    db.add(competitor)
    db.commit()
    db.refresh(competitor)
    return competitor

def remove_competitor(db: Session, start_number: str):
    """Ta bort deltagare och alla tidsregistreringar."""
    found = db.query(Competitor).filter_by(start_number=start_number).first()
    if found is None:
        return None
    remove_times_by_start_number(db, start_number)
    db.delete(found)
    db.commit()
    return found

def get_times(db: Session):
    """Hämta alla tidsregistreringar från databasen."""
    return db.query(TimeEntry).all()

def remove_times_by_start_number(db: Session, start_number: str):
    """Ta bort alla tider baserat på start nummer."""
    times = (
        db.query(TimeEntry)
        .join(Competitor)
        .filter(Competitor.start_number == start_number)
        .all()
    )
    for t in times:
        db.delete(t)
    db.commit()
    return len(times)

def get_times_by_start_number(db: Session, start_number: str):
    """Hämta tidsregistreringar för en specifik tävlande baserat på startnummer."""
    return (
        db.query(TimeEntry)
        .join(Competitor)
        .filter(Competitor.start_number == start_number)
        .all()
    )


def record_time_for_start_number(db: Session, start_number: str, station: str) -> TimeEntry | None:
    """Registrera en ny tid för en tävlande med angivet startnummer."""
    competitor = db.query(Competitor).filter_by(start_number=start_number).first()
    if competitor is None:
        return None  # hanteras i router
    entry = TimeEntry(competitor_id=competitor.id, station=station, timestamp=datetime.datetime.now(datetime.timezone.utc))
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry