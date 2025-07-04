from typing import Optional, List
from pydantic import BaseModel, Field

class ExtractResponseRecord(BaseModel):
    """
    Represents a single record in the extraction response.
    """
    contenido_documento: str = Field(..., description="Content of the document")
    fecha_radicacion: str = Field(..., description="Filing date of the document")
    destinatario: str = Field(..., description="Receptor of the document")
    asunto: str = Field(..., description="Subject of the document")
    tipo_documento: str = Field(..., description="Type of the document")
    referencia: str = Field(..., description="Reference of the document")
    observaciones: Optional[str] = Field(..., description="Observations related to the document")
    empresa: str = Field(..., description="Company associated with the document")

class ExtractResponse(BaseModel):
    """
    Represents the response from the PDF extraction process.
    """
    status: str = Field(..., description="Status of the extraction process")
    message: str = Field(..., description="Message providing details about the extraction")
    data: List[ExtractResponseRecord] = Field(..., description="Extracted data from the PDF")  # Adjust type as needed