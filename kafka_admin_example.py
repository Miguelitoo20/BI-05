import six
import sys

if sys.version_info >= (3, 12, 0):
    sys.modules['kafka.vendor.six.moves'] = six.moves

from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaProducer, KafkaConsumer
import json

admin_client = KafkaAdminClient(
    bootstrap_servers=['localhost:29092'],
    client_id='admin_client'
)

topic_list = [NewTopic(name="nuevo_tema1", num_partitions=1, replication_factor=1)]
admin_client.create_topics(new_topics=topic_list, validate_only=False)

producer = KafkaProducer(bootstrap_servers=['localhost:29092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

producer.send('nuevo_tema1', {'mensaje': 'Hola, nuevo tema!'})
producer.flush()

consumer = KafkaConsumer('nuevo_tema1',
                         bootstrap_servers=['localhost:29092'],
                         auto_offset_reset='earliest',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for mensaje in consumer:
    print(f"Mensaje recibido: {mensaje.value}")
    break

consumer.close()

print("Temas existentes:", admin_client.list_topics())

admin_client.close()
