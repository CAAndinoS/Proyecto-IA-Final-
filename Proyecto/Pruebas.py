import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import matplotlib.pyplot as plt

# Cargar y preprocesar los datos
data = pd.read_csv("https://drive.google.com/u/0/uc?id=12V9a2jg-pw0JPNngvlFIKfIqFZTXmAN8&export=download")

# Reemplazar los valores "No" y "Yes" con 0 y 1 en columnas con datos categóricos
data["gender"] = data["gender"].map({"male": 0, "female": 1, "other": 2})
data["hypertension"] = data["hypertension"].map({"No": 0, "Yes": 1})
data["heart_disease"] = data["heart_disease"].map({"No": 0, "Yes": 1})
data["smoking_history"] = data["smoking_history"].map({"not current": 0, "former": 1, "No Info": 2, "current": 3, "never": 4, "ever": 5})

# Calcular la matriz de correlación de Pearson
correlation_matrix = data.corr()

# Visualizar la matriz de correlación utilizando un mapa de calor (heatmap)
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Matriz de Correlación de Pearson")
plt.show()

# Separar características y variable objetivo
X = data.drop("diabetes", axis=1)
y = data["diabetes"]

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Obtener el número de características (campos) utilizadas para entrenar el modelo
num_train_features = X_train.shape[1]
print("Número de campos utilizados para entrenar el modelo:", num_train_features)

# Entrenar el modelo XGBoost
model = XGBClassifier(random_state=42)
model.fit(X_train, y_train, eval_set=[(X_test, y_test)], early_stopping_rounds=10, verbose=True)

# Número de épocas de entrenamiento
num_epochs = model.get_booster().best_iteration
print("Número de épocas de entrenamiento:", num_epochs)

# Evaluar el modelo en el conjunto de prueba
exactitud = model.score(X_test, y_test)
print("Exactitud del modelo en el conjunto de prueba:", exactitud)

# Obtener la importancia relativa de las características
importance_scores = model.feature_importances_

# Crear un DataFrame para visualizar las características y sus importancias
feature_importance_df = pd.DataFrame({'Feature': X_train.columns, 'Importance': importance_scores})

# Ordenar las características por importancia descendente
feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

# Visualizar las características y sus importancias en un gráfico de barras
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importance_df, palette='coolwarm')
plt.title('Importancia Relativa de las Características')
plt.xlabel('Importancia')
plt.ylabel('Característica')
plt.show()

# Mostrar la curva ROC y el AUC
from sklearn.metrics import roc_curve, roc_auc_score
y_probs = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_probs)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label='Curva ROC (AUC = {:.2f})'.format(roc_auc_score(y_test, y_probs)))
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('Tasa de Falsos Positivos (FPR)')
plt.ylabel('Tasa de Verdaderos Positivos (TPR)')
plt.title('Curva ROC')
plt.legend(loc='lower right')
plt.show()

# Mostrar la matriz de confusión
from sklearn.metrics import confusion_matrix
y_pred = model.predict(X_test)
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 6))
sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt="d", linewidths=0.5)
plt.xlabel('Predicción')
plt.ylabel('Valor Real')
plt.title('Matriz de Confusión')
plt.show()

# Mostrar la precisión, recall y f1-score
from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
print("Reporte de Clasificación:\n", report)

# Mostrar la pérdida logarítmica (log loss)
from sklearn.metrics import log_loss
logloss = log_loss(y_test, y_probs)
print("Pérdida Logarítmica (Log Loss):", logloss)

# Obtener las predicciones del modelo en el conjunto de prueba
y_pred = model.predict(X_test)

# Obtener las probabilidades de predicción para cada clase en el conjunto de prueba
probabilidades_prediccion = model.predict_proba(X_test)

# Crear una lista para almacenar los supuestos probables y sus probabilidades asociadas
supuestos_probables = []

# Recorrer las predicciones y las probabilidades para cada muestra en el conjunto de prueba
for i in range(len(y_test)):
    muestra = X_test.iloc[i]  # Obtener la muestra (características) actual
    verdadero_valor = y_test.iloc[i]  # Obtener el verdadero valor (etiqueta) de la muestra
    supuesto = y_pred[i]  # Obtener el supuesto probable (predicción) del modelo
    probabilidad_supuesto = probabilidades_prediccion[i][supuesto]  # Probabilidad asociada al supuesto probable

    # Agregar el supuesto probable y la probabilidad a la lista
    supuestos_probables.append({'Muestra': muestra, 'Verdadero Valor': verdadero_valor, 'Supuesto Probable': supuesto, 'Probabilidad': probabilidad_supuesto})

# Convertir la lista de supuestos probables a un DataFrame
supuestos_probables_df = pd.DataFrame(supuestos_probables)

# Mostrar los supuestos probables y las probabilidades asociadas
print("Supuestos probables y sus probabilidades asociadas:")
print(supuestos_probables_df)