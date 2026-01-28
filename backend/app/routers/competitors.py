# backend/app/routers/competitors.py
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db

router = APIRouter(prefix="/competitors", tags=["competitors"])


@router.get("/", response_model=list[schemas.CompetitorOut])
def read_competitors(db: Session = Depends(get_db)):
    return crud.get_competitors(db)

@router.get("/{competitor_id}", response_model=schemas.CompetitorOut)
def read_competitor(competitor_id: int, db: Session = Depends(get_db)):
    competitor = crud.get_competitor_by_id(db, competitor_id)
    if competitor is None:
        raise HTTPException(status_code=404, detail="Competitor not found")
    return competitor

@router.post("/", response_model=schemas.CompetitorOut, status_code=201)
def create_competitor(data: schemas.CompetitorIn, db:Session = Depends(get_db)):
    competitor = crud.add_competitor(db,start_number=data.start_number, name=data.name)
    if competitor is None:
        raise HTTPException(status_code=409,detail="Start Number Already Exists")
    return competitor

@router.delete("/{start_number}", status_code=204)
def delete_competitor(start_number: str, db: Session = Depends(get_db)):
    ok = crud.remove_competitor(db, start_number)
    if ok is None:
        raise HTTPException(status_code=404, detail="Competitor not found")
    return Response(status_code=204)