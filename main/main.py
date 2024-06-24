from db.database import SessionLocal
from db.query import si_gu_dong_ri, si_gu_dong
from init.consumer import init
from create.create_excel import CreateExcel

excel_title = '과속 상세내역'
excel = CreateExcel(excel_title)

topic = 'large-message'
consumer = init(client_id='consumer1', group_id='test-group1')
consumer.subscribe(topic)
# 하나의 consumer가 특정 하나의 파티션만을 처리하기 위해서 사용
# consumer.assign(TopicPartition('topic2', 0))

db = SessionLocal()

def __create_row(values: list, address: str) -> list:
    return [values[0], values[1], values[2], values[3], address, values[6], values[7]]

for messages in consumer:
    for values in messages.value:
        x = float(values[4])
        y = float(values[5])
    
        result = db.execute(si_gu_dong_ri(x, y)).fetchone()
        if not result:
            result = db.execute(si_gu_dong(x, y)).fetchone()
            
        address = excel.create_excel(result)
            
        row = __create_row(values, address)
        excel.ws.append(row)
        
excel.wb.save("./result.xlsx")
excel.wb.close()
 

    

