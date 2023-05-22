import os
from pymongo import MongoClient
import whisper

# Establecer la conexión con la base de datos MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['whisper_db']
collection = db['whisper_results']

# Cargar el modelo de Whisper
model = whisper.load_model("base")

# Directorio de los archivos MP4
directorio = input("Ingresa el directorio: ")
print(directorio)


def procesar_archivo(filepath):
    # Obtener la lista de videos en la base de datos
    videos_en_db = set([documento['archivo'] for documento in collection.find()])
    
    # Verificar si el video ya está en la base de datos
    if os.path.basename(filepath) in videos_en_db:
        print(f"El archivo {filepath} ya tiene una transcripción en la base de datos. Ignorando...")
        return
    
    # Procesar el archivo con Whisper
    result = model.transcribe(filepath, fp16=False)
    resultado_whisper = result["text"]
    
    # Crear un documento con el resultado y otros metadatos
    documento = {
        'archivo': os.path.basename(filepath),
        'directorio': os.path.dirname(filepath),
        'resultado_whisper': resultado_whisper
    }
    
    # Insertar el documento en la base de datos
    collection.insert_one(documento)
    print(f"Archivo {filepath} procesado con Whisper. Resultado: {resultado_whisper}")


# Iterar por cada archivo MP4 en el directorio y subdirectorios
for root, dirs, files in os.walk(directorio):
    for filename in files:
        if filename.endswith('.mp4'):
            # Ruta completa del archivo
            filepath = os.path.join(root, filename)
            
            # Procesar el archivo con Whisper
            procesar_archivo(filepath)
