from fastapi import FastAPI
from typing import List
from fastapi import Depends, FastAPI, HTTPException

from models.response import AddressResponse, BalanceResponse, TransactionResponse
from core.blockchain import BlockchainQuerier
from database import Base, engine, SessionLocal
from sqlalchemy.orm import sessionmaker, Session


Base.metadata.create_all(engine)

LocalSession = sessionmaker(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Initializing client class for whole session
querier = BlockchainQuerier()


@app.get("/api/{address}", response_model=AddressResponse)
async def get_address(address: str, txn_limit: int = 10):
    return querier.get_address(address, txn_limit)


@app.get("/api/{address}/txs", response_model=List[TransactionResponse])
async def get_transactions(address: str, txn_limit: int = 10):
    return querier.get_transactions(address, txn_limit)


@app.get("/api/{address}/balance", response_model=BalanceResponse)
async def get_address_balance(address: str):
    return querier.get_balance(address)


# User endpoints [Currently broken... need to debug]


# @app.post("/api/users/", response_model=PydanticUser)
# async def create_user(user: UserEmail, db: Session = Depends(get_db)):
#     # Validation should be added here
#     crud = DatabaseSession(db)
#     return crud.create_user(user)


# @app.get("/api/users/{user_id}", response_model=PydanticUser)
# async def get_user(user_id: str, db: Session = Depends(get_db)):
#     # Validation should be added here
#     crud = DatabaseSession(db)
#     return crud.get_user_by_id(user_id)


# @app.post("/api/users/{user_id}/addresses", response_model=List[PydanticAddress])
# async def add_address_to_user(user_id: str, address: UserAddress, db: Session = Depends(get_db)):
#     # Validation should be added here
#     address_string = address.address
#     address_response = querier.get_address(address_string)
#     address = PydanticAddress(**address_response.dict())
#     address.user_id = user_id

#     crud = DatabaseSession(db)
#     return crud.add_address(address)
