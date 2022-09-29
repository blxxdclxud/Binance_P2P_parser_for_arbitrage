from flask import Blueprint, Flask
from google_sheets import start_spreadsheet

app = Flask(__name__)
p2p_parser = Blueprint(
    'p2p_parser',
    __name__
)


@p2p_parser.route("/post", methods=["POST"])
def main_post():
    print(11)
    start_spreadsheet()


if __name__ == '__main__':
    app.register_blueprint(p2p_parser)
    app.run(host='localhost', port=5000)
