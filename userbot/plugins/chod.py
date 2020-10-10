"""
Available Commands: .chod

by @xcruzhd2
inspired from @xtratgbot """

from telethon import events

import asyncio




@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 12)

    input_str = event.pattern_match.group(1)

    if input_str == "chod":

        await event.edit(input_str)

        animation_chars = [
        
            "`Ruk jaa , Abhi teri maa chodta hu `",
            "`Your mom (Randi) founded`",
            "`Your Mom Is Going To Fuck`",
            "`Fucking Your Mom😈😈\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done. 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Fucking Your Mom😈😈\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done..\n\nFucked Percentage... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Fucking Your Mom😈😈\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done...\n\nFucked Percentage... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Fucking Your Mom😈😈\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done....\n\nFucked Percentage... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Fucking Your Mom😈😈\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done.....\n\nFucked Percentage... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Fucking Your Mom😈😈\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done......\n\nFucked Percentage... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Fucking Your Mom😈😈\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done.......\n\nFucked Percentage... 84%\n█████████████████████▒▒▒▒ `",
            "`Fucking Your Mom😈😈\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nAlmost Done........\n\nFucked Percentage... 100%\n█████████████████████████ `",
            "`Fucking Your Mom😈😈\n\n\nYour Mom's Pussy Get Red\nCumming On Pussy\n\nYour mom get Pregnant\n\nResult: Now You Have 1 More Younger Brother 👍👍`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])
