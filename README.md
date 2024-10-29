# Tarea2Distro

Sistema distribuido para la gestión logística en una aplicación de ecommerce, implementado como parte de la Tarea 2 del curso de Sistemas Distribuidos.

## Descripción del Proyecto

Este proyecto utiliza una arquitectura distribuida basada en microservicios para gestionar el flujo de pedidos en una aplicación de ecommerce. La comunicación se maneja de manera asíncrona utilizando Kafka y gRPC, y se implementa una máquina de estados finita para gestionar el ciclo de vida de los pedidos. Las métricas de rendimiento se almacenan en Elasticsearch y se visualizan en Kibana.

## Componentes Principales

- **gRPC Server**: Recibe y procesa pedidos enviados desde el cliente gRPC.
- **gRPC Client**: Simula eventos de compra leyendo datos desde un archivo CSV.
- **Producer**: Envía mensajes de pedidos a Kafka.
- **Consumer**: Consume mensajes de Kafka, mide métricas de rendimiento y las indexa en Elasticsearch.
- **Docker Compose**: Configura y ejecuta todos los servicios necesarios en contenedores.

## Requisitos Previos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python 3.9+](https://www.python.org/downloads/)
- [Apache Kafka](https://kafka.apache.org/)
- [gRPC](https://grpc.io/)
- [Elasticsearch](https://www.elastic.co/)

## Configuración

### 1. Clonar el Repositorio
```bash
git clone https://github.com/Soundsur/Tarea2Distro.git
cd Tarea2Distro
```

### 2. Configurar el Entorno Virtual

Crear y activar el entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```
Instalar las dependencias:
```bash
pip install -r gRPC_server/requirements.txt
```
### 3. Generar Archivos gRPC
Navegar a la carpeta del servidor gRPC:
```bash
cd gRPC_server
```

### 4. Navegar a la carpeta del servidor gRPC:

```bash
cd gRPC_server
```
Compilar el archivo orders.proto:

```bash

python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. orders.proto
```
Copiar los archivos generados (orders_pb2.py y orders_pb2_grpc.py) a la carpeta gRPC_client para asegurar la compatibilidad.
Ejecución del Proyecto

#### 1. Iniciar el Sistema con Docker Compose

Desde la raíz del proyecto, ejecutar:

```bash

docker compose up --build
```
Esto iniciará los servicios de Zookeeper, Kafka, Elasticsearch y Kibana. Puedes verificar el estado de Kafka en la interfaz de Kafka-UI accediendo a http://localhost:8080.
#### 2. Ejecutar el Servidor gRPC

En una nueva terminal, activar el entorno virtual e iniciar el servidor:

```bash

source venv/bin/activate
cd gRPC_server
python3 grpc_server.py
```
#### 3. Ejecutar el Cliente gRPC

En otra terminal, activar el entorno virtual y ejecutar el cliente:

```bash

source venv/bin/activate
cd gRPC_client
python3 grpc_client.py
```
Esto enviará eventos de compra al servidor gRPC para su procesamiento.
#### 4. Ejecutar el Consumidor de Kafka

En una nueva terminal, activar el entorno virtual y ejecutar el consumidor:

```bash

source venv/bin/activate
python3 consumer.py
```
Se te pedirá seleccionar el nivel de carga (baja, media, alta) para simular diferentes escenarios de procesamiento.
Visualización de Métricas en Kibana

    Abre Kibana en tu navegador en http://localhost:5601.
    Utiliza las opciones de "Discover" o "Visualize" para explorar las métricas de latencia, throughput, tiempos de envío, y tiempos de procesamiento por estado indexadas en Elasticsearch.

Limpieza del Sistema

Para detener y limpiar todos los contenedores y volúmenes, utiliza el siguiente comando:

```bash

docker compose down --volumes --rmi all --remove-orphans
```
Notas Adicionales

    Asegúrate de activar el entorno virtual en cada terminal antes de ejecutar cualquier componente fuera de Docker.
    El sistema implementa técnicas de escalabilidad y tolerancia a fallos mediante la replicación de mensajes y el manejo de colas en Kafka.
    Se puede añadir funcionalidad adicional, como notificaciones por correo electrónico en los cambios de estado de los pedidos, utilizando el protocolo SMTP.
