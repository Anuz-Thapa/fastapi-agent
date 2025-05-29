from pydantic import BaseModel
from typing import List


class RequestState(BaseModel):   #for vaidation
    model_name:str 
    model_provider:str 
    system_prompt:str 
    message:List[str]
    allow_search:bool