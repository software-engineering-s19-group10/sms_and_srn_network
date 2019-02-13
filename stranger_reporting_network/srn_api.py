from flask import Flask, request
import stranger_reporting_network.reporting as reporting
import json

app = Flask(__name__)


@app.route("/post_coords", methods=['POST'])
def post(request):
    lat = request.args.get('lat')
    long = request.args.get('long')
    reporting.report_stranger(lat, long, severity=1)

@app.route("/get_closest", methods=['POST'])
def get_closest(request):
    lat = request.args.get('lat')
    long = request.args.get('long')
    return json.dumps(reporting.send_closest_srn(lat, long))


if __name__ == "__main__":
    app.run(debug=True)