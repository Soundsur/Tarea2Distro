import grpc
import orders_pb2
import orders_pb2_grpc
import csv
import json

ruta_archivo = '/home/sound/Documents/Distro/Tarea2Distro/gRPC_client/dataset_compras.csv'  # Uso de ruta absoluta

def enviar_compra_json(datos_compra):
    """Función para enviar la solicitud gRPC con los datos de compra en formato JSON."""
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = orders_pb2_grpc.OrderServiceStub(channel)

        # Convertir datos de compra a JSON
        mensaje_json = json.dumps(datos_compra)

        # Crear el mensaje de la solicitud gRPC
        request = orders_pb2.MessageRequest(message=mensaje_json)

        try:
            # Enviar la solicitud gRPC
            response = stub.SendMessage(request)
            print(f"Respuesta del servidor: {response.response}")
        except grpc.RpcError as e:
            print(f"[Cliente] Error en la solicitud gRPC: {e}")

def leer_dataset_y_enviar_compras(archivo_csv, num_consultas=500):
    """Leer el archivo CSV y enviar las compras como mensajes JSON."""
    with open(archivo_csv, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader):
            if i >= num_consultas:
                break

            datos_compra = {
                "nombre_producto": row['NombreProducto'],
                "precio": float(row['Precio']),
                "pasarela_pago": row['PasarelaPago'],
                "marca_tarjeta": row['MarcaTarjeta'],
                "banco": row['Banco'],
                "region": row['Region'],
                "direccion": row['Direccion'],
                "correo": row['Correo']
            }

            enviar_compra_json(datos_compra)

if __name__ == '__main__':
    leer_dataset_y_enviar_compras(ruta_archivo, num_consultas=500)
