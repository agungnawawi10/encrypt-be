import asyncio
import websockets


async def handler(websocket):
    print("Client connected")

    async for message in websocket:
        print(f"[RECEIVED]{message}", flush=True)


async def main():
    async with websockets.serve(handler, "localhost", 8765, ping_interval=None):
        print("Server running on ws://localhost:8765")
        await asyncio.Future()


asyncio.run(main())
