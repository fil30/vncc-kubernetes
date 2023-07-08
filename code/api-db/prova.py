from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://username:password@hostname/db')

Session = sessionmaker(bind=engine)
session = Session()

result = session.query(MyTable).filter_by(name='John').all()

class model(Base):
    __tablename__ = 'car_list'
    
    id = Column(Integer, primary_key=True)
    car_make = Column(String(50))
    car_model = Column(String(50))
    prod_year = Column(Integer)
    engine_size = Column(String(50))
    horsepower = Column(String(50))
    torque = Column(String(50))
    speed = Column(String(50))
    price = Column(Integer)










from flask import Flask
from sqlalchemy import *

app = Flask(__name__)

SQLALCHEMY_DATABASE_URI = "mysql://user:password@db"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Create a route
@app.route('/get_cars', methods=['GET'])

def get_all_cars():
    with get_session() as db:
        all_cars = db.query(list_cars).all()
        return jsonify(all_cars)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")