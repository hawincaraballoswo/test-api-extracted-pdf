import logging
from openai import AzureOpenAI
from openai.types.chat import ChatCompletionMessage
from config import AzureOpenAISetting

class AzureOpenAi:
    def __init__(self, azure_openai_setting : AzureOpenAISetting):
        self.endpoint = azure_openai_setting.endpoint
        self.api_key = azure_openai_setting.api_key
        self.api_version = azure_openai_setting.api_version
        self.deployment_name = azure_openai_setting.deployment_name

        self.function_calling: dict = {
                            "type": "function",
                            "function": {
                                "name": "get_data_document",
                                "description": "Extrae la información del documento",
                                "parameters": {
                                    "type": "object",
                                    "properties": {
                                        "fecha_radicacion": {
                                            "type": "string",
                                            "description": "Campo fecha que indica la fecha en la que se radicó el documento en el formato DD-MM-YYYY.",
                                        },
                                        "destinario": {
                                            "type": "string",
                                            "description": "Campo usuario que indica el área a la cual se dirige un documento.",
                                        },
                                        "tipo": {
                                            "type": "string",
                                            "description": "Tipo de documento que se carga, refiere a documento legal, interno, recibo, etc.",
                                        },
                                        "asunto": {
                                            "type": "string",
                                            "description": "Motivo del documento (Tipo de reclamo)",
                                        },
                                        "referencia": {
                                            "type": "string",
                                            "description": "Id del documento o caso. Por ejemplo: 'RE2220202230687'.",
                                        },
                                        "observaciones": {
                                            "type": "string",
                                            "description": "Observaciones diligenciadas por el usuario.",
                                        },
                                        "empresa": {
                                            "type": "string",
                                            "description": "Empresa asociada al reclamo (Afinia, Air-e, etc)",
                                        },
                                    },
                                    "required": ["fecha_radicacion", "destinario", "tipo", "asunto", "referencia", "empresa"],
                                },
                            }
                        }

        self.prompt = f"Eres un experto extrayendo información de documentos de reclamos, extrae la información del documento y completa los campos requeridos. Asegúrate de que la información sea precisa y esté en el formato correcto. Si no puedes encontrar un campo, por favor, indícalo como 'N/A'. Asegúrate de que la información sea precisa y esté en el formato correcto."
    
    def extracted_data(self, content_file) -> ChatCompletionMessage :
        client = AzureOpenAI(
            azure_endpoint = self.endpoint, 
            api_key = self.api_key,  
            api_version = self.api_version
        )

        print(f"Extracting data from content: {content_file[:40]}...")

        response = client.chat.completions.create(
            model=self.deployment_name,
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "user", "content": content_file}
            ],
            tools=[self.function_calling],
            tool_choice="auto",
        )

        print("Data extraction completed successfully.")
        print(f"tokens used: {response.usage.total_tokens}")
        print(f"token prompt: {response.usage.prompt_tokens}")
    
        return response.choices[0].message


