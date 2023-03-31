"""
≛ <b>Commands Available</b> ≛

──────────────────────
<code>/bin</code> bin || <reply_to_msg> - Information about the Bin.
──────────────────────

© <a href="https://t.me/TakashiKovace">TakeshiKovace</a>
"""


import os
import re
import time
import requests

from mills.decorators import bot_cmd
from mills.plugins.checkers.utils.userinfo import get_user_info
from mills.plugins.checkers.utils.bininfo import get_bin_info, get_bin_info_all



@bot_cmd(cmd="bin", text_only = True)
async def _(m):
    text = m.pattern_match.group(1).strip()
    if len(text) < 6:
        await m.sod("Invalid bin.")
        return
    bin_info = get_bin_info(text[:6])
    if not bin_info:
        url="https://lookup.binlist.net/"+bin
        r = requests.get(url).json()

        try:
            scheme = r["scheme"]
        except:
            scheme = 'None'
        try:
            type = r['type']
        except:
            type='None'
        try:
            brand = r['brand']
        except:
            brand ='brand'    
        try:
            country = r["country"]["name"]
            emoji = r["country"]['emoji']
            alpha2 = r["country"]['alpha2']
        except:
            country='None'
            emoji='None'
            alpha2="None"
        try:
            bank = r['bank']['name']
        except:
            bank = 'None'
        try:
            url = r['bank']['url']
        except:
            url = 'None'
        try:
            phone = r['bank']['phone']
        except:
            phone = 'None'


        mess = f"""
        <b>Bin</b>: <code>{text[:6]}</code>
        <b>Vendor</b>: <b>{scheme}</b>
        <b>Type</b>: <b>{type}</b>
        <b>Level</b>: <b>{brand}</b>
        <b>Bank name</b>: <b>{bank}</b>
        <b>Iso</b>: <b>{alpha2} {emoji}</b>
        <b>Country</b>: <b>{country}</b>
        <b>Phone</b>: <b>{phone}</b>
        """
        await m.sod(mess)
        return
    mess = f"""
<b>Bin</b>: <code>{text[:6]}</code>
<b>Vendor</b>: <b>{bin_info['vendor']}</b>
<b>Type</b>: <b>{bin_info['type']}</b>
<b>Level</b>: <b>{bin_info['level']}</b>
<b>Prepaid</b>: <b>{bin_info['prepaid']}</b>
<b>Bank name</b>: <b>{bin_info['bank_name']}</b>
<b>Iso</b>: <b>{bin_info['iso']} {bin_info['flag']}</b>
<b>Country</b>: <b>{bin_info['country']}</b>
"""
    await m.sod(mess)