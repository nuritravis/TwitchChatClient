import websockets
import asyncio

class Twitch_IRC:
    pass

async def h(websocket):
    name = await websocket.rcv()
    print(f'server received: name')

h("wss://eventsub.wss.twitch.tv/ws")
