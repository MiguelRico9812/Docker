FROM python:3.9-slim
WORKDIR /app
COPY server.py .
# Exponemos el puerto UDP
EXPOSE 8080/udp
CMD ["python", "server.py"]