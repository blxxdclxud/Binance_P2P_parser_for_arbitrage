from config import logger
from dotenv import load_dotenv
import os
import sys
import traceback

import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials

from CONSTANTS import CREDENTIALS_FILE
from handlers import make_total_data_array

load_dotenv()

GOOGLE_SHEET_ID = os.getenv("SPREADSHEET_ID")

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
http_auth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http=http_auth)


def fill_whole_table(data):
    data.sort(key=lambda x: x[-1], reverse=True)
    print(data[0])
    values = service.spreadsheets().values().batchUpdate(
        spreadsheetId=GOOGLE_SHEET_ID,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": f"A9:N{8 + len(data)}",
                 "majorDimension": "ROWS",
                 "values": data}
            ]
        }).execute()

    # pprint(values)


def start_spreadsheet():
    user_data = service.spreadsheets().values().get(
        spreadsheetId=GOOGLE_SHEET_ID,
        majorDimension="ROWS",
        range="B4:B6"
    ).execute()["values"][0]

    try:
        bank_amount = float(user_data[0])
    except Exception:
        bank_amount = 0.0
    try:
        buy_limit = float(user_data[1])
    except Exception:
        buy_limit = 0
    try:
        sell_limit = float(user_data[2])
    except Exception:
        sell_limit = 0

    logger.info(f'{__name__}/{sys._getframe().f_code.co_name}: {bank_amount}, "BUY": {buy_limit}, "SELL": {sell_limit}')
    try:
        fill_whole_table(make_total_data_array("RUB", bank_amount, {"BUY": buy_limit,
                                                                    "SELL": sell_limit}))

        logger.info("Done successfully!")
        print("Done successfully!")
    except Exception:
        logger.error(f'{__name__}/{sys._getframe().f_code.co_name}: {traceback.format_exc()}')
        print("Error!", traceback.print_exc())

