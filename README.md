# A Kafka-Django example using microservices

## How to use

- Download

```bash
https://www.apache.org/dyn/closer.cgi
```

- Extract:

```bash
tar -xzf kafka_2.13–3.5.0.tgz
```

- Move to kafka directory

```bash
cd kafka_2.13–3.5.0
```

- Generate a Cluster UUID

```bash
 KAFKA_CLUSTER_ID="$(bin/kafka-storage.sh random-uuid)"
```

- Format Log Directories

```
bin/kafka-storage.sh format -t $KAFKA_CLUSTER_ID -c config/kraft/server.properties
```

- Start the Kafka Server

```bash
bin/kafka-server-start.sh config/kraft/server.properties
```

- Create topic

```bash
bin/kafka-console-consumer.sh  --topic topic_user_created  --bootstrap-server localhost:9092 --from-beginning
```

- Use the following command to start listening to the topic

```bash
python3 manage.py launch_queue_listener
```
