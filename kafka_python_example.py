import six
import sys

if sys.version_info >= (3, 12, 0):
    sys.modules['kafka.vendor.six.moves'] = six.moves

from kafka import KafkaProducer, KafkaConsumer
import json

producer = KafkaProducer(bootstrap_servers=['localhost:29092'],
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

producer.send('mi_tema', {'mensaje': 'Hola, Kafka!'})
producer.flush()

consumer = KafkaConsumer('mi_tema',
                         bootstrap_servers=['localhost:29092'],
                         auto_offset_reset='earliest',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for mensaje in consumer:
    print(f"Mensaje recibido: {mensaje.value}")
    break 

consumer.close()