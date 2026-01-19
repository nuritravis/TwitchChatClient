import websockets
import asyncio
from dotenv import load_dotenv
import os
import irc_parser

load_dotenv()
OAUTH_TOKEN = os.getenv("OAUTH_TOKEN")     
USERNAME = os.getenv("USERNAME")           
CHANNEL = str(input("Channel: "))      

def msg_constructor(msg: str):
    irc_msg = f'PRIVMSG #{CHANNEL} :{msg} \r\n'
    return irc_msg

async def main():

    uri = "wss://irc-ws.chat.twitch.tv:443"
    async with websockets.connect(uri) as ws:
        await ws.send("CAP REQ :twitch.tv/tags twitch.tv/commands twitch.tv/membership\r\n")
        await ws.send(f"PASS oauth:{OAUTH_TOKEN}\r\n")
        await ws.send(f"NICK {USERNAME}\r\n")
        await ws.send(f"JOIN #{CHANNEL}\r\n")
        print("Connected. Listening...\n")

        while True:
            message = await ws.recv()

            # a single recv can contain multiple IRC lines
            for line in message.split("\r\n"):
                if not line:
                    continue
                
                parsed_msg = irc_parser.parse_line(line)
                
                if parsed_msg is not None and parsed_msg[1][1] == "PRIVMSG":
                    user = irc_parser.get_user(parsed_msg)
                    print(f"{user}: {parsed_msg[2]}")


                # respond to PING to stay connected
                if line.startswith("PING"):
                    await ws.send(line.replace("PING", "PONG") + "\r\n")

asyncio.run(main())




    

