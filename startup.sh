#!/bin/bash

# Activar el entorno virtual si es necesario
# source .venv/bin/activate

# Ejecutar la aplicación con Uvicorn
exec uvicorn src.extracted_pdf_api.main:app 
