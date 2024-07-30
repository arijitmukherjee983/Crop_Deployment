from flask import Flask, request, render_template
import numpy as np
import pickle
import sqlite3

# Load the model
model = pickle.load(open('model_new.pkl', 'rb'))

# Create Flask app
app = Flask(__name__)


# Initialize the SQLite database
def init_db():
    with sqlite3.connect('responses.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS responses (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_response TEXT
                        )''')
        conn.commit()


# Call init_db to ensure the database and table are created
init_db()


@app.route('/')
def index():
    return render_template('index1.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        N = int(request.form['Nitrogen'])
        P = int(request.form['Phosphorus'])
        K = int(request.form['Potassium'])
        temp = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['pH'])
        rainfall = float(request.form['Rainfall'])

        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        prediction = model.predict(single_pred)

        crop_dict = {
            1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
            8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
            14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
            19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
        }

        if prediction[0] in crop_dict:
            crop = crop_dict[prediction[0]]
            result = "{} is the best crop to be cultivated right there".format(crop)
        else:
            result = "Sorry, we could not determine the best crop to be cultivated with the provided data."

    except Exception as e:
        result = f"An error occurred: {e}"

    return render_template('index1.html', result=result)


@app.route('/response', methods=['POST'])
def response():
    user_response = request.form['UserResponse']
    try:
        with sqlite3.connect('responses.db') as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO responses (user_response) VALUES (?)", (user_response,))
            conn.commit()
        response_message = "Thank you for your feedback!"
    except Exception as e:
        response_message = f"An error occurred: {e}"

    return render_template('index1.html', response_message=response_message)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


# Python main
if __name__ == '__main__':
    app.run(debug=True)
