""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.marine$")
async def usit(e):
    await e.edit(
        f"**Hallo Sensei {DEFAULTUSER} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Pirates](t.me/coklintoud)"
        "\n[One Piece](https://github.com/aldoaprilyan3/One-Piece)"
        "\n[Instagram](Instagram.com/aldoaprilyan3)")


@register(outgoing=True, pattern="^.yonkou$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/aldoaprilyan3/One-Piece/Lord-Userbot/varshelper.txt)")


CMD_HELP.update({
    ".marine":
    "`.marine`\
\nUsage: Bantuan Untuk One Piece.\
\n`.yonkou`\
\nUsage: Melihat Daftar Vars."
})
