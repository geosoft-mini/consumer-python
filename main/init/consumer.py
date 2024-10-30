
from kafka import KafkaConsumer
from json import loads

def init(client_id, group_id):
    return KafkaConsumer(
        client_id = client_id,
        bootstrap_servers = ['localhost:9092'], # 카프카 브로커 주소 리스트
        auto_offset_reset = 'latest', # 오프셋 위치(earliest:가장 처음, latest: 가장 최근)
        enable_auto_commit = False, # 오프셋 자동 커밋 여부
        group_id = group_id, # 컨슈머 그룹 식별자
        value_deserializer = lambda x: loads(x.decode('utf-8')), # 메시지의 값 역직렬화
        auto_commit_interval_ms = 100000,
        consumer_timeout_ms = 10000,
        max_poll_records = 10,
    )
