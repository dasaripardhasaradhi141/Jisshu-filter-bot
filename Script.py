import os
class script(object):
    START_TXT = """<b>Hᴇʟʟᴏ {}, ᴍʏ ɴᴀᴍᴇ <a href=https://t.me/{}>{}</a>
    
ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇꜱ ᴀɴᴅ ꜱᴇʀɪᴇꜱ 😁, ᴊᴜꜱᴛ ᴛʏᴘᴇ ᴍᴏᴠɪᴇ/ꜱᴇʀɪᴇꜱ ɴᴀᴍᴇ</b>"""
    
    HELP_TXT = """<b>ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ᴅᴏᴄᴜᴍᴇɴᴛᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ꜱᴘᴇᴄɪꜰɪᴄ ᴍᴏᴅᴜʟᴇꜱ..</b>"""
    
    TELE_TXT = """<b>/telegraph - sᴇɴᴅ ᴍᴇ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ (5ᴍʙ)

ɴᴏᴛᴇ - ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋ ɪɴ ʙᴏᴛʜ ɢʀᴏᴜᴘs ᴀɴᴅ ʙᴏᴛ ᴘᴍ</b>"""
    FSUB_TXT = """<b>• ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ 😗
• ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ᴛᴀʀɢᴇᴛ ғᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ᴄʜᴀɴɴᴇʟ ᴏʀ Gʀᴏᴜᴘ  😉
• sᴇɴᴅ /fsub ʏᴏᴜʀ_ᴛᴀʀɢᴇᴛ_ᴄʜᴀᴛ_ɪᴅ
ᴇx: <code>/fsub -100xxxxxx</code>

ɴᴏᴡ ɪᴛ's ᴅᴏɴᴇ.ɪ ᴡɪʟʟ ᴄᴏᴍᴘᴇʟ ʏᴏᴜʀ ᴜsᴇʀs ᴛᴏ ᴊᴏɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ, ᴀɴᴅ I ᴡɪʟʟ ɴᴏᴛ ᴘʀᴏᴠɪᴅᴇ ᴀɴʏ ғɪʟᴇs ᴜɴᴛɪʟ ʏᴏᴜʀ ᴜsᴇʀs ᴊᴏɪɴ ʏᴏᴜʀ ᴛᴀʀɢᴇᴛ ᴄʜᴀɴɴᴇʟ.

ᴛᴏ ᴅɪsᴀʙʟᴇ ғsᴜʙ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ, sɪᴍᴘʟʏ sᴇɴᴅ <code>/del_fsub</code>

ᴛᴏ ᴄʜᴇᴄᴋ ɪғ ғsᴜʙ ɪs ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴏʀ ɴᴏᴛ, ᴜsᴇ <code>/show_fsub</code></b>"""

    FORCESUB_TEXT="""<b>
ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ʀᴇᴏ̨ᴜᴇsᴛᴇᴅ ʙʏ ʏᴏᴜ.

ʏᴏᴜ ᴡɪʟʟ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ᴏғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ.

ғɪʀsᴛ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ "Jᴏɪɴ ᴜᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ" ʙᴜᴛᴛᴏɴ, ᴛʜᴇɴ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ "ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ Jᴏɪɴ" ʙᴜᴛᴛᴏɴ.

ᴀғᴛᴇʀ ᴛʜᴀᴛ, ᴛʀʏ ᴀᴄᴄᴇssɪɴɢ ᴛʜᴀᴛ ᴍᴏᴠɪᴇ ᴛʜᴇɴ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ "ᴛʀʏ ᴀɢᴀɪɴ" ʙᴜᴛᴛᴏɴ.
    </b>"""
    
    TTS_TXT="""
<b>• sᴇɴᴅ /tts ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ</b>"""

    DISCLAIMER_TXT = """
<b>ᴛʜɪꜱ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢ ꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪʙʙᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ꜱʜᴀʀᴇ ᴏʀ ᴄᴏɴꜱᴜᴍᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ. 

🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/DPS_Files'>ᴅᴘꜱ</a></b>"""
    

    ABOUT_TEXT = """<b>⍟───[ MY ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
‣ ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/{}>{}</a>
‣ ᴍʏ ʙᴇsᴛ ғʀɪᴇɴᴅ : <a href='tg://settings'>ᴛʜɪs ᴘᴇʀsᴏɴ</a> 
‣ ᴅᴇᴠ : <a href='https://t.me/DPS_Movies'>ᴅᴘꜱ ᴍᴏᴠɪᴇꜱ</a> 
‣ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a> 
‣ ʟᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/download/releases/3.0/'>ᴘʏᴛʜᴏɴ 3</a> 
‣ ᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a> 
‣ ʙᴏᴛ sᴇʀᴠᴇʀ : <a href='https://heroku.com'>ʜᴇʀᴏᴋᴜ</a> 
‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ2.7.1 [sᴛᴀʙʟᴇ]></b>"""    
    
    SUPPORT_GRP_MOVIE_TEXT = '''<b>ʜᴇʏ {}

ɪ ғᴏᴜɴᴅ {} ʀᴇsᴜʟᴛs 🎁,
ʙᴜᴛ ɪ ᴄᴀɴ'ᴛ sᴇɴᴅ ʜᴇʀᴇ 🤞🏻
ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ ᴛᴏ ɢᴇᴛ ✨</b>'''

    CHANNELS = """
<u>ᴏᴜʀ ᴀʟʟ ɢʀᴏᴜᴘꜱ ᴀɴᴅ ᴄʜᴀɴɴᴇʟꜱ</u> 

▫ ᴀʟʟ ʟᴀᴛᴇꜱᴛ ᴀɴᴅ ᴏʟᴅ ᴍᴏᴠɪᴇꜱ & ꜱᴇʀɪᴇꜱ.
▫ ᴀʟʟ ʟᴀɴɢᴜᴀɢᴇꜱ ᴍᴏᴠɪᴇꜱ ᴀᴠᴀɪʟᴀʙʟᴇ.
▫ ᴀʟᴡᴀʏꜱ ᴀᴅᴍɪɴ ꜱᴜᴘᴘᴏʀᴛ.
▫ 𝟸𝟺x𝟽 ꜱᴇʀᴠɪᴄᴇꜱ ᴀᴠᴀɪʟᴀʙʟᴇ."""

    LOGO = """

BOT WORKING PROPERLY 🔥"""
    
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v4.2 [ Sᴛᴀʙʟᴇ ]</code>
</b>"""
        
    
    STATUS_TXT = """<b><u>🗃 ᴅᴀᴛᴀʙᴀsᴇ 1 🗃</u>

