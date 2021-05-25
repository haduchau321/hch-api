from fastapi import FastAPI
from pydantic import BaseModel
import time_now
import heroku3
import mails
import outlook
import Checkzalo

token_sever = '6c700e69-198a-4ed0-a3d8-88ec28f3a099'

app = FastAPI()

 
@app.get('/')
async def home_main():
    return time_now.time_get()

@app.get('/tempmail')
async def tempmail():
    return {'Mail':mails.getmail(),'Bản Quyền':'Hà Đứu Hậu','data_time':time_now.time_get()}

@app.get('/tempmail/code&mail={mail}')
async def tempmail_code(mail:str):
    return mails.get_code(mail)

@app.get('/MailTM')
async def MailTM():
    return mails.get_mail_hdh()

@app.get('/MailTM/code&token={token}')
async def MailTM_Code(token:str):
    return mails.get_code_hdh(token)

@app.get('/outlook/email={email}&password={password}')
async def outlook_message(email:str,password:str):
    return outlook.doc_outlook(email,password)

@app.get('/ZaloChecker/phone={phone}&token={token}')
async def ZaloChecker(phone:str,token:str):
    kt = Checkzalo.zalo_key(token)
    if kt == False:
        return {'status':False,'message':'the token is wrong or expired'}
    else:
        to_data = Checkzalo.Zalo_run(phone)
        if to_data['status'] == None:
            heroku_conn = heroku3.from_key(token_sever)
            app = heroku_conn.apps()['api-hch']
            app.restart()
        return to_data
