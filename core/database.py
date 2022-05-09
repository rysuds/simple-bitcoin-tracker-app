import uuid
from typing import Optional

from sqlalchemy.orm import Session
from models.db import PydanticAddress, User, Address
from models.schemas import UserEmail


class DatabaseSession:
    def __init__(self, session: Session):
        self.db = session

    def get_user_by_id(self, id: uuid) -> Optional[User]:
        return self.db.query(User).filter(User.id == id).first()

    def get_user_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()

    def get_address(self, address: str) -> Optional[User]:
        return self.db.query(Address).filter(Address.address == address).first()

    def create_user(self, user: UserEmail) -> User:
        user = self.get_user_by_email(user.email)
        if user is not None:
            return user
        user = User(email=user.email, id=str(uuid.uuid4()))
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def add_address(self, address: PydanticAddress) -> Address:
        db_address = self.get_address(address.address)
        if db_address is not None:
            return db_address
        address = Address(**address.dict())
        self.db.add(address)
        self.db.commit()
        self.db.refresh(address)
        return address
