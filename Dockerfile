# Usa una imagen base de Python
FROM python:3.11-slim

LABEL authors="RCRR"

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto
COPY . .

# Instala las dependencias
RUN pip install -r requirements.txt

# Configura la variable de entorno para producción
ENV DJANGO_SETTINGS_MODULE=rcrr_test.settings

# Expone el puerto
EXPOSE 8080

# Ejecuta el servidor Django
CMD exec gunicorn rcrr_test.wsgi:application --bind :8080 --workers 3
