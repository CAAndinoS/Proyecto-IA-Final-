from conexion import conectar_bd

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
