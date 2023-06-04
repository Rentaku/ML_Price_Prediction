import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from tensorflow import keras
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from flask import Flask, request, jsonify

model = keras.models.load_model("best_model.h5")

def prepare_data(mileage, manufacture, model, category, year, gear_box_type):
    # Input nilai untuk setiap fitur
    input_value0 = str(mileage)
    input_value1 = str(manufacturer)
    input_value2 = str(model)
    input_value3 = str(category)
    input_value4 = str(year)
    input_value5 = str(gear_box_type)

    column_names1 = normalized_df.columns[1:31]  # Nama-nama kolom
    column_names2 = normalized_df.columns[31:1597]
    column_names3 = normalized_df.columns[1597:1608]
    column_names4 = normalized_df.columns[1608:1629]
    column_names5 = normalized_df.columns[1629:1633]

    features = [input_value0] + \
               [1 if col == input_value1 else 0 for col in column_names1] + \
               [1 if col == input_value2 else 0 for col in column_names2] + \
               [1 if col == input_value3 else 0 for col in column_names3] + \
               [1 if col == input_value4 else 0 for col in column_names4] + \
               [1 if col == input_value5 else 0 for col in column_names5

    return features

def predict(x):
    scaler = MinMaxScaler()
    data_predict = scaler.transform([x])
    predictions = model.predict(data_predict)
    return predictions

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    if request.method == "POST":
        try:
            input_data = request.get_json()
            if not input_data:
                return jsonify({"error": "no data"})

            feature1 = input_data.get('feature1')
            feature2 = input_data.get('feature2')
            feature3 = input_data.get('feature3')
            feature4 = input_data.get('feature4')
            feature5 = input_data.get('feature5')
            feature6 = input_data.get('feature6')
            features = prepare_data(feature1, feature2, feature3, feature4, feature5, feature6)
            prediction = predict(features)

            data = {"prediction": prediction}
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)})
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)