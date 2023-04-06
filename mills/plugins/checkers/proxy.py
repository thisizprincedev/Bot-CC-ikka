"""
≛ <b>Commands Available</b> ≛

──────────────────────
- <code>/chk</code> cc cvv mes ano || <reply_to_msg>.
➛ Stripe Charge $5.
──────────────────────

© <a href="https://t.me/TakashiKovace">TakeshiKovace</a>
"""


import json
import os
import re
import time
import requests
from mills import LOG_CHAT

from mills.decorators import bot_cmd
from mills.plugins.checkers.utils.gateinfo import get_gate_info
from mills.plugins import rand_user_base
from mills.plugins.checkers.utils.getcards  import get_cards
from mills.plugins._helpers.strings import get_strings
from mills.plugins.checkers.funcs.proxy_defs import socks4, socks5, http, https

@bot_cmd(cmd="proxy", text_only = True)
async def _(m):
    text = m.pattern_match.group(1)
    browser = requests.Session()
    
    if proxy := await m.adb.get_key('use_proxy'):
        browser.proxies = {'http': proxy, 'https': proxy}
        
    if 'socks4' in text:
        se = socks4(browser)
        open("proxy/socks4.txt", "w").write(se)
        if os.path.exists("proxy/socks4.txt"):
            await m.sod(file='proxy/socks4.txt')
        else:
            await m.sod("not found.")
    
    if 'socks5' in text:
        se = socks5(browser)
        open("proxy/socks5.txt", "w").write(se)
        if os.path.exists("proxy/socks5.txt"):
            await m.sod(file='proxy/socks5.txt')
        else:
            await m.sod("not found.")
        
    if 'https' in text:
        se = https(browser)
        open("proxy/Https.txt", "w").write(se)
        if os.path.exists("proxy/https.txt"):
            await m.sod(file='proxy/https.txt')
        else:
            await m.sod("not found.")
        
    if 'http' in text:
        se = http(browser)
        open("proxy/Http.txt", "w").write(se)
        if os.path.exists("proxy/Http.txt"):
            await m.sod(file='proxy/Http.txt')
        else:
            await m.sod("not found.")
    

    return