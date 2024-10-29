from confluent_kafka import Producer
import json
from uuid import uuid4

# Configuración del productor de Kafka
producer_conf = {
    'bootstrap.servers': 'localhost:9093',
    'client.id': 'productor1'
}
producer = Producer(producer_conf)

def delivery_report(err, msg):
    """Callback para confirmar la entrega de mensajes."""
    if err is not None:
        print(f"[Producer] Error al entregar mensaje: {err}")
    else:
        print(f"[Producer] Mensaje enviado a {msg.topic()} [{msg.partition()}]")

def enviar_mensaje(message):
    """Función para enviar un mensaje a Kafka."""
    try:
        
        key = str(uuid4())
        print(f"Key: {key} Produciendo mensaje: {message}")
        producer.produce('el-topico1', key=key.encode('utf-8'), value=message, callback=delivery_report)
        producer.poll(0)  # Procesa las colas del Producer
        producer.flush()  # Espera a que todos los mensajes pendientes sean entregados
    except Exception as e:
        print(f"[Producer] Error al enviar mensaje: {e}")


