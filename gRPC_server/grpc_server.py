import grpc
from concurrent import futures
import orders_pb2
import orders_pb2_grpc
from producer import enviar_mensaje  # Importa la función del producer.py
import json
import time

# Implementa el servicio gRPC
class OrderService(orders_pb2_grpc.OrderServiceServicer):
    def SendMessage(self, request, context):
        # Método para enviar mensajes genéricos a Kafka
        print(f"[Servidor] Mensaje recibido: {request.message}")

        # Convertir el mensaje en un diccionario y agregar el timestamp de envío
        mensaje_dict = json.loads(request.message)
        mensaje_dict["timestamp_envio"] = time.time()  # Agregar timestamp actual

        # Enviar el mensaje con el timestamp agregado
        enviar_mensaje(json.dumps(mensaje_dict))
        return orders_pb2.MessageResponse(response="Mensaje enviado a Kafka")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    orders_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("[Servidor] Servidor gRPC en ejecución en el puerto 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
