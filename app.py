from flask import Flask

from csv_to_json import CsvToJson

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/csv/to/json/keyed')
def csv_to_json_keyed():
    raw_csv = open("samples/TileData.csv", "r")
    csv_to_json = CsvToJson()
    json_output = csv_to_json.keyed_csv_to_array(raw_csv.read().splitlines())
    return json_output


if __name__ == '__main__':
    app.run()
