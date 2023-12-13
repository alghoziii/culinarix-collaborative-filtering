# culinarix-collaborative-filtering

## Overview

This Flask-based API provides restaurant recommendations and information based on User_Id making recommendations for users after logging in from the application. This provides predictions based on User_Id from a machine learning model to display restaurant details

## Endpoints

**Base URL :**

> https://culinarix-collaborative-filtering-6lmjk4zvdq-as.a.run.app

### Get prediction

#### Endpoint:

`GET /prediction/<User_Id>`

#### Description:

This endpoint provides restaurant recommendations based on the User_Id entered. If User_Id is not found, it will display a query based on the highest restaurant rating


#### Response:

![image](https://github.com/alghoziii/culinarix-collaborative-filtering/assets/91893301/e9eed979-e47b-4b3b-b50c-e68dbf377398)


- Status: 200 OK
- Content: JSON
  - `User_Id` (int):  example User_Id who is logged in to the application
  - `recommended_places` (array of objects): An array of recommended places with details.

### Get Top-Rated Restaurants

#### Endpoint:

`GET /top-rated`

#### Description:

This endpoint is used if the user_id does not exist then takes the restaurant with the top ranking based on the culinary ranking.

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
   https://github.com/alghoziii/culinarix-collaborative-filtering.git

   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the API:
   ```bash
   flask run
