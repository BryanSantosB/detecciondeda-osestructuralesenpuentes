import pandas as pd

# Cargar el archivo Excel
archivo_excel = r'C:\Users\Bryan Santos\Desktop\Bryan\10MO CICLO\Capstone Project\tesis_analizadas.xlsx'
df = pd.read_excel(archivo_excel)


# Función para calificar cada tesis según los indicadores
def calificar_tesis(row):
    puntaje_total = 0

    # Indicadores metodológicos (20%)
    metodologicos = {'Tipo de investigación': 5.0, 'Enfoque': 5.0, 'Nivel (alcance)': 5.0,
                     'Diseño de investigación': 5.0}
    for indicador, peso in metodologicos.items():
        puntaje_total += peso if pd.notnull(row[indicador]) else 0

    # Innovación tecnológica (20%)
    innovacion = {'Desarrollo de software': 1.5, 'Tecnologías emergentes': 5.0,
                  'Validación de modelos': 3.5, 'Marcos de referencias': 5.0,
                  'Validación del producto': 5.0}
    for indicador, peso in innovacion.items():
        puntaje_total += peso if row[indicador] == 'SI' else 0

    # Frecuencia de técnicas e instrumentos de recolección de datos (20%)
    recoleccion_datos = {'Encuestas': 1.0, 'Observación/Registro de datos': 18.0, 'Entrevistas': 1.0}
    for indicador, peso in recoleccion_datos.items():
        puntaje_total += peso if row[indicador] == 'SI' else 0

    # Resultados y discusión (20%)
    resultados = {'Aplicación de pruebas estadísticas': 5.0, 'Métricas de rendimiento': 7.0,
                  'Relevantes y aportan a la ciencia y tecnología': 8.0}
    for indicador, peso in resultados.items():
        puntaje_total += peso if row[indicador] == 'SI' else 0

    # Indicadores de citación (20%) - Asignamos el puntaje completo
    puntaje_total += 20.0

    return puntaje_total


# Calificar cada tesis
df['Puntaje Total'] = df.apply(calificar_tesis, axis=1)

# Generar estadísticas
promedio_calidad = df['Puntaje Total'].mean()
num_tesis_alta_calidad = df[df['Puntaje Total'] >= 80].shape[0]
porcentaje_alta_calidad = (num_tesis_alta_calidad / df.shape[0]) * 100

print("Promedio de calidad de tesis:", promedio_calidad)
print("Número de tesis de alta calidad (≥ 80):", num_tesis_alta_calidad)
print(f"Porcentaje de tesis de alta calidad: {porcentaje_alta_calidad:.2f}%")
