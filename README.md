# culinarix-collaborative-filtering

## Overview

This Flask-based API provides restaurant recommendations and information based on user_id making recommendations for users after logging in from the application. This provides predictions based on user_id from a machine learning model to display restaurant details

## Endpoints

### Get prediction

#### Endpoint:

`GET /prediction/<user_id>`

#### Description:

This endpoint provides restaurant recommendations based on the user_id entered. If user_id is not found, it will display a query based on the highest restaurant rating

#### Request:


#### Response:

![image](https://github.com/alghoziii/culinarix-collaborative-filtering/assets/91893301/e9eed979-e47b-4b3b-b50c-e68dbf377398)


- Status: 200 OK
- Content: JSON
  - `user_id` (int):  example user_id who is logged in to the application
  - `recommended_places` (array of objects): An array of recommended places with details.

### Get Top-Rated Restaurants

#### Endpoint:

`GET /top-rated`

#### Description:

This endpoint retrieves the top-rated restaurants based on culinary ratings.

#### Response:

![image](https://github.com/alghoziii/culinarix-collaborative-filtering/assets/91893301/a1535c52-4b0d-468e-9db3-3316564f8f1d)


- Status: 200 OK
- Content: JSON
  - `status` (string): "SUCCESS" or "ERROR"
  - `message` (string): A message describing the status
  - `top_rated_places` (array of objects): An array of top-rated places with details.

## Technologies Used

- Python
- Flask
- tensorflow
- numpy
- pandas

## Usage

1. Clone the repository:

   ```bash
   git clone [https://github.com/LeeVonks/content-based.git](https://github.com/alghoziii/culinarix-collaborative-filtering.git)

   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the API:
   ```bash
   flask run
