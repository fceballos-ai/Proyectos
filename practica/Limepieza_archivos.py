import os
import shutil
import time

def limpiar_descargas(directorio):
    # Definimos la antigüedad (por ejemplo, archivos de más de 30 días)
    segundos_en_un_mes = 30 * 24 * 60 * 60
    limite = time.time() - segundos_en_un_mes

    print(f"Iniciando limpieza en: {directorio}")
    
    if not os.path.exists(directorio):
        print("La ruta no existe.")
        return

    for archivo in os.listdir(directorio):
        ruta_completa = os.path.join(directorio, archivo)
        
        # Verificamos si es un archivo y si es antiguo
        if os.path.isfile(ruta_completa):
            fecha_modificacion = os.path.getmtime(ruta_completa)
            
            if fecha_modificacion < limite:
                try:
                    os.remove(ruta_completa)
                    print(f"Eliminado: {archivo}")
                except Exception as e:
                    print(f"Error al eliminar {archivo}: {e}")

# Ejemplo de uso (ajusta la ruta a una carpeta de prueba)
if __name__ == "__main__":
    limpiar_descargas('./mi_carpeta_de_logs')