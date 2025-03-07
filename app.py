from flask import Flask, request, render_template, jsonify, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import tensorflow as tf
from PIL import Image
import numpy as np
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

model_path = os.path.join('D:\\', 'MiniP', 'model', 'vggbest_model.keras')
model = tf.keras.models.load_model(model_path)

def preprocess_image(image):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  # Store password as plain text

        if User.query.filter_by(username=username).first():
            flash('Username already exists')
            return redirect(url_for('signup'))

        new_user = User(username=username, password=password)  # No hashing here
        db.session.add(new_user)
        db.session.commit()
        flash('Signup successful. Please login.')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.password == password:  # Plain text comparison
            session['user_id'] = user.id
            flash('Login successful')
            return redirect(url_for('prediction'))
        else:
            flash('Invalid credentials')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Logged out successfully')
    return redirect(url_for('landing'))

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if 'user_id' not in session:
        flash('Please log in to access this page')
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    username = user.username

    prediction = None
    if request.method == 'POST':
        file = request.files['file']
        if file:
            img = Image.open(file)
            processed_img = preprocess_image(img)
            
            result = model.predict(processed_img)
            predicted_class = np.argmax(result)
            classes = ['A+', 'A-', 'AB+', 'AB-', 'B+', 'B-', 'O+', 'O-']
            prediction = classes[predicted_class]

            return jsonify({'prediction': prediction})
    
    return render_template('prediction.html', prediction=prediction, username=username)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
