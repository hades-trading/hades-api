from starlette.exceptions import HTTPException
from fastapi.staticfiles import StaticFiles

from hades.core import TradeBotConf
from hades.core.exchange.binance import BinanceUMExchangeClient

exchange = BinanceUMExchangeClient(TradeBotConf.load())


class SPAStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope):
        try:
            response = await super().get_response(path, scope)
        except HTTPException as ex:
            if ex.status_code == 404:
                response = await super().get_response('.', scope)
        return response
