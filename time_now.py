from datetime import datetime,date

def time_get():
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H:%M:%S")
    return {"date":str(today),'time':current_time,'license':'Hà Đức Hậu'}



