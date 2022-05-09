from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from pydantic_sqlalchemy import sqlalchemy_to_pydantic


from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    email = Column(String)
    addresses = relationship(
        "Address", back_populates="user", cascade="all, delete, delete-orphan"
    )


class Address(Base):
    __tablename__ = "addresses"

    address = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"))
    user = relationship("User", back_populates="addresses")
    transactions = relationship(
        "Transaction", back_populates="address", cascade="all, delete, delete-orphan"
    )

    num_transactions = Column(Integer)
    total_received = Column(Integer)
    total_sent = Column(Integer)
    finnal_balance = Column(Integer)


class Transaction(Base):
    __tablename__ = "transactions"

    hash = Column(String, primary_key=True, index=True)
    address_id = Column(String, ForeignKey("addresses.address"))
    address = relationship("Address", back_populates="transactions")
    block_height = Column(Integer)
    transaction_index = Column(Integer)


PydanticUser = sqlalchemy_to_pydantic(User)
PydanticAddress = sqlalchemy_to_pydantic(Address)
PydanticTransaction = sqlalchemy_to_pydantic(Transaction)
