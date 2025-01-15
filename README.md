# ThermoPro BLE Monitor

Monitoriza los datos de temperatura y humedad en tiempo real desde el dispositivo ThermoPro TP359 utilizando Python y BLE (Bluetooth Low Energy).

## 📖 Descripción
Este proyecto IoT permite conectarte al dispositivo **ThermoPro TP359** vía Bluetooth para obtener los valores de temperatura y humedad. Utiliza la biblioteca `bleak` para escanear y conectarse al dispositivo, habilitando notificaciones para procesar y mostrar los datos en tiempo real.

## 🛠️ Requisitos
Antes de comenzar, asegúrate de tener lo siguiente:

- Python 3.7 o superior
- Un dispositivo ThermoPro TP359
- Un adaptador Bluetooth compatible con BLE
- Librerías necesarias:
  - `bleak`
  - `asyncio`

## 🚀 Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/thermopro-ble-monitor.git
   cd thermopro-ble-monitor
   ```

2. **Instala las dependencias:**
   ```bash
   pip install bleak
   ```

3. **Conecta el dispositivo:**
   - Asegúrate de que el dispositivo ThermoPro TP359 esté encendido y dentro del rango del adaptador Bluetooth.

## 📂 Archivos

- **`BLE_Search.py`**: Escanea dispositivos BLE cercanos y muestra sus direcciones y nombres.
- **`BLE_Data.py`**: Se conecta al dispositivo, habilita notificaciones y muestra los datos de temperatura y humedad en tiempo real.

## 🖥️ Uso

1. **Escanea los dispositivos BLE cercanos:**
   ```bash
   python BLE_Search.py
   ```
   Nota: Busca el dispositivo llamado `TP359` y toma nota de su dirección (por ejemplo, `FB:E7:C4:CF:3A:F6`).

2. **Obtén los datos de temperatura y humedad:**
   - Actualiza la variable `device_address` en `BLE_Data.py` con la dirección del dispositivo encontrada.
   - Ejecuta el script:
     ```bash
     python BLE_Data.py
     ```

   - Los datos se imprimirán en consola cada minuto en formato JSON.

## 📝 Ejemplo de Salida

```json
{
  "Timestamp": "2025-01-15T10:00:00",
  "Temperature": 23.5,
  "Humidity": 45
}
```

## 📚 Recursos

- [ThermoPro TP359 en Amazon](https://www.amazon.com.mx/ThermoPro-Term%C3%B3metro-inal%C3%A1mbrico-habitaciones-temperatura/dp/B08J7VXPLV)
- [Documentación de Bleak](https://github.com/hbldh/bleak)

## 🤝 Contribuciones
¡Contribuciones son bienvenidas! Si tienes ideas para mejorar este proyecto, abre un issue o envía un pull request.

## 📜 Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
