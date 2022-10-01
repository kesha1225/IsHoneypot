from typing import Optional

from pydantic import BaseModel, Field


class Response(BaseModel):
    is_honeypot: bool = Field(alias="IsHoneypot")
    error: Optional[str] = Field(alias="Error")
    max_tx_amount: int = Field(alias="MaxTxAmount")
    max_tx_amount_bnb: int = Field(alias="MaxTxAmountBNB")
    buy_tax: float = Field(alias="BuyTax")
    sell_tax: float = Field(alias="SellTax")
    buy_gas: int = Field(alias="BuyGas")
    sell_gas: int = Field(alias="SellGas")