» ᴛᴏᴛᴀʟ ᴜsᴇʀs - <code>{}</code>
» ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs - <code>{}</code>
» ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🗳 ᴅᴀᴛᴀʙᴀsᴇ 2 🗳</u></b>

» ᴛᴏᴛᴀʟ ꜰɪʟᴇs - <code>{}</code>
» ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🤖 ʙᴏᴛ ᴅᴇᴛᴀɪʟs 🤖</u>

» ᴜᴘᴛɪᴍᴇ - <code>{}</code>
» ʀᴀᴍ - <code>{}%</code>
» ᴄᴘᴜ - <code>{}%</code></b>"""

    NEW_USER_TXT = """<b>#New_User {}

≈ ɪᴅ:- <code>{}</code>
≈ ɴᴀᴍᴇ:- {}</b>"""

    NEW_GROUP_TXT = """#New_Group {}

Group name - {}
Id - <code>{}</code>
Group username - @{}
Group link - {}
Total members - <code>{}</code>
User - {}"""

    REQUEST_TXT = """<b>📜 ᴜꜱᴇʀ - {}
📇 ɪᴅ - <code>{}</code>

🎁 ʀᴇǫᴜᴇꜱᴛ ᴍꜱɢ - <code>{}</code></b>"""  
   
    IMDB_TEMPLATE_TXT = """
<b>ʜᴇʏ {message.from_user.mention}, ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʀᴇꜱᴜʟᴛꜱ ꜰᴏʀ ʏᴏᴜʀ ǫᴜᴇʀʏ {search}.

