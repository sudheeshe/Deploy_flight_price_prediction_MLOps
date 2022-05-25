from Src.Read_Yaml import read_params
from Src.Prediction_Validation_Insertion import PredictionValidation
from Src.Predict_From_Model import Prediction


try:
    path = read_params('params.yaml')
    print('Inside Predict method')
    pred_val_obj = PredictionValidation(path['test_data']['raw_test_dataset'])
    pred_val_obj.prediction_validation()

    predict = Prediction(path['test_data']['final_test_data'])
    predict.prediction_from_model()

    print("Prediction File created at Prediction_Output_File folder!!!")

except Exception as e:
    print(f"Error occurred while training: {e}")