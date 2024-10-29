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

1. **Clonar el Repositorio**
   ```bash
   git clone https://github.com/Soundsur/Tarea2Distro.git
   cd Tarea2Distro
