
```bash
sudo docker exec -it kafka /bin/sh
cd opt/kafka_2.13-2.8.1/bin
kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic first_kafka_topic
kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic diabet_kafka_topic
kafka-topics.sh --list --zookeeper zookeeper:2181


CREATE TABLE ml_predict ( predict VARCHAR ( 50 ) NOT NULL)


sudo docker kill $(sudo docker ps -q)

```