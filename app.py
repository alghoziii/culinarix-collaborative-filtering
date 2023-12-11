import os
from flask import Flask, jsonify, redirect
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd

app = Flask(__name__)

culinary_data = pd.read_csv("https://storage.googleapis.com/dataset-culinarix/culinary_dataset.csv")
dataset_path = "https://storage.googleapis.com/dataset-culinarix/culinary_rating.csv"  # Mengganti os.path.join
rating = pd.read_csv(dataset_path)
model = load_model("recommendation_rating_model.h5", compile=False)

@app.route("/")
def index():
    return jsonify({
        "status": {
            "code" : 200,
            "message": "Success fetching the API"
        },
        "data": None
    }), 200

@app.route("/prediction/<int:User_Id>", methods=["GET"])
def prediction(User_Id):
        # Cek apakah user_id berada dalam rentang 1-200
    if 1 <= User_Id <= 200:
        id_user = User_Id
    else:
        # Jika di luar rentang, arahkan ke endpoint /top-rated
        return redirect("/top-rated")
    
    id_place = range(1, 20)
    place_data = np.array(list(set(rating.Place_Id)))
    place_data[:10]

    id_user = User_Id
    user = np.array([id_user for _ in range(len(place_data))])  # Mengganti variabel yang tidak digunakan

    predictions = model.predict([user.reshape(-1, 1), place_data.reshape(-1, 1)])
    predictions = np.array([a[0] for a in predictions])
    recommended_place_ids = (-predictions).argsort()[:10].tolist()

    recommended_places = culinary_data[culinary_data['Place_Id'].isin(recommended_place_ids)][
        ['Place_Id', 'Place_Name', 'Culinary_Ratings', 'Category', 'Address', 'Description', 'Coordinate', 'Lat', 'Long', 'Gmaps_Address', 'Image_Address']
    ].to_dict(orient='records')

    response_json = {
        "user_id": id_user,
        "recommended_places": recommended_places
    }
    return jsonify(response_json)

# API endpoint untuk mendapatkan restoran dengan rating tertinggi
@app.route('/top-rated', methods=['GET'])
def get_top_rated_places():
    try:
        top_rated_places = culinary_data.sort_values(by='Culinary_Ratings', ascending=False).head(10)
        response = {
            'status': 'SUCCESS',
            'message': 'Restoran dengan Rating Tertinggi',
            'top_rated_places': top_rated_places.to_dict(orient='records')
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'status': 'ERROR', 'message': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
