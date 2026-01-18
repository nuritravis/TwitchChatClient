
def parse_msg(msg: str) -> str:
    if "PRIVMSG" in msg:
        d = dict(
            (k.strip(), v.strip())
            for k, v in (item.split("=", 1) for item in msg.split(";"))
        )
        return d
if __name__ == "__main__":
    dummy1 = "@badge-info=;badges=la-velada-v-badge/1;client-nonce=0bcbe47c7ef74e9cb645ed37b3d66508;color=#FF69B4;display-name=Exveeeee;emotes=;first-msg=0;flags=;id=bc4d241c-fdac-4ba4-bacb-1c21df2af2e3;mod=0;returning-chatter=0;room-id=1093257262;subscriber=0;tmi-sent-ts=1768757038846;turbo=0;user-id=141382154;user-type= :exveeeee!exveeeee@exveeeee.tmi.twitch.tv PRIVMSG #itskatchii :arky my favorite bruhhhh"
    dummy2 = "@badge-info=subscriber/8;badges=vip/1,subscriber/6,share-the-love/1;client-nonce=eef0ea92c7ea40e8bcfb1e8e982f314e;color=#8A2BE2;display-name=CONVlCKT;emotes=;first-msg=0;flags=;id=b3de9f2a-ab51-4ac0-b44e-fd3e685fdd80;mod=0;returning-chatter=0;room-id=1093257262;subscriber=1;tmi-sent-ts=1768758126580;turbo=0;user-id=198395503;user-type=;vip=1 :convlckt!convlckt@convlckt.tmi.twitch.tv PRIVMSG #itskatchii :it would run out of content after a week"
    print("\n")
    print(parse_msg(dummy1))
    print("\n")
    print("\n")

    print(parse_msg(dummy2))
    print("\n")