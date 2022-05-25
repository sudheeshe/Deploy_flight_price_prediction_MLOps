import json
import os
from wsgiref import simple_server
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import Response
import flask_monitoringdashboard as dashboard
from Src.Read_Yaml import read_params
from flask_cors import CORS, cross_origin
from Src.Prediction_Validation_Insertion import PredictionValidation
from Src.Predict_From_Model import Prediction


app = Flask(__name__)
dashboard.bind(app)
CORS(app)


@app.route("/", methods = ['GET'])
@cross_origin()
def home():
    return "Welcome to Flight Price Prediction home page"


@app.route("/predict", methods = ['GET'])
@cross_origin()
def predict_route_client():

    try:
        path = read_params('params.yaml')
        print('Inside Predict method')
        pred_val_obj = PredictionValidation(path['test_data']['raw_test_dataset'])
        pred_val_obj.prediction_validation()

        predict = Prediction(path['test_data']['final_test_data'])
        prediction = predict.prediction_from_model()

        return Response(str(json.loads(prediction)))

    except Exception as e:
        return f"Error occurred while prediction: {e}"

port = int(os.getenv("PORT", 5000))

if __name__ == "__main__":
    host = '0.0.0.0'
    httpd = simple_server.make_server(host=host, port=port, app=app)
    httpd.serve_forever()