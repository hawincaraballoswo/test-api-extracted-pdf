from pydantic import BaseModel, Field

class ParameterRequest(BaseModel):
    name_document :str
    