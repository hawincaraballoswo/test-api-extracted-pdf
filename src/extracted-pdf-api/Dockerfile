# Imagen base oficial de Python
FROM python:3.13

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . .

# Instalar las dependencias
RUN pip install --no-cache-dir -r src/extracted-pdf-api/requirements.txt

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 80

# Comando para ejecutar la aplicación con Uvicorn
CMD ["uvicorn", "src.extracted_pdf_api.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
