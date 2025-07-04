import json
import uvicorn
from fastapi import FastAPI
from models.parameter_request import ParameterRequest
from models.extract_response import ExtractResponse, ExtractResponseRecord
from config import Settings, get_settings
from services.extractor_pdf_text import ExtractorPdfText
from services.azure_openai import AzureOpenAi
import logging

app = FastAPI(title="Extracted PDF API", version="1.0.0")

settings: Settings = get_settings()
print(f"Settings loaded: {settings}")

extractor_pdf_text = ExtractorPdfText(settings.azure_intelligent_service)
azure_openai = AzureOpenAi(settings.azure_openai)

@app.post("/extracted-expedients-pdf")
def extracted_pdf(request: ParameterRequest) -> ExtractResponse:
    """
    Extracts text from a PDF file.
    """
    try:
        document_file: str = extractor_pdf_text.extract_text(file_name=request.name_document)
        print(f"Document file extracted: {len(document_file)} characters")
        
        # Call Azure OpenAI to extract structured data from the PDF content
        structured_data = azure_openai.extracted_data(content_file=document_file)
        print(f"Response from Azure OpenAI: {structured_data}")
        if not structured_data:
            raise ValueError("No structured data found in the response from Azure OpenAI.")
        
        # Parse the structured data to extract the function arguments
        data = json.loads(structured_data.tool_calls[0].function.arguments)
        print(f"Extracted data: {data}")

        # Simulate PDF extraction logic here
        response_record : ExtractResponseRecord = ExtractResponseRecord(
            contenido_documento= document_file,
            fecha_radicacion=data.get("fecha_radicacion", ""),
            destinatario=data.get("destinatario", ""),
            asunto=data.get("asunto", ""),
            tipo_documento= data.get("tipo", ""),
            referencia= data.get("referencia", ""),
            observaciones= data.get("observaciones", ""),
            empresa= data.get("empresa", "")
        )
        extracted_response: ExtractResponse = ExtractResponse(
            status="success",
            message="PDF extraction completed successfully.",
            data=[response_record]
        )
        return extracted_response

    except Exception as e:
        # Handle any exceptions that occur during the extraction process
        return ExtractResponse(
            status="error",
            message=f"An error occurred during PDF extraction: {str(e)}",
            data=[]
        )
    



if __name__ == "__main__":
    config = uvicorn.Config(
        "main:app", host=settings.host, port=settings.port, log_level=settings.log_level
    )

    server = uvicorn.Server(config)

    server.run()