#!/bin/bash

# Instalar dependencias
pip install --no-cache-dir -r src/extracted-pdf-api/requirements.txt

# Ejecutar la aplicación con el path completo a uvicorn
exec python -m uvicorn src.extracted_pdf_api.main:app --host 0.0.0.0 --port 8000 --reload
