import mysql.connector

def conectar_bd():
    # Configura los datos de conexión a la base de datos
    config = {
        'user': 'caas',
        'password': 'admin1234',
        'host': 'localhost',
        'database': 'proyecto'
    }

    try:
        # Crea la conexión a la base de datos
        conn = mysql.connector.connect(**config)
        return conn
    except mysql.connector.Error as err:
        # En caso de error, muestra el mensaje de error y devuelve None
        print("Error al conectar a la base de datos:", err)
        return None

def guardar_datos(name, gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level, diabetes):
    try:
        conn = conectar_bd()

        # Crea un cursor para ejecutar consultas
        cursor = conn.cursor()

        # Prepara la consulta SQL para insertar los datos en la tabla de la base de datos
        sql = "INSERT INTO diabetes (name, gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level, diabetes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (name, gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level, diabetes)

        # Ejecuta la consulta
        cursor.execute(sql, valores)

        # Confirma la operación y cierra el cursor y la conexión
        conn.commit()
        cursor.close()
        conn.close()

        return True
    except Exception as e:
        # Manejo de errores (por ejemplo, registro de errores en un archivo)
        print("Error al guardar en la base de datos:", e)
        return False

