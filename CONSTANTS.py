from itertools import combinations_with_replacement

CREDENTIALS_FILE = 'creds.json'

ASSETS = [
    "USDT",
    "BTC",
    "BUSD",
    "ETH"
]

combinations = list(combinations_with_replacement(ASSETS, 2))
ALL_ASSET_COUPLES = list(set(combinations + list(map(lambda x: x[::-1], combinations))))
# BANKS_RUS = [
#     "Тинькофф",
#     "Росбанк",
#     "QIWI",
#     "ЮMoney"
# ]

BANKS_EN_RUS = {
    "TinkoffNew": "Тинькофф",
    "RosBankNew": "Росбанк",
    "QIWI": "QIWI",
    "YandexMoneyNew": "ЮMoney"
}

OPERATION_TYPES = {
    "T+T": ("BUY", "SELL"),
    "M+M": ("SELL", "BUY"),
    "T+M": ("BUY", "BUY"),
    "M+T": ("SELL", "BUY")
}

SYMBOLS = [
    "ETHUSDT",
    "ETHBTC",
    "ETHBUSD",
    "BTCBUSD",
    "BTCUSDT",
    "BUSDUSDT"
]