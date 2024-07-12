
# Usa una imagen de Python oficial como base
FROM python:3.9

# Establece el directorio de trabajo en el directorio raíz de la aplicación Django
WORKDIR /app

# Copia el archivo de requerimientos e instala las dependencias
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copia todo el contenido del directorio actual al directorio de trabajo en el contenedor
COPY . .

# Configura las variables de entorno, si es necesario
# ENV VARIABLE_NAME=value

# Expone el puerto en el que corre la aplicación Django
EXPOSE 8000

# Comando para ejecutar la aplicación Django usando Gunicorn (u otro servidor que prefieras)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "survey_api.wsgi:application"]
