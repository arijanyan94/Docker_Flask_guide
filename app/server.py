from flask import Flask, request, Response
import jsonpickle
import pandas as pd
from ofcom_internet import run

df_internet = pd.read_csv('ofcom_broadband_2021-05.txt')
df_internet.drop(df_internet.filter(regex="Unname"),axis=1, inplace=True)
internet_columns = [
                     'max_adsl_predicted_down',
                     'max_adsl_predicted_up',
                     'max_sfbb_predicted_down',
                     'max_sfbb_predicted_up',
                     'max_ufbb_predicted_down',
                     'max_ufbb_predicted_up',
                     'adsl_availability',
                     'sfbb_availability',
                     'ufbb_availability']

# Initialize the Flask application
app = Flask(__name__)

@app.route('/api/process', methods=['POST'])
def process():
    try:
        req = request
        result = run(req.data, internet_columns, df_internet)
    except Exception as e:
        response = {'message': 'Error was generated {}'.format(e)}
        response_pickled = jsonpickle.encode(response)

        return Response(response=response_pickled, status=500, mimetype="application/json")

    # build a response dict to send back to client
    response = {'message': result}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")

# Change the hosting address to the one of your server and the port
app.run(host='0.0.0.0', port=8060)
