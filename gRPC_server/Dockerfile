FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requerimientos
COPY requirements.txt .

# Instalar las dependencias del archivo requirements.txt
RUN pip install -r requirements.txt

# Copiar todos los archivos del directorio actual al contenedor
COPY . .

# Exponer el puerto 50051 para gRPC
EXPOSE 50051

# Genera los archivos Python desde el archivo .proto
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto

# Comando para ejecutar el servidor gRPC
CMD ["python3", "grpc_server.py"]
