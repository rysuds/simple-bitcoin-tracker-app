import requests
from typing import List
from pydantic import BaseModel, Field

from models.response import AddressResponse, TransactionResponse, BalanceResponse


class BlockchainQuerier:
    def __init__(self):
        self.session = requests.Session()

    # TODO add error handling and retry logic
    def get_address(self, address: str, txn_limit: int = 10) -> AddressResponse:
        response = self.session.get(
            f'https://blockchain.info/rawaddr/{address}?limit={txn_limit}')
        return AddressResponse(**response.json())

    def get_transactions(self, address: str, txn_limit: int) -> List[TransactionResponse]:
        address: AddressResponse = self.get_address(address, txn_limit)
        return address.transactions

    def get_balance(self, address: str) -> int:
        address: AddressResponse = self.get_address(address)
        return BalanceResponse(
            total_received=address.total_received,
            total_sent=address.total_sent,
            final_balance=address.final_balance
        )
