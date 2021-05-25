import requests
import json
import random
import re

def getmail():
	s = requests.session()
	headers = {
	'Connection': 'keep-alive',
	'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'X-Requested-With': 'XMLHttpRequest',
	'sec-ch-ua-mobile': '?0',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Dest': 'empty',
	'Referer': 'https://www.fakemail.net/',
	'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
	}
	response = s.get('https://www.fakemail.net/index/index', headers=headers)
	mail = response.text.rsplit('{"email":"')[1].rsplit('"')[0]
	return mail


def get_code(id_dv):
	s = requests.session()
	headers = {
		'Connection': 'keep-alive',
		'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'X-Requested-With': 'XMLHttpRequest',
		'sec-ch-ua-mobile': '?0',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
		'Sec-Fetch-Site': 'same-origin',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Dest': 'empty',
		'Referer': 'https://www.fakemail.net/',
		'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		}
	cookie = {'TMA':str(id_dv).replace('@','%40')}
	out = s.get('https://www.fakemail.net/index/refresh',headers=headers,cookies=cookie)
	sms = str(out.text.rsplit('"predmet":"')[1].rsplit('"')[0])
	if sms == 'Welcome to FakeMail:)':
    		code = None
	else:
    		code = sms
	try:
		otp = re.findall('[0-9]+', sms)[0]
	except:
		otp = ''

	dataout = {'Mail':id_dv,'message':code,'OTP':otp}
	return dataout

def get_mail_hdh():
    charsMail ="abcdefghijklmnopqrstuvwxyz"
    numbers = "01234567789"
    email = ''
    number = ''
    for i in range(10):
        email += random.choice(charsMail)
        number +=random.choice(numbers)

    headers = {
        'authority': 'api.mail.tm',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'origin': 'https://mail.tm',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://mail.tm/',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    }
    s = requests.session()
    mien = json.loads(str(s.get('https://api.mail.tm/domains').text))['hydra:member'][0]['domain']
    mail = email+number+'@'+mien
    data = '{"address":"'+mail+'","password":"rhgfdgfd"}'
    mails = json.loads(str(s.post('https://api.mail.tm/accounts', headers=headers, data=data).text))
    response = json.loads(str(s.post('https://api.mail.tm/token', headers=headers, data=data).text))
    return {'Mail':mails['address'],'token':response['token'],'Bản Quyền':'Hà Đứu Hậu'}

def get_code_hdh(authorization):
    headers = {
        'authority': 'api.mail.tm',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'accept': 'application/json, text/plain, */*',
        'authorization': 'Bearer '+authorization,
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'origin': 'https://mail.tm',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://mail.tm/',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5'
    }
    response = json.loads(str(requests.get('https://api.mail.tm/messages', headers=headers).text))
    try:
        code = {'Message':response['hydra:member'][0]['subject'],'OTP':re.findall('[0-9]+', str(response['hydra:member'][0]['subject']))[0],'Bản Quyền':'Hà Đứu Hậu'}
        return code
    except:
        code = {'Message':None,'OTP':None,'Bản Quyền':'Hà Đứu Hậu'}
        return code
