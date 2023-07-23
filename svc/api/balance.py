from fastapi import APIRouter
from svc.core import exchange

balance_router = APIRouter()

@balance_router.get('')
async def get_kline():
    return [record._asdict() for record in exchange.get_balance()]
