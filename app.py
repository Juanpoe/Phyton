from flask import Flask, render_template, request
import joblib

#cargar el modelo   
model = joblib.load('models/modelo_regresion.pkl')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/predict', models=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    # obtener los valores del formulario
    Edad = float(request.form['Edad'])
    Hipertension = float(request.form['Hipertension'])
    Diabetes = float(request.form['Diabetes'])

    # Realizar un prediccion
    pred = model.predict([[Edad, Hipertension, Diabetes]])
    pred_porcentaje = pred[0]


    # definir el menaje segun el resultado de la prediccion
    return render_template('resultado.html', pred= pred_porcentaje)

if __name__ == '__main__':
    app.run()