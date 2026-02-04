import requests # pyright: ignore[reportMissingModuleSource]

def obtener_clima(ciudad):
    # Usamos una API gratuita (requiere registro, pero aquí usamos un ejemplo educativo)
    API_KEY = "9c216ad30f4189183a77d9bab672ef1d" 
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={API_KEY}&units=metric&lang=es"

    try:
        respuesta = requests.get(URL)
        datos = respuesta.json()

        if respuesta.status_code == 200:
            temp = datos['main']['temp']
            clima = datos['weather'][0]['description']
            print(f"--- Reporte para {ciudad} ---")
            print(f"Temperatura: {temp}°C")
            print(f"Condición: {clima}")
        else:
            print(f"Error: No se pudo encontrar la ciudad (Código {respuesta.status_code})")
            
    except Exception as e:
        print(f"Ocurrió un error de conexión: {e}")

# Para ejecutarlo, primero instala la librería: pip install requests
if __name__ == "__main__":
    obtener_clima("Madrid")