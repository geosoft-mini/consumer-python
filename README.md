```shell
$ python -m venv [가상환경이름]
$ source [가상환경이름]/bin/activate
$ pip install -r requirements.txt

$ docker-compose -f docker-compose/docker-compose-kafka.yml up
$ docker-compose -f docker-compose/docker-compose-postgis.yml

# kafka 토픽 생성 명령어
$ kafka-topics --create --topic overspeed-detail-address --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3

# kafka 토픽 삭제 명령어
$ kafka-topics --delete --bootstrap-server localhost:9092 --topic overspeed-detail-address

# kafka 토픽 생성 리스트 확인
$ kafka-topics --list --bootstrap-server localhost:9092

# kafka lag 확인
$ kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group test-group1
```












