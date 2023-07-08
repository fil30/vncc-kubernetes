from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'db'

mysql = MySQL(app)

@app.route('/get_cars', methods=['GET'])
def get_data():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()

        # Execute your SQL query here
        cursor.execute("SELECT * FROM car_list")

        # Fetch all rows from the query result
        rows = cursor.fetchall()

        # Create a list to hold the serialized data
        data = []

        # Loop through each row and create a dictionary based on your data model
        for row in rows:
            # Assuming you have columns 'id', 'name', and 'age' in your table
            data.append({
                'id': row[0],
                'car_make': row[1],
                'car_model': row[2],
                'prod_year': row[3],
                'engine_size': row[4],
                'horsepower': row[5],
                'torque': row[6],
                'acceleration': row[7],
                'price': row[8],
            })

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Serialize the data and return as JSON response
        return jsonify(data)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")