import logging
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
import numpy as np
from config import AzureIntelligentServiceSetting

class ExtractorPdfText:
    def __init__(self, azure_intelligent_service: AzureIntelligentServiceSetting ):
        self.endpoint = azure_intelligent_service.endpoint
        self.api_key = azure_intelligent_service.api_key
        self.formUrl = azure_intelligent_service.formUrl

    def extract_text(self, file_name:str) -> str:
        print(f"Extracting text from PDF file: {self.formUrl}")
        file_url = f"{self.formUrl}/{file_name}"
        print(f"Extracting text from PDF file: {file_url}")

        if not file_url:
            raise ValueError("No content found in the PDF document.")

        document_intelligence_client  = DocumentIntelligenceClient(
            endpoint=self.endpoint, credential=AzureKeyCredential(self.api_key)
        )
        print("Waiting for the document analysis to complete...")

        poller = document_intelligence_client.begin_analyze_document(
            "prebuilt-read", AnalyzeDocumentRequest(url_source=file_url)
        )

        print("Document analysis completed successfully.")

        return poller.result().content




