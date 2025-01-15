import asyncio
import json
from datetime import datetime
from bleak import BleakClient
from bleak.exc import BleakDeviceNotFoundError

# Dirección del dispositivo BLE al que deseas conectarte
device_address = "FB:E7:C4:CF:3A:F6"

# Variable global para almacenar el último dato recibido
last_data = None

# Función para manejar notificaciones
def notification_handler(sender, data):
    global last_data
    try:
        # Leer la humedad (confirmada en posición 5)
        humidity = data[5]

        # Leer la temperatura (posiciones 3-4, tamaño 2, escala 1/10, orden little)
        temperature = int.from_bytes(data[3:5], byteorder="little", signed=True) / 10

        # Obtener el timestamp actual
        timestamp = datetime.now().isoformat()

        # Guardar el último dato recibido en formato JSON
        last_data = {
            "Timestamp": timestamp,
            "Temperature": round(temperature, 1),
            "Humidity": humidity
        }
    except Exception as e:
        print(f"Error al procesar datos: {e}")

# Función para imprimir el último dato cada minuto
async def print_last_data():
    while True:
        await asyncio.sleep(60)  # Esperar 60 segundos
        if last_data:
            print(json.dumps(last_data, indent=2))

# Función principal para habilitar notificaciones
async def enable_notifications(address):
    while True:  # Intentar reconectar indefinidamente en caso de error
        try:
            async with BleakClient(address) as client:
                print(f"Conectado a {address}")
                # Habilitar notificaciones solo para la característica relevante
                char_uuid = "00010203-0405-0607-0809-0a0b0c0d2b10"
                await client.start_notify(char_uuid, notification_handler)
                print(f"Notificaciones habilitadas para {char_uuid}")
                
                # Ejecutar la tarea de impresión en paralelo
                await print_last_data()
        except BleakDeviceNotFoundError:
            print(f"Dispositivo {address} no encontrado. Reintentando en 5 segundos...")
            await asyncio.sleep(5)  # Esperar antes de reintentar
        except Exception as e:
            print(f"Error inesperado: {e}. Reintentando en 5 segundos...")
            await asyncio.sleep(5)  # Esperar antes de reintentar

# Ejecutar el programa
asyncio.run(enable_notifications(device_address))
