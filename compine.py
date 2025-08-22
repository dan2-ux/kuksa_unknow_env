import asyncio
import websockets
import json
import board
import neopixel_spi as neopixel
import busio

NUM_PIXELS = 60
PIXEL_ORDER = neopixel.GRB

last_state = None
base_colour = 0xFF0000
base_inten = 100

def apply_intensity(color, intensity):
    intensity = max(0.0, min(1.0, intensity))
    r = int(((color >> 16) & 0xFF) * intensity)
    g = int(((color >> 8) & 0xFF) * intensity)
    b = int((color & 0xFF) * intensity)
    return (r << 16) | (g << 8) | b

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)

pixels = neopixel.NeoPixel_SPI(
    spi,
    NUM_PIXELS,
    pixel_order=PIXEL_ORDER,
    auto_write=False,
)

# Initialize the state variable
past_state = None
uri = "ws://192.168.88.78:8888"

async def get_ambient_data():
    global past_state, uri
    
    async with websockets.connect(uri) as websocket:
        get_request = {
            "action": "get",
            "path": "Vehicle.Cabin.Light.AmbientLight.Row1.DriverSide.IsLightOn",
            "requestId": "get-ambient-1"
        }
        
        await websocket.send(json.dumps(get_request))
        response = await websocket.recv()
        data = json.loads(response)
        current_state = data.get("value")

        # Check if the state has changed
        if current_state != past_state:
            print(f"Ambient Light State: {'On' if current_state else 'Off'}")
            
            # Update the NeoPixel based on the new state
            if current_state:
                pixels.fill(apply_intensity(base_colour, base_inten))
            else:
                pixels.fill(apply_intensity(base_colour, 0))  # Set intensity to 0 if the light is off
                
            pixels.show()
            
            # Update the past_state to current_state
            past_state = current_state

async def main():
    while True:
        await get_ambient_data()
        await asyncio.sleep(1)  # Adding a small delay to avoid spamming requests

# Run the event loop
asyncio.run(main())
