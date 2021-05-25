import imaplib,re
from bs4 import BeautifulSoup as bs 

def doc_outlook(mail,password):
    msrvr = imaplib.IMAP4_SSL('outlook.office365.com', 993)
    msrvr.login(mail, password)
    # print(str(len(msrvr.select('inbox'))))
    stat,cnt = msrvr.select('inbox')
    # print(str(len(cnt)))
    # for i in range(0,5):
    try:
        stat,dta = msrvr.fetch(cnt[0], '(BODY[TEXT])')
        soup = bs(dta[0][1], "html.parser").find_all('p')
        tinnhan =''
        for tn in soup:
            tinnhan += tn.text+'\n'
        try:
            code = re.findall('[0-9]+', tinnhan)[0]
        except:
            code = None
        data_out = {'TinNhan':tinnhan.replace('\n',' ').replace('=\r',''),'OTP':code}
    except:
        data_out = {'TinNhan':None,'OTP':None}
    msrvr.close()
    msrvr.logout()
    return data_out


# mail = 'minhthao7463@hotmail.com'
# password = 'yeutaodi123'
# tn = doc_outlook(mail,password)
# print(tn)