IMDb Data:

<b>🏷 Title</b>: <a href={url}>{title}</a>
┣⪼🎭 Genres: {genres}
┣⪼📆 Year: <a href={url}/releaseinfo>{year}</a>
┣⪼🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 (based on {votes} user ratings.)
┣⪼📀 RunTime: {runtime} Minutes


⏰Result Shown in: {remaining_seconds} <i>seconds</i> 🔥
</b>
"""

    FILE_CAPTION = """<b>{file_name}\n\n𝖩𝗈𝗂𝗇➥ 「<a href="https://t.me/DPS_Movies">ᴅᴘꜱ ᴍᴏᴠɪᴇꜱ</a>」</b>"""
    

    ALRT_TXT = """ !"""

    OLD_ALRT_TXT = """ʏᴏᴜ ᴀʀᴇ ᴜsɪɴɢ ᴍʏ ᴏʟᴅ ᴍᴇssᴀɢᴇs..sᴇɴᴅ ᴀ ɴᴇᴡ ʀᴇǫᴜᴇsᴛ.."""

    NO_RESULT_TXT = """<b>ᴛʜɪs ᴍᴇssᴀɢᴇ ɪs ɴᴏᴛ ʀᴇʟᴇᴀsᴇᴅ ᴏʀ ᴀᴅᴅᴇᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ 🙄</b>"""
    
    I_CUDNT = """🤧 𝗛𝗲𝗹𝗹𝗼 {}

𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 𝗮𝗻𝘆 𝗺𝗼𝘃𝗶𝗲 𝗼𝗿 𝘀𝗲𝗿𝗶𝗲𝘀 𝗶𝗻 𝘁𝗵𝗮𝘁 𝗻𝗮𝗺𝗲.. 😐"""

    I_CUD_NT = """😑 𝗛𝗲𝗹𝗹𝗼 {}

𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 𝗮𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝗿𝗲𝗹𝗮𝘁𝗲𝗱 𝘁𝗼 𝘁𝗵𝗮𝘁 😞... 𝗰𝗵𝗲𝗰𝗸 𝘆𝗼𝘂𝗿 𝘀𝗽𝗲𝗹𝗹𝗶𝗻𝗴."""
    
    CUDNT_FND = """🤧 𝗛𝗲𝗹𝗹𝗼 {}

𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 𝗮𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝗿𝗲𝗹𝗮𝘁𝗲𝗱 𝘁𝗼 𝘁𝗵𝗮𝘁 𝗱𝗶𝗱 𝘆𝗼𝘂 𝗺𝗲𝗮𝗻 𝗮𝗻𝘆 𝗼𝗻𝗲 𝗼𝗳 𝘁𝗵𝗲𝘀𝗲 ?? 👇"""
    
    FONT_TXT= """<b>ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴍᴏᴅᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ꜰᴏɴᴛs sᴛʏʟᴇ, ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ʟɪᴋᴇ ᴛʜɪs ꜰᴏʀᴍᴀᴛ

<code>/font hi how are you</code></b>"""
    
    PLAN_TEXT = """<b>⍟ ʙᴜʏ ᴘᴀɪᴅ ᴘʟᴀɴ ʙʏ - /plan ⍟

───[ ᴏʀ ]───

⍟ ɢᴇᴛ ᴘʀᴇᴍɪᴜᴍ ʙʏ ʀᴇꜰᴇʀʀɪɴɢ ⍟

ʀᴇғᴇʀʀᴇ ʏᴏᴜʀ ʟɪɴᴋ ᴛᴏ ʏᴏᴜʀ ғʀɪᴇɴᴅs, ғᴀᴍɪʟʏ, ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ɢʀᴏᴜᴘ ᴛᴏ ɢᴇᴛ ғʀᴇᴇ ᴘʀᴇᴍɪᴜᴍ ғᴏʀ {}

ʀᴇғᴇʀᴀʟ ʟɪɴᴋ - https://telegram.me/{}?start=VJ-{}

