from pymongo import MongoClient
from tenacity import retry, stop_after_attempt, wait_fixed

# Reemplaza con tu cadena de conexión de MongoDB Atlas
MONGODB_URI = "mongodb+srv://brianlopez7475:<password>@cluster0.jpyadpc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def get_mongo_client():
    try:
        client = MongoClient(MONGODB_URI)
        # Prueba la conexión
        client.admin.command('ping')
        print("Conexión exitosa a MongoDB Atlas")
        return client
    except Exception as e:
        print(f"Error al conectar a MongoDB Atlas: {e}")
        raise
