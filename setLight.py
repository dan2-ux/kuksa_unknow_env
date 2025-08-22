import asyncio
import websockets
import json

async def set_led():
    uri = "ws://192.168.88.78:8888"  # Replace with your server IP if needed

    async with websockets.connect(uri) as websocket:
        # Turn LED on
        set_on = {
            "action": "set",
            "path": "Vehicle.Cabin.Light.AmbientLight.Row1.DriverSide.IsLightOn",
            "value": True,
            "requestId": "led-on-1"
        }
        await websocket.send(json.dumps(set_on))
        response = await websocket.recv()
        print("LED On response:", response)

        # Set LED color to red
        set_color = {
            "action": "set",
            "path": "Vehicle.Cabin.Light.AmbientLight.Row1.DriverSide.Color",
            "value": 0xffffffff,
            "requestId": "led-color-1"
        }
        await websocket.send(json.dumps(set_color))
        response = await websocket.recv()
        print("LED Color response:", response)

        # Set LED intensity to 50
        set_intensity = {
            "action": "set",
            "path": "Vehicle.Cabin.Light.AmbientLight.Row1.DriverSide.Intensity",
            "value": 50,
            "requestId": "led-intensity-1"
        }
        await websocket.send(json.dumps(set_intensity))
        response = await websocket.recv()
        print("LED Intensity response:", response)

if __name__ == "__main__":
- setLight.py 36/44 81%
