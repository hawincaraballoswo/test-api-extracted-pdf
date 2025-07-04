from config import get_settings, Settings

def main():
    settings = get_settings()
    print("✅ Configuración cargada correctamente:")
    print(f"Host: {settings.host}")
    print(f"Puerto: {settings.port}")
    print(f"Log level: {settings.log_level}")
    print(f"Azure OpenAI endpoint: {settings.azure_openai.endpoint}")
    print(f"Azure OpenAI API key: {settings.azure_openai.api_key}")
    print(f"Azure Intelligent Service endpoint: {settings.azure_intelligent_service.endpoint}")
    print(f"Azure Intelligent Service form URL: {settings.azure_intelligent_service.formUrl}")

if __name__ == "__main__":
    main()
