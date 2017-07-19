import discord
from discord import Embed

import level_system


description = "Show your Level or server scoreboard"


async def ex(message, client):
    if len(list(message.mentions)) > 0:
        member = message.mentions[0]
        xp = level_system.get_xp(member)
        level = int(int(xp) / 1000)
        progress = (int(xp) % 1000) / 1000
        progress_bar = "[" + "===================="[:int(progress * 20)] + "                    "[int(progress * 20):] + "]\n\n   " + str(int(progress * 100)) + "% to next LVL"
        await client.send_message(message.channel, embed=Embed(color=discord.Color.gold(),
                                                               title=member.name + "'s Level",
                                                               description=("**[LVL %s]**  `%s XP`\n```\n%s\n```" % (level, xp, progress_bar))))

    else:
        gettedtable = level_system.get_table()
        temptable = dict([(k, gettedtable[k]) for k in sorted(gettedtable, key=gettedtable.get, reverse=True)])
        if len(temptable.keys) >= 20:
            table = temptable
        else:
            for k, v in temptable:
                table[k] = v
        out = ""
        for memb_id in table:
            try:
                out += "**%s:**  **`%s XP`** \n" % (discord.utils.get(message.server.members, id=memb_id).name, table[memb_id])
            except:
                pass
        await client.send_message(message.channel, "**XP LIST**\n\n" + out[:1980])
