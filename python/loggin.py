from connection import get_mongo_client

#Funcion de Inicio de sesión
def login(username, password):
    client = get_mongo_client()
    if client:
        db = client["ciffer"]
        col = db["users"]
        
        user = col.find_one({"user": username, "password": password})
        if user:
            print("Inicio de sesión exitoso")
            return True
        else:
            print("Usuario o contraseña incorrectos")
            return False
    else:
        print("No se pudo conectar a la base de datos")
        return False
    
#Probar la función de inicio de sesión
if __name__ == "__main__":
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    login(username, password)