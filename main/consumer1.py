from db.database import SessionLocal
from db.query import si_gu_dong_ri, si_gu_dong
from init.consumer import init

topic = 'topic2'
consumer = init(client_id='consumer1', group_id='test-group1')
consumer.subscribe(topic)

db = SessionLocal()

for messages in consumer:
    for value in messages.value:
        x = float(value[0])
        y = float(value[1])
        
        result = db.execute(si_gu_dong_ri(x, y)).fetchone()
        if not result:
            result = db.execute(si_gu_dong(x, y)).fetchone()
        
        print(result)