ɪғ {} ᴜɴɪǫᴜᴇ ᴜsᴇʀ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴡɪᴛʜ ʏᴏᴜʀ ʀᴇғᴇʀᴀʟ ʟɪɴᴋ ᴛʜᴇɴ ʏᴏᴜ ᴡɪʟʟ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴀᴅᴅᴇᴅ ɪɴ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ.

</b>"""
    
    VERIFICATION_TEXT = """<b>👋 ʜᴇʏ {} {},

📌 <u>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪғɪᴇᴅ ᴛᴏᴅᴀʏ, ᴘʟᴇᴀꜱᴇ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪғʏ & ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ғᴏʀ ᴛɪʟʟ ɴᴇxᴛ 𝟺 ʜᴏᴜʀs</u>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 1/3 ✓

ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ғɪʟᴇꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴꜱ ᴛʜᴇɴ ʙᴜʏ ʙᴏᴛ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ 😊

💶 sᴇɴᴅ /plan ᴛᴏ ʙᴜʏ sᴜʙsᴄʀɪᴘᴛɪᴏɴ</b>"""

    VERIFY_COMPLETE_TEXT = """<b>👋 ʜᴇʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 1st ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ғᴏʀ 𝟺 ʜᴏᴜʀs</b>"""

    SECOND_VERIFICATION_TEXT = """<b>👋 ʜᴇʏ {} {},

📌 <u>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ, ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ᴛɪʟʟ ɴᴇxᴛ 𝟺 ʜᴏᴜʀs</u>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 2/3

ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ғɪʟᴇꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴꜱ ᴛʜᴇɴ ʙᴜʏ ʙᴏᴛ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ 😊

💶 sᴇɴᴅ /plan ᴛᴏ ʙᴜʏ sᴜʙsᴄʀɪᴘᴛɪᴏɴ</b>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b>👋 ʜᴇʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 2nd ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ғᴏʀ 𝟺 ʜᴏᴜʀs</b>"""

    THIRDT_VERIFICATION_TEXT = """<b>👋 ʜᴇʏ {},
    
📌 <u>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ᴛᴏᴅᴀʏ, ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ & ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ꜰᴜʟʟ ᴅᴀʏ.</u>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 3/3

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</b>"""

    THIRDT_VERIFY_COMPLETE_TEXT= """<b>👋 ʜᴇʏ {},
    
ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 3rd ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ꜰᴜʟʟ ᴅᴀʏ </b>"""

    VERIFIED_LOG_TEXT = """<b><u>☄ ᴜsᴇʀ ᴠᴇʀɪꜰɪᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ ☄</u>

⚡️ ɴᴀᴍᴇ:- {} [ <code>{}</code> ] 
📆 ᴅᴀᴛᴇ:- <code>{} </code></b>

