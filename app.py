from flask import Flask, request

from csv_to_json import CsvToJson

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/csv/to/json/keyed', methods=["POST", "GET"])
def csv_to_json_keyed():
    if request.method == "GET":
        raw_csv = open("samples/TileData.csv", "r")
        raw_csv_data = raw_csv.read()
    if request.method == "POST":
        raw_csv_data = request.data.decode("utf-8")
    csv_to_json = CsvToJson(raw_csv_data.splitlines())
    json_output = csv_to_json.keyed_csv_to_array()
    return json_output


if __name__ == '__main__':
    app.run()
