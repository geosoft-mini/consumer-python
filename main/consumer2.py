from db.database import SessionLocal
from db.query import si_gu_dong_ri, si_gu_dong
from init.consumer import init
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.title = '과속 상세내역'
column = ['회사코드', '차량번호', '차량ID', '날짜', '주소', '속도', '발생시각']
ws.append(column)

topic = 'large-message'
consumer = init(client_id='consumer2', group_id='test-group1')
consumer.subscribe(topic)

db = SessionLocal()





for message in consumer: # 207
    values = message.value
    for value in values:
        x = float(value[4])
        y = float(value[5])
    
        result = db.execute(si_gu_dong_ri(x, y)).fetchone()
        
        if not result:
            result = db.execute(si_gu_dong(x, y)).fetchone()
            
        try:
            combine = result[0] + result[1] + result[2] + result[3]
        except:
            combine = result[0] + result[1] + result[2]
            
        row = [value[0], value[1], value[2], value[3], combine, value[6], value[7]]
    
        ws.append(row)
        
                
wb.save("./result.xlsx")    
wb.close()  
    
    
    
