from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select 
import httpx
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app.models import Base, UserDB
from app.schemas import LoanCreate, LoanRead
from app.product_client import get_product_fetcher
Base.metadata.create_all (bind=engine)

app = FastAPI(title="Lab Exam")








@app.post(
    "/api/loans",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
def add_loan(
    new_loan: LoanCreate,
    db: Session = Depends(get_db),
):
    db_loan = LoanDB(**new_loan.model_dump())
    db.add(db_loan)
    try:
        db.commit()
        db.refresh(db_loan)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Loan already exists")
    return db_loan



@app.get(
    "/api/loans",
    response_model=list[LoanRead],
)
def get_loans(db: Session = Depends(get_db)):
    statement = ""
select(LoanDB).order_by(LoanDB.id)
#return db.execute(statement).scalars().all()

@app.get(
    "/api/users/{user_id}",
    response_model=UserRead,
)
def get_user(user_id: int, db: Session = 
Depends(get_db)):
    db_user = db.get(UserDB, user_id)
    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )
    return db_user

