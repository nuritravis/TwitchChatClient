
dummy1 = "@badge-info=;badges=la-velada-v-badge/1;client-nonce=0bcbe47c7ef74e9cb645ed37b3d66508;color=#FF69B4;display-name=Exveeeee;emotes=;first-msg=0;flags=;id=bc4d241c-fdac-4ba4-bacb-1c21df2af2e3;mod=0;returning-chatter=0;room-id=1093257262;subscriber=0;tmi-sent-ts=1768757038846;turbo=0;user-id=141382154;user-type= :exveeeee!exveeeee@exveeeee.tmi.twitch.tv PRIVMSG #itskatchii :arky my favorite bruhhhh"
dummy2 = "@badge-info=subscriber/8;badges=vip/1,subscriber/6,share-the-love/1;client-nonce=eef0ea92c7ea40e8bcfb1e8e982f314e;color=#8A2BE2;display-name=CONVlCKT;emotes=;first-msg=0;flags=;id=b3de9f2a-ab51-4ac0-b44e-fd3e685fdd80;mod=0;returning-chatter=0;room-id=1093257262;subscriber=1;tmi-sent-ts=1768758126580;turbo=0;user-id=198395503;user-type=;vip=1 :convlckt!convlckt@convlckt.tmi.twitch.tv PRIVMSG #itskatchii :it would run out of content after a week"

def parse_line(msg: str) -> tuple:
    if not msg or msg[0] != "@":
        return None

    # split tags from the rest at the FIRST space
    # remove the leading '@' so tags parse cleanly
    tags_part, rest = msg[1:].split(" ", 1)

    # parse tags (semicolon-delimited; key/value split on first '=')
    line_tags = dict(item.split("=", 1) for item in tags_part.split(";"))

    # split the trailing message body from the head at the FIRST " :"
    if " :" in rest:
        head, line_body = rest.split(" :", 1)
    else:
        head, line_body = rest, ""

    # split the head into tokens 
    line_data = head.split()

    return line_tags, line_data, line_body

def get_user(msg: tuple)->str:
    username = msg[1][0]
    username = username[username.index(":")+1:username.index("!")]
    return username

if __name__ == "__main__":

    print("\n")
    print(parse_line(dummy1))
    print("\n")
    print(parse_line(dummy2)[1][0])
    print(get_user(parse_line(dummy2)))
    print("\n")
    print(parse_line(dummy2))
    print("\n")