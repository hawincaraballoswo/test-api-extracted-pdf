from functools import lru_cache
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AzureIntelligentServiceSetting(BaseModel):
    endpoint: str = Field(default="")
    api_key: str = Field(default="")
    formUrl: str = Field(default="")

class AzureOpenAISetting(BaseModel):
    endpoint: str = Field(default="")
    api_key: str = Field(default="")
    deployment_name: str = Field(default="o4-mini") 
    api_version: str = Field(default="2024-12-01-preview")

class Settings(BaseSettings):
    port: int = Field(default=80)
    host: str = Field(default="0.0.0.0")
    log_level: str = Field(default="info")
    route_file: str = Field(default="")

    azure_openai: AzureOpenAISetting = Field(default_factory=AzureOpenAISetting)
    azure_intelligent_service: AzureIntelligentServiceSetting = Field(default_factory=AzureIntelligentServiceSetting)
    
    model_config = SettingsConfigDict(env_file=".env.template", env_nested_delimiter="__")

@lru_cache()
def get_settings() -> Settings:
    return Settings()