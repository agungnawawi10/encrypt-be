import asyncio
from crypto.encrypt import encrypt
import websockets


async def handler(websocket):
    print("Client connected!")

    try:
        async for message in websocket:
            encrypted = encrypt(message)
            print(f"[ENCRYPTED] {encrypted}", flush=True)
            await websocket.send(encrypted)

    except Exception as e:
        print("Connection error:", e)


async def main():
    async with websockets.serve(handler, "localhost", 8765, ping_interval=None):
        print("Server running on ws://localhost:8765")
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
