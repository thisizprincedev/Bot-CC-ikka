import requests
from mills.plugins import BINS_DICT


def get_bin_info(bin_to_find: int):
    if str(bin_to_find[:6]) in BINS_DICT:
        xx = BINS_DICT[str(bin_to_find[:6])]
        return xx
    else:
        url="https://lookup.binlist.net/"+bin_to_find
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

            
        return {
            "country": country,
            "iso": alpha2,
            "flag": emoji,
            "vendor": scheme,
            "type": type,
            "level": brand,
            "bank_name": bank,
            "prepaid": True if type == "PREPAID" else False
        } 

def get_bin_info_all(bin_to_find):
    
    if bin_to_find in BINS_DICT:
        xx = BINS_DICT[bin_to_find]
        return xx
    else:
        return False