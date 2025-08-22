import asyncio, websockets, json

async def get_speed():
    uri = "ws://192.168.88.78:8888"
    async with websockets.connect(uri) as websocket:
        get_request = {
            "action": "get",
            "path": "Vehicle.Cabin.Light.AmbientLight.Row1.DriverSide.IsLightOn",
            "requestId": "get-speed-1"
        }
        await websocket.send(json.dumps(get_request))
        response = await websocket.recv()
        data = json.loads(response)
        print("Current Vehicle.Cabin.Light.AmbientLight.Row1.DriverSide.IsLightOn:", data.get("value"))

asyncio.run(get_speed())