#verified_{}_completed"""


    MOVIES_UPDATE_TXT = """<b>#𝑵𝒆𝒘_𝑭𝒊𝒍𝒆_𝑨𝒅𝒅𝒆𝒅 ✅
**🍿 Title:** {title}
**🎃 Genres:** {genres}
**📆 Year:** {year}
**⭐ Rating:** {rating} / 10
</b>"""

    PREPLANS_TXT = """<b>👋 ʜᴇʏ {}
    
- ᴘʀᴇᴍɪᴜᴍ ꜱʟᴏᴛꜱ ᴡɪʟʟ ʙᴇ ᴏᴘᴇɴ ᴀᴛ ᴛʜᴇ ꜱᴛᴀʀᴛɪɴɢ ᴏꜰ ᴇᴠᴇʀʏ ᴍᴏɴᴛʜ - \n\n- ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ᴛᴏ ꜱᴛᴀʏ ᴜᴘᴅᴀᴛᴇᴅ - \n\n🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🎁\n\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ\n○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs\n○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ\n○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ\n○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs\n○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs\n○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ\n\nᴄʟɪᴄᴋ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /myplan\n
</b>"""    

    PREPLANSS_TXT = """<b>👋 ʜᴇʏ {}
    
- ᴘʀᴇᴍɪᴜᴍ ꜱʟᴏᴛꜱ ᴡɪʟʟ ʙᴇ ᴏᴘᴇɴ ᴀᴛ ᴛʜᴇ ꜱᴛᴀʀᴛɪɴɢ ᴏꜰ ᴇᴠᴇʀʏ ᴍᴏɴᴛʜ - \n\n- ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ᴛᴏ ꜱᴛᴀʏ ᴜᴘᴅᴀᴛᴇᴅ - \n\n🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🎁\n\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ\n○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs\n○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ\n○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ\n○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs\n○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs\n○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ\n\nᴄʟɪᴄᴋ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /myplan\n
</b>"""

    OTHER_TXT = """<b>👋 ʜᴇʏ {},
    
🎁 <u>ᴏᴛʜᴇʀ ᴘʟᴀɴ</u>
⏰ ᴄᴜꜱᴛᴏᴍɪꜱᴇᴅ ᴅᴀʏꜱ
💸 ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴅᴀʏꜱ ʏᴏᴜ ᴄʜᴏᴏꜱᴇ

🏆 ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴀ ɴᴇᴡ ᴘʟᴀɴ ᴀᴘᴀʀᴛ ꜰʀᴏᴍ ᴛʜᴇ ɢɪᴠᴇɴ ᴘʟᴀɴ, ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀʟᴋ ᴛᴏ ᴏᴜʀ <a href='https://t.me/DPS_Files'>ᴏᴡɴᴇʀ</a> ᴅɪʀᴇᴄᴛʟʏ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ ᴄᴏɴᴛᴀᴄᴛ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.
    
👨‍💻 ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴏᴡɴᴇʀ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴏᴛʜᴇʀ ᴘʟᴀɴ.

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    FREE_TXT = """<b>👋 ʜᴇʏ {}
    
- ᴘʀᴇᴍɪᴜᴍ ꜱʟᴏᴛꜱ ᴡɪʟʟ ʙᴇ ᴏᴘᴇɴ ᴀᴛ ᴛʜᴇ ꜱᴛᴀʀᴛɪɴɢ ᴏꜰ ᴇᴠᴇʀʏ ᴍᴏɴᴛʜ - \n\n- ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ᴛᴏ ꜱᴛᴀʏ ᴜᴘᴅᴀᴛᴇᴅ - \n\n🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs 🎁\n\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪғʏ\n○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ\n○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs\n○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ\n○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ\n○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs\n○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs\n○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ\n\nᴄʟɪᴄᴋ ᴛᴏ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ /myplan\n
</b>"""

    ADMIN_CMD_TXT = """<b>
-------------User Premium------------
➩ /add_premium {user ID} {Times} - Add a premium user
➩ /remove_premium {user ID} - Remove a premium user
➩ /add_redeem - Generate a redeem code
➩ /premium_users - List all premium users
➩ /refresh - Refresh free trial for users
-------------Update Channel----------
➩ /set_muc {channel ID} - Set the movies update channel
--------------PM Search--------------
➩ /pm_search_on - Enable PM search
➩ /pm_search_off - Disable PM search
--------------Verify ID--------------
➩ /verify_id - Generate a verification ID for group use only
--------------Set Ads----------------
➩ /set_ads {ads name}}#{Times}#{photo URL} - <a href="https://t.me/DPS_Files/11">Explain</a>
➩ /del_ads - Delete ads
-------------Top Trending------------
➩ /setlist {Mirzapur, Money Heist} - <a href=https://t.me/DPS_Files/10>Explain</a>
➩ /clearlist - Clear all lists
</b>"""

    ADMIN_CMD_TXT2 = """<b>
--------------Index File--------------
➩ /index - Index all files
--------------Leave Link--------------
➩ /leave {group ID} - Leave the specified group
-------------Send Message-------------
➩ /send {user-name} - Use this command as a reply to any message
----------------Ban User---------------
➩ /ban {user-name} - Ban user 
➩ /unban {user-name} - Unban user
--------------Broadcast--------------
➩ /broadcast - Broadcast a message to all users
➩ /grp_broadcast - Broadcast a message to all connected groups

</b>"""
    
    GROUP_TEXT = """<b>
 --------------Set Verify-------------
