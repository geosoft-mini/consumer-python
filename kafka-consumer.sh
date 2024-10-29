# kafka-topics --create --topic overspeed-detail-address --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3
while true : 
do
kafka-consumer-groups --bootstrap-server localhost:9092 --describe --group test-group1

sleep 10
done

kafka-consumer-groups --bootstrap-server localhost:9092 --group test-group1 --topic overspeed-detail-address --reset-offsets --to-earliest --execute

kafka-consumer-groups --bootstrap-server localhost:9092 --group test-group1 --topic overspeed-detail-addres --reset-offsets --to-earliest --dry-run