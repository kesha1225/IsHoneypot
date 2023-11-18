from pydantic import BaseModel, Field


class Token(BaseModel):
    name: str
    symbol: str
    decimals: int
    address: str
    total_holders: int = Field(alias="totalHolders")


class WithToken(BaseModel):
    name: str
    symbol: str
    decimals: int
    address: str
    total_holders: int = Field(alias="totalHolders")


class HoneypotResult(BaseModel):
    is_honeypot: bool = Field(alias="isHoneypot")


class SimulationResult(BaseModel):
    buy_tax: float = Field(alias="buyTax")
    sell_tax: float = Field(alias="sellTax")
    transfer_tax: float = Field(alias="transferTax")
    buy_gas: str = Field(alias="buyGas")
    sell_gas: str = Field(alias="sellGas")


class Chain(BaseModel):
    id: str
    name: str
    short_name: str = Field(alias="shortName")
    currency: str


class Pair(BaseModel):
    name: str
    address: str
    token0: str
    token1: str
    type: str


class PairData(BaseModel):
    pair: Pair
    chain_id: str = Field(alias="chainId")
    reserves0: str
    reserves1: str
    liquidity: float
    router: str
    created_at_timestamp: str = Field(alias="createdAtTimestamp")
    creation_tx_hash: str = Field(alias="creationTxHash")


class Response(BaseModel):
    token: Token
    with_token: WithToken = Field(alias="withToken")
    simulation_success: bool = Field(alias="simulationSuccess")
    honeypot_result: HoneypotResult = Field(alias="honeypotResult")
    simulation_result: SimulationResult = Field(alias="simulationResult")
    flags: list
    chain: Chain
    router: str
    pair: PairData
    pair_address: str = Field(alias="pairAddress")
