from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
from conexion import conectar_bd, guardar_datos

app = Flask(__name__)

# Cargar el modelo entrenado
model = joblib.load("model.pkl")

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los valores ingresados por el usuario desde el formulario web
    name = str(request.form['name'])
    gender = int(request.form['gender'])
    age = float(request.form['age'])
    hypertension = int(request.form['hypertension'])
    heart_disease = int(request.form['heart_disease'])
    smoking_history = int(request.form['smoking_history'])
    bmi = float(request.form['bmi'])
    HbA1c_level = float(request.form['HbA1c_level'])
    blood_glucose_level = float(request.form['blood_glucose_level'])

    # Realizar la predicción utilizando el modelo cargado
    data = {
        'gender': [gender],
        'age': [age],
        'hypertension': [hypertension],
        'heart_disease': [heart_disease],
        'smoking_history': [smoking_history],
        'bmi': [bmi],
        'HbA1c_level': [HbA1c_level],
        'blood_glucose_level': [blood_glucose_level]
    }

    # Convertir los datos ingresados en un DataFrame de pandas
    data_df = pd.DataFrame(data)

    # Realizar la predicción utilizando el modelo cargado
    prediction = model.predict(data_df)

    # Determinar el resultado de la predicción
    if prediction[0] == 0:
        result = "No tiene diabetes."
    else:
        result = "Tiene diabetes."

    # Guardar los datos en la base de datos
    if guardar_datos(name, gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level, result):
        print("Datos guardados correctamente en la base de datos.")
    else:
        print("Error al guardar los datos en la base de datos.")

    # Devolver el resultado de la predicción como una respuesta JSON
    return jsonify({'result': result})

# Definir la ruta para visualizar los datos de la base de datos
@app.route('/data_viewer')
def data_viewer():
    try:
        conn = conectar_bd()

        # Crea un cursor para ejecutar consultas
        cursor = conn.cursor()

        # Consulta SQL para obtener todos los datos de la tabla 'diabetes'
        sql = "SELECT * FROM diabetes"

        # Ejecuta la consulta
        cursor.execute(sql)

        # Recupera todos los registros y almacénalos en una lista de diccionarios
        data = []
        columns = [column[0] for column in cursor.description]
        for row in cursor.fetchall():
            data_row = dict(zip(columns, row))

            # Mapear valores numéricos a sus representaciones en texto
            gender_mapping = {
                0: "Masculino",
                1: "Femenino",
                2: "Otro"
            }
            data_row['gender'] = gender_mapping.get(data_row['gender'], "Desconocido")

            hypertension_mapping = {
                0: "No",
                1: "Sí"
            }
            data_row['hypertension'] = hypertension_mapping.get(data_row['hypertension'], "Desconocido")

            heart_disease_mapping = {
                0: "No",
                1: "Sí"
            }
            data_row['heart_disease'] = heart_disease_mapping.get(data_row['heart_disease'], "Desconocido")

            smoking_history_mapping = {
                0: "No actual",
                1: "Anterior",
                2: "No info",
                3: "Actual",
                4: "Nunca",
                5: "Siempre"
            }
            data_row['smoking_history'] = smoking_history_mapping.get(data_row['smoking_history'], "Desconocido")

            data.append(data_row)

        # Cierra el cursor y la conexión
        cursor.close()
        conn.close()

        # Renderiza la plantilla HTML y pasa los datos recuperados a la plantilla
        return render_template('data_viewer.html', data=data)
    except Exception as e:
        # Manejo de errores (por ejemplo, registro de errores en un archivo)
        print("Error al recuperar los datos de la base de datos:", e)
        return "Error al recuperar los datos de la base de datos."

if __name__ == '__main__':
    app.run(debug=True)

