from flask import Blueprint
from google_sheets import start_spreadsheet
from dotenv import load_dotenv
import os

p2p_parser = Blueprint(
    'p2p_parser',
    __name__
)


@p2p_parser.route("/", methods=["POST"])
def main_post():
    start_spreadsheet()


# if __name__ == '__main__':
#     load_dotenv()
#     HOST = os.getenv('HOST')
#     app.register_blueprint(p2p_parser)
#     app.run(host=HOST, port=5000)