/set_verify {{website link}} {{website api}}
/set_verify_2 {{website link}} {{website api}}
/set_verify_3 {{website link}} {{website api}}
-------------Set Verify Time-----------
/set_time_2 {{seconds}} Sᴇᴛ ᴛʜᴇ sᴇᴄᴏɴᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴛɪᴍᴇ
/set_time_3 {{seconds}} Sᴇᴛ ᴛʜᴇ ᴛʜɪʀᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴛɪᴍᴇ
--------------Verify On Off------------
/verifyoff {{verify.off code}} - off verification <a href="https://t.me/DPS_Files">Cᴏɴᴛᴀᴄᴛ</a> ᴛʜᴇ ʙᴏᴛ ᴀᴅᴍɪɴ ғᴏʀ ᴀ ᴠᴇʀɪғʏ.ᴏғғ ᴄᴏᴅᴇ
/verifyon - on verification 
------------Set File Caption-----------
/set_caption - set coustom file caption 
-----------Set Imdb Template-----------
/set_template - set IMDb template <a href="https://t.me/DPS_Files/8">Example</a>
--------------Set Tutorial-------------
/set_tutorial - set 1 verification tutorial 
-------------Set Log Channel-----------
--> ᴀᴅᴅ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ʙʏ ᴛʜɪs ꜰᴏʀᴍᴀᴛ & ᴍᴀᴋᴇ sᴜʀᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ 👇

/set_log {{log channel id}}
---------------------------------------
ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀʟʟ ᴅᴇᴛᴀɪʟs 
ʙʏ /details ᴄᴏᴍᴍᴀɴᴅ
Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴀɴᴅ ᴜsᴇ ᴀʟʟ ғᴇᴀᴛᴜʀᴇs😇</b>"""

    SOURCE_TXT = """<b>
NOTE:
- ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʜᴇʀᴇ ◉› :<a href="https://t.me/DPS_Files">ᴅᴘs ᴍᴏᴠɪᴇs</a>

developer : ᴅᴘs ᴍᴏᴠɪᴇs
</b>""" 
    GROUP_C_TEXT = """<b>
 --------------Set Verify-------------
/set_verify {website link} {website api}
/set_verify_2 {website link} {website api}
/set_verify_3 {website link} {website api}
-------------Set Verify Time-----------
/set_time_2 {seconds} Sᴇᴛ ᴛʜᴇ sᴇᴄᴏɴᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴛɪᴍᴇ
/set_time_3 {seconds} Sᴇᴛ ᴛʜᴇ ᴛʜɪʀᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴛɪᴍᴇ
--------------Verify On Off------------
/verifyoff {verify.off code} - off verification <a href="https://t.me/DPS_Files">Cᴏɴᴛᴀᴄᴛ</a> ᴛʜᴇ ʙᴏᴛ ᴀᴅᴍɪɴ ғᴏʀ ᴀ ᴠᴇʀɪғʏ.ᴏғғ ᴄᴏᴅᴇ
/verifyon - on verification 
------------Set File Caption-----------
/set_caption - set coustom file caption 
-----------Set Imdb Template-----------
/set_template - set IMDb template <a href="https://t.me/DPS_Files/8">Example</a>
--------------Set Tutorial-------------
/set_tutorial {tutorial link} - set 1 verification tutorial 
/set_tutorial_2 {tutorial link} - set 2 verification tutorial 
/set_tutorial_3 {tutorial link} - set 3 verification tutorial 
-------------Set Log Channel-----------
--> ᴀᴅᴅ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ʙʏ ᴛʜɪs ꜰᴏʀᴍᴀᴛ & ᴍᴀᴋᴇ sᴜʀᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ 👇

/set_log {log channel id}
---------------------------------------
ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀʟʟ ᴅᴇᴛᴀɪʟs 
ʙʏ /details ᴄᴏᴍᴍᴀɴᴅ
Iғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ᴅᴏᴜʙᴛs ᴘʟᴇᴀsᴇ <a href="https://t.me/DPS_Files">ᴄᴏɴᴛᴀᴄᴛ</a> ᴍʏ <a href="https://t.me/DPS_Files">ᴀᴅᴍɪɴ</a></b>"""
