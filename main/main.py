from db.database import SessionLocal
from db.query import si_gu_dong_ri, si_gu_dong
from init.consumer import init
from create.create_excel import CreateExcel
import os

excel_title = '과속 상세내역'
excel_sheet_name = '과속 상세내역 주소변환'

os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir('./excel')

excel = CreateExcel(excel_title, excel_sheet_name)
result_file_name_path = os.getcwd() + '/' + excel.save_file_name()

topic = 'overspeed-detail-address'
consumer = init(client_id='consumer1', group_id='test-group1')
consumer.subscribe([topic])

db = SessionLocal()

def create_row(values: list, address: str) -> list:
    return [values[0], values[1], values[2], values[3], address, values[6], values[7]]

try:
    for messages in consumer:
        for values in messages.value:            
            x = float(values[4])
            y = float(values[5])
            result = db.execute(si_gu_dong_ri(x, y)).fetchone()
            if not result:
                result = db.execute(si_gu_dong(x, y)).fetchone()
                
            if result == None:
                result = '제2경인고속도로 인천대교'
            
            address = excel.create_excel(result)
            row = create_row(values, address)
            excel.ws.append(row)
        consumer.commit()

    excel.wb.save(result_file_name_path)
    excel.wb.close()               
except Exception as e:
    print(e)




    
 
