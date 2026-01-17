import websockets
import asyncio

OAUTH_TOKEN = "trcg86uh0afabbjnm9cbs6dy3ni9ss"      
USERNAME = "nnurrii"            
            

async def main():
    CHANNEL = str(input("Channel: "))  
    uri = "wss://irc-ws.chat.twitch.tv:443"
    async with websockets.connect(uri) as ws:
        await ws.send("CAP REQ :twitch.tv/tags twitch.tv/commands twitch.tv/membership\r\n")
        await ws.send(f"PASS oauth:{OAUTH_TOKEN}\r\n")
        await ws.send(f"NICK {USERNAME}\r\n")
        await ws.send(f"JOIN #{CHANNEL}\r\n")
        print("Connected. Listening...\n")

        while True:
            message = await ws.recv()

            # A single recv can contain multiple IRC lines
            for line in message.split("\r\n"):
                if not line:
                    continue

                print(line)

                # Respond to PING to stay connected
                if line.startswith("PING"):
                    await ws.send(line.replace("PING", "PONG") + "\r\n")

asyncio.run(main())




    

