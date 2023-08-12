# Sistema de Predicción y Gestión de Datos de Diabetes

Este repositorio contiene el código para un Sistema de Predicción y Gestión de Datos de Diabetes. El sistema utiliza un modelo de aprendizaje automático para predecir si un individuo tiene diabetes en función de varias características de entrada. También incluye funcionalidad para almacenar y ver los datos recopilados en una base de datos. El sistema está construido utilizando Python, Flask, Pandas, XGBoost y MySQL.

## Instalación

Antes de ejecutar la aplicación, asegúrate de tener las dependencias necesarias instaladas en tu sistema Linux:


Bibliotecas de Python
```bash
pip install pandas scikit-learn xgboost joblib flask mysql-connector-python
```
## Base de Datos MySQL
Necesitas tener un servidor de base de datos MySQL instalado y en funcionamiento. Crea una base de datos llamada proyecto y configura los ajustes de conexión a la base de datos en el archivo conexion.py.
## Uso
Carga y procesa los datos para el modelo de aprendizaje automático ejecutando el script:
```bash
python preprocess_data.py
```
Entrena el modelo XGBoost ejecutando:
```bash
python train_model.py
```
Inicia la aplicación web de Flask para utilizar el sistema de predicción y gestión de datos:
```bash
python app.py
```
Esto iniciará un servidor de desarrollo, y podrás acceder a la aplicación en tu navegador web visitando http://localhost:5000.

Utiliza la interfaz web para ingresar la información del paciente y obtener predicciones de diabetes.

La aplicación también proporciona una interfaz para ver los datos almacenados en la base de datos. Accede a la visor de datos visitando http://localhost:5000/data_viewer.

## Archivos
reprocess_data.py: Carga y procesa el conjunto de datos para entrenar el modelo.

train_model.py: Entrena el modelo XGBoost con los datos preprocesados y lo guarda como model.pkl.

conexion.py: Proporciona funciones para conectarse a la base de datos MySQL.

app.py: Contiene la aplicación Flask para la interfaz web, predicciones y gestión de datos.

templates/: Directorio que contiene plantillas HTML para la aplicación web.

## Nota
Reemplaza los detalles de conexión a la base de datos MySQL en conexion.py con tu configuración de base de datos real.

Este README asume que estás utilizando un sistema basado en Linux. Ajusta las instrucciones de instalación y uso para otras plataformas según sea necesario.

## Descargo de Responsabilidad
Este sistema se proporciona con fines educativos y de demostración únicamente. No debe considerarse como asesoramiento médico ni utilizarse para tomar decisiones médicas reales. Las predicciones realizadas por el modelo de aprendizaje automático pueden no ser precisas y no deben reemplazar las opiniones médicas profesionales.

Este README asume que estás utilizando un sistema basado en Linux. Ajusta las instrucciones de instalación y uso para otras plataformas según sea necesario.
