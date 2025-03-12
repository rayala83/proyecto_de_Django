# Usa una imagenbase de python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copiamos los archivos de la aplicacion al contenedor
COPY . /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# expon el puerto 8000 (el que usa Django por ddefecto)
EXPOSE 8000

#Comandos para ejecutar la app
CMD [ "python", "manage.py", "runserver", "0.0.0.0.8000" ]