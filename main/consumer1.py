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

# 하나의 consumer가 특정 하나의 파티션만을 처리하기 위해서 사용
# consumer.assign(TopicPartition('topic2', 0))

db = SessionLocal()

for messages in consumer:
    for value in messages.value:
        x = float(value[4])
        y = float(value[5])
    
        result = db.execute(si_gu_dong_ri(x, y)).fetchone()
        if not result:
            result = db.execute(si_gu_dong(x, y)).fetchone()
            
        combine = result[0] + result[1] + result[2] + result[3]
            
        if not result[3]:
            combine = result[0] + result[1] + result[2]
            
        row = [value[0], value[1], value[2], value[3], combine, value[6], value[7]]
        ws.append(row)
        
            
wb.save("./result.xlsx")
wb.close()
 

    

