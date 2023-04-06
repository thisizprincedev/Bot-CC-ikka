import requests
import random
from random import randint
import string
import json
from mills.plugins._helpers.tools import find_between

def socks4(r):
	prox = r.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	return prox


def socks5(r):
	prox = r.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	return prox


def http(r):
	prox = r.get(f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=100000&country=all&ssl=all&anonymity=all").text
	return prox


def https(r):
	prox = r.get(f"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=100000&country=all&ssl=all&anonymity=all").text
	return prox
