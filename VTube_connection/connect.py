import asyncio
import websockets
import json

async def main():

    # Set local port
    uri = "ws://localhost:6666"
    async with websockets.connect(uri) as ws:
        
        # Auth request
        await ws.send(json.dumps({
            "apiName": "VTubeStudioPublicAPI",
            "apiVersion": "1.0",
            "requestID": "1",
            "messageType": "Authentication",
            "message": {
                "clientKey": "YOUR_PASSWORD_HERE"
            }
        }))
        response = await ws.recv()
        print(response)

asyncio.run(main())