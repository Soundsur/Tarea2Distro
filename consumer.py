from confluent_kafka import Consumer
from elasticsearch import Elasticsearch
import json
import time
from datetime import datetime
import random

consumer_conf = {
    'bootstrap.servers': 'localhost:9093',
    'group.id': 'grupo-consumidor1',
    'auto.offset.reset': 'earliest' 
}
consumer = Consumer(consumer_conf)
consumer.subscribe(['el-topico1'])

# Configuración de Elasticsearch
es = Elasticsearch(["http://localhost:9200"])

def registrar_metrica(metrica, valor, compra_id, estado=None):
    metric_data = {
        "timestamp": datetime.utcnow(),
        "metrica": metrica,
        "valor": valor,
        "compra_id": compra_id
    }
    # Si hay un estado, se agrega al documento
    if estado:
        metric_data["estado"] = estado

    es.index(index="metrics-index", document=metric_data)


# Función para simular diferentes cargas de trabajo
def simular_carga(carga):
    if carga == "baja":
        return 0.5  # 0.5 segundos de espera entre mensajes
    elif carga == "media":
        return 1  # 1 segundo de espera entre mensajes
    elif carga == "alta":
        return 2  # 2 segundos de espera entre mensajes
    else:
        return 1  # Carga media por defecto

print("[Consumidor] Esperando eventos de pedidos...")

# Elegir la carga de trabajo
carga = input("[Consumidor] Seleccione la carga de trabajo (baja, media, alta): ").strip().lower()
delay = simular_carga(carga)

def maquina_estados(compra_id):
   estados = {
       "Procesando": "Preparación",
       "Preparación": "Enviado",
       "Enviado": "Entregado",
       "Entregado": "Finalizado",
       "Finalizado": None
   }
   
   estado_actual = "Procesando"

   while estado_actual is not None:
        # Registrar la métrica de cambio de estado en Elasticsearch
        tiempo_inicio = time.time()
        print(f"Compra {compra_id} - Estado actual: {estado_actual}")
        registrar_metrica("estado_transicion", tiempo_inicio, compra_id, estado=estado_actual)

        # Simular tiempo de procesamiento variable
        tiempo_espera = random.randint(1, 3)
        time.sleep(tiempo_espera)

        # Calcular el tiempo de procesamiento para este estado
        tiempo_procesamiento = time.time() - tiempo_inicio
        registrar_metrica("tiempo_de_procesamiento", tiempo_procesamiento, compra_id, estado=estado_actual)

        # Transición al siguiente estado
        estado_actual = estados[estado_actual]

try:
    start_time = time.time()
    mensajes_procesados = 0

    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            print(f"[Error] {msg.error()}")
            continue

        mensaje = msg.value().decode('utf-8')       #Imprenta de mensajes por consumidor
        print(f"[Consumidor] Evento recibido: {mensaje}")

        try:
            processing_start = time.time()
            message = json.loads(msg.value().decode('utf-8'))

            # Obtener el timestamp de envío del mensaje desde el productor
            tiempo_envio = message.get("timestamp_envio", None)
            if tiempo_envio:
                tiempo_envio = float(tiempo_envio)
                tiempo_total_envio = time.time() - tiempo_envio
                compra_id = msg.key().decode('utf-8')
                registrar_metrica("tiempos_de_envio", tiempo_total_envio, compra_id)


            document = {
                "NombreProducto": message["nombre_producto"],
                "Precio": float(message["precio"]),
                "PasarelaPago": message["pasarela_pago"],
                "MarcaTarjeta": message["marca_tarjeta"],
                "Banco": message["banco"],
                "Region": message["region"],
                "Direccion": message["direccion"],
                "Correo": message["correo"]
            }

            es.index(index="compras-index", document=document)
            print(f"Mensaje recibido e indexado en Elasticsearch: {document}")

            latencia = time.time() - processing_start
            compra_id = msg.key().decode('utf-8')  
            registrar_metrica("latencia", latencia, compra_id)

            # Ejecutar la máquina de estados para la compra
            maquina_estados(compra_id)

            mensajes_procesados += 1
            elapsed_time = time.time() - start_time

            throughput = mensajes_procesados / elapsed_time
            registrar_metrica("throughput", throughput, compra_id)

            time.sleep(delay)

        except json.JSONDecodeError as e:
            print(f"Error decodificando JSON: {e}")

finally:
    consumer.close()
