import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

def cargar_datos(ruta):
    """Carga el dataset desde un archivo CSV."""
    return pd.read_csv(ruta)

def eliminar_duplicados(df):
    """Elimina filas duplicadas."""
    return df.drop_duplicates()

def manejar_valores_faltantes(df, estrategia='media'):
    """Completa valores faltantes (media, mediana o moda)."""
    imputer = SimpleImputer(strategy=estrategia)
    df_numerico = df.select_dtypes(include=[np.number])
    df[df_numerico.columns] = imputer.fit_transform(df_numerico)
    return df

def eliminar_outliers(df, columnas, desviaciones=3):
    """Elimina outliers usando desviación estándar."""
    for col in columnas:
        media = df[col].mean()
        std = df[col].std()
        df = df[(df[col] >= media - desviaciones * std) & 
                (df[col] <= media + desviaciones * std)]
    return df

def codificar_categoricas(df, columnas):
    """Codifica variables categóricas."""
    le = LabelEncoder()
    for col in columnas:
        df[col] = le.fit_transform(df[col])
    return df

def normalizar_datos(df, columnas):
    """Normaliza datos numéricos al rango [0, 1]."""
    scaler = StandardScaler()
    df[columnas] = scaler.fit_transform(df[columnas])
    return df

def preprocesar_completo(ruta, columnas_categoricas, columnas_numericas):
    """Pipeline completo de preprocesamiento."""
    df = cargar_datos(ruta)
    df = eliminar_duplicados(df)
    df = manejar_valores_faltantes(df)
    df = codificar_categoricas(df, columnas_categoricas)
    df = normalizar_datos(df, columnas_numericas)
    return df