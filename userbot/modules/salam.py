from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^kntl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**LU KONTOL**")
    sleep(3)
    await typew.edit("`NGOMONG JOROK DOSA GA SI!!!`")
    sleep(3)
    await typew.edit("`DAHLAH DASAR KEPALA KONTOL!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^G(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**MAKAN REBUNG PAKE BALOK**")
    sleep(3)
    await typew.edit("`NIMBRUNG GOBLOKK!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("`NIMBRUNG GOBLOKK!!!`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**HAI ANZEEENGGGG SAYA {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`KONTOLLL.....`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hai Anzeeeenggg SAYA {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`KONTOLLL.....`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Astaghfirulloh anda berdosa sekali...`")
    sleep(1)
    await typew.edit("`Waallaikumsalam Sayang......`")
# Owner @Si_Dian


@register(outgoing=True, pattern='^l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Astaghfirulloh anda berdosal sekali...`")
    sleep(1)
    await typew.edit("`Waallaikumsalam Sayang.....`")
# Owner @Si_Dian


CMD_HELP.update({
    "salam":
    "`P`\
\nUsage: Untuk Memberi Hujatan.\
\n\n`L`\
\nUsage: Untuk Menjawab Salam."
})
