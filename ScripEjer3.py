import pandas as pd


# Cargar dataset
datos = pd.read_csv("C:\\Users\\Alumno\\PycharmProjects\\WelcomeScreen\\housing.csv")

print("Valores nulos:")
print(datos.isnull().sum())

# Eliminar valores nulos
datos = datos.dropna()

print("\nDataset despues de eliminar valores nulos:")
print(datos.shape)