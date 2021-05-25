import requests

def Zalo_run(Phone):
    s = requests.session()
    s.headers.update({
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
        })
    param = {
        'a': 'pw'
    }

    data = {
        'phone_num': Phone,
        'iso_country_code': 'VN',
        'continue': 'https://chat.zalo.me',
    }
    datas = s.post('https://id.zalo.me/account/authen?',params = param, data = data,).json()

    if datas['error_code'] == -22:
        return {'phone':Phone,'status':True,'message':'Live'}
    elif datas['error_code'] == -31:
        return {'phone':Phone,'status':False,'message':'Disable/Does not exist'}
    else:
        return {'phone':Phone,'status':None,'message':'An unknown error'}

def zalo_key(token):
    token_list = ['5748t43fghudghdfgh433ghfudghufgh',
                    'gjnjfnbvcjb9wetig49gjdfgiu2i39g',
                    'fjgbdfkbjdkfjb9we348r9423fi923i',
                    'kvbdfmjkbmfkbmdfkbmdfkbmdfbkmdb',
                    'fgkbioke94itg3e049ig94gi49gi94g']
    for kt in token_list:
        if kt.strip() == token.strip():
            return True
    return False
