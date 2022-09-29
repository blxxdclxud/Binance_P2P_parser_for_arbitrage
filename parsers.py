from config import logger
import asyncio
from aiohttp import ClientSession


def form_asset_info_params(asset, fiat, trade_type, pay_types=None, limit=0,
                           merchant_check=False, page=1, publisher_type=None, row=1):
    if pay_types is None:
        pay_types = []

    params = {
        "asset": asset,
        "fiat": fiat,
        "merchantCheck": merchant_check,
        "page": page,
        "payTypes": pay_types,
        "publisherType": publisher_type,
        "rows": row,
        "tradeType": trade_type,
        "transAmount": limit
    }
    return params


def make_asset_info_dict(data):
    needed_data = data["data"][0]
    result = {
        "asset": needed_data["adv"]["asset"],
        "price": needed_data["adv"]["price"],
        "payment_system": ', '.join(dct["tradeMethodName"] for dct in needed_data["adv"]["tradeMethods"] if dct["tradeMethodName"] != None),
        "user_nickname": needed_data["advertiser"]["nickName"],
        "user_id": needed_data["advertiser"]["userNo"]
    }

    return result


def form_symbol_price_params(symbol):
    params = {
        "symbol": symbol
    }

    return params


def make_price_dict(data):
    data["price"] = float(data["price"])

    return data


all_data = []
all_symbols_data = {
    "USDTUSDT": 1.0,
    "BTCBTC": 1.0,
    "BUSDBUSD": 1.0,
    "ETHETH": 1.0
}
count = 0


async def get_all_data(session, params, num):
    if "symbol" in params:
        url_parameters = {"url": 'https://binance.com/api/v3/ticker/price',
                          "params": params}
    else:
        url_parameters = {"url": 'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',
                          "json": params}
    async with session.post(**url_parameters) as resp:
        assert resp.status == 200

        resp_json = await resp.json()

        if "symbol" in params:
            all_symbols_data[params["symbol"]] = make_price_dict(resp_json)["price"]
            # time.sleep(0.5)
        else:
            # print(params)
            # print(123, resp_json, url_parameters)
            all_data.append((num, make_asset_info_dict(resp_json)))


async def load_data(data_params):
    async with ClientSession() as session:
        tasks = []
        for idx in range(len(data_params)):
            task = asyncio.create_task(get_all_data(session, data_params[idx], idx + 1))
            tasks.append(task)

        await asyncio.gather(*tasks)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
loop = asyncio.get_event_loop()
