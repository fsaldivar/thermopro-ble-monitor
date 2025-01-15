import asyncio
from bleak import BleakScanner

async def scan_ble_devices():
    print("Escaneando dispositivos BLE cercanos...")
    devices = await BleakScanner.discover()
    if devices:
        print("Dispositivos BLE encontrados:")
        for device in devices:
            print(f"Dirección: {device.address} - Nombre: {device.name}")
    else:
        print("No se encontraron dispositivos BLE.")

asyncio.run(scan_ble_devices())
