from typing import List
from pydantic import BaseModel, Field


class TransactionResponse(BaseModel):
    hash: str
    block_height: int
    transaction_index: int = Field(alias='tx_index')


class AddressResponse(BaseModel):
    address: str
    num_transactions: int = Field(alias='n_tx')
    transactions: List[TransactionResponse] = Field(alias='txs')
    total_received: int
    total_sent: int
    final_balance: int


class BalanceResponse(BaseModel):
    total_received: int
    total_sent: int
    final_balance: int
