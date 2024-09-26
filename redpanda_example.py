import six
import sys

if sys.version_info >= (3, 12, 0):
    sys.modules['kafka.vendor.six.moves'] = six.moves

from kafka import KafkaProducer, KafkaConsumer, KafkaAdminClient
from kafka.admin import NewTopic
import json
from kafka.errors import TopicAlreadyExistsError

bootstrap_servers = ['localhost:9092']
topic_name = 'mi_tema_redpanda'

def create_topic(topic):
    admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
    try:
        topic_list = [NewTopic(name=topic, num_partitions=1, replication_factor=1)]
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        print(f"Tema '{topic}' creado exitosamente.")
    except TopicAlreadyExistsError:
        print(f"El tema '{topic}' ya existe.")
    finally:
        admin_client.close()

def produce_message(message):
    producer = KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send(topic_name, message)
    producer.flush()
    producer.close()
    print(f"Mensaje enviado: {message}")

def consume_messages():
    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset='earliest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    print("Esperando mensajes...")
    for message in consumer:
        print(f"Mensaje recibido: {message.value}")
        break
    consumer.close()

if __name__ == "__main__":
    create_topic(topic_name)

    produce_message({"clave": "valor", "mensaje": "Hola, Redpanda!"})

    consume_messages()