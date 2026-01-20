import websockets
import asyncio
from dotenv import load_dotenv
import os
import irc_parser

load_dotenv()
OAUTH_TOKEN = os.getenv("OAUTH_TOKEN")     
USERNAME = os.getenv("USERNAME")           
CHANNEL = str(input("Channel: "))  
URI = "wss://irc-ws.chat.twitch.tv:443"    

def construct_msg(msg: str) -> str:
    irc_msg = f'PRIVMSG #{CHANNEL} :{msg}\r\n'
    return irc_msg

async def receive_msg(ws: object):
    while True:
        message = await ws.recv()

        # a single recv can contain multiple IRC lines
        for line in message.split("\r\n"):
            if not line:
                continue

            # respond to PING to stay connected
            if line.startswith("PING"):
                await ws.send(line.replace("PING", "PONG") + "\r\n")

            # parse and display incoming PRIVMSGs
            parsed_msg = irc_parser.parse_line(line)
            if parsed_msg is not None and parsed_msg[1][1] == "PRIVMSG":
                user = irc_parser.get_user(parsed_msg)
                print(f"{user}: {parsed_msg[2]}")

async def send_msg(ws: object):
    while True:
        user_input = await asyncio.to_thread(input)
        chat_msg = construct_msg(user_input)
        await ws.send(chat_msg)

async def main():

    async with websockets.connect(URI) as ws:
        await ws.send("CAP REQ :twitch.tv/tags twitch.tv/commands twitch.tv/membership\r\n")
        await ws.send(f"PASS oauth:{OAUTH_TOKEN}\r\n")
        await ws.send(f"NICK {USERNAME}\r\n")
        await ws.send(f"JOIN #{CHANNEL}\r\n")
        print("Connected. Listening...\n")

        recv_task = asyncio.create_task(receive_msg(ws))
        send_task = asyncio.create_task(send_msg(ws))
        await asyncio.gather(send_task, recv_task)
        
        
asyncio.run(main())




    

