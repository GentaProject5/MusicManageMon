# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, ICON_HELP
from userbot.utils import edit_delete, edit_or_reply, ayiin_cmd
from time import sleep

modules = CMD_HELP


@ayiin_cmd(pattern="help(?: |$)(.*)")
async def help(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, str(CMD_HELP[args]))
        else:
            await edit_delete(event, f"**Module `{args}` Gak Ada Tod**, **Ketik Yang Bener Anj.**")
    else:
        user = await event.client.get_me()
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += f"`\t\t\t{ICON_HELP}\t\t\t"
        await event.edit("πΏ")
        sleep(3)
        await edit_or_reply(
            event,
            f"**[β§ π°ππΈπΈπ½-πππ΄ππ±πΎπ β§](https://github.com/AyiinXd/Ayiin-Userbot)**\n"
            f"**ί· πΉππΌπ»π°π·** `{len(modules)}` **Modules**\n"
            f"**βοΈ πΎππ½π΄π:** [{user.first_name}](tg://user?id={user.id})\n\n"
            f"{ICON_HELP}   {string}"
            f"\n\nβ  **πππΏπΏπΎππ** : @AyiinXdSupport\nβ  **π½πΎππ΄π** :  `{cmd}help yinsubot` **Untuk Melihat Module Lainnya**"
        )
