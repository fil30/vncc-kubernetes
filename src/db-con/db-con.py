# Retrieve data from the database and return them in json format

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@datab/datab'
db = SQLAlchemy(app)
CORS(app)

class Car(db.Model):
    __tablename__ = 'car_list'
    Id = db.Column(db.Integer, primary_key=True)
    Car_Make = db.Column(db.String(13), nullable=False)
    Car_Model = db.Column(db.String(29), nullable=False)
    Production_Year = db.Column(db.Integer, nullable=False)
    Engine_Size_L = db.Column(db.String(20), nullable=False)
    Horsepower = db.Column(db.String(7), nullable=False)
    Torque_lbft = db.Column(db.String(7), nullable=False)
    MPH_Time_seconds = db.Column(db.String(5), nullable=False)
    Price_in_USD = db.Column(db.Integer, nullable=False)

@app.route('/get_car_data', methods=['GET'])
def get_car_data():
    try:
        car_data = Car.query.all()
        car_data_list = []
        for car in car_data:
            car_data_list.append({
                'Id': car.Id,
                'Car_Make': car.Car_Make,
                'Car_Model': car.Car_Model,
                'Production_Year': car.Production_Year,
                'Engine_Size_L': car.Engine_Size_L,
                'Horsepower': car.Horsepower,
                'Torque_lbft': car.Torque_lbft,
                'MPH_Time_seconds': car.MPH_Time_seconds,
                'Price_in_USD': car.Price_in_USD
            })
        return jsonify(car_data_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)