# Definimos la versión de Python a usar
FROM python:3.10

# Definimos la carpeta para el espacio de trabajo
WORKDIR /app
# Creamos una copia del documento con las dependencias a instalar
COPY requirements.txt /app/requirements.txt

# Instalamos las dependencias que necesitamos 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copiamos todo el contenido de la carpeta y lo guardamos en /app/
COPY . /app

# Lanzamos el servidor de uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]